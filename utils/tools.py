import concurrent.futures
import itertools
import re

from loguru import logger

from datatypes.config import Settings
from datatypes.executor import Executor, Status
from sdk.server import Server
from sdk.telegram import Telegram


def _hide_host(host: str, streamer_mode: bool):
    ip_regex = "^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\" \
               ".(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\" \
               ".(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\" \
               ".(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    if streamer_mode and re.fullmatch(ip_regex, host):
        integers = re.findall('(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', host)
        integers[1] = integers[2] = 'x'
        host = '.'.join(integers)
    return host


def _generate_log_record(settings: Settings, instance: Server, offline: bool, ping_log: str):
    emoji = settings.offline_emoji if offline else settings.online_emoji
    host = _hide_host(host=instance.host, streamer_mode=settings.streamer_mode)

    return settings.message_template.format(
        emoji=emoji,
        name=instance.name,
        host=host,
        ping_log=ping_log
    )


def get_server_instances(servers: dict[str, str], settings: Settings) -> list[Server]:
    instances = []
    for server in servers.items():
        instances.append(Server(name=server[0], host=server[1], settings=settings))
    return instances


def ping_pool(server_instances: list[Server], telegram: Telegram, settings: Settings):
    indexes = range(0, len(server_instances))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(_main_executor, indexes,
                               itertools.repeat(server_instances),
                               itertools.repeat(telegram),
                               itertools.repeat(settings))

    for result in results:
        if result.status.name == 'log':
            logger.info(result.message)
        if result.status.name == 'warn':
            logger.warning(result.message)
        if result.status.name == 'error':
            logger.error(result.message)


def _main_executor(index: int, server_instances: list[Server], telegram: Telegram, settings: Settings):
    instance = server_instances[index]
    server = instance.ping()
    if server.is_offline:
        warn = _generate_log_record(settings=settings,
                                   instance=instance,
                                   offline=True,
                                   ping_log=server.ping_log)
        response = telegram.send_message(warn)
        if not response.ok:
            return Executor(
                status=Status.error,
                message=f"{warn} telegram response is not ok. "
                        f"code: {response.error_code}, "
                        f"description: {response.description}."
            )
        else:
            return Executor(
                status=Status.warn,
                message=f"{warn} telegram message successfully sent."
            )
    else:
        return Executor(
            status=Status.log,
            message=_generate_log_record(
                settings=settings,
                instance=instance,
                offline=False,
                ping_log=server.ping_log
            )
        )
