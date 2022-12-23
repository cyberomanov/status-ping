import re

from loguru import logger

from datatypes.config import Settings
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


def generate_log_record(settings: Settings, instance: Server, offline: bool, ping_log: str):
    emoji = settings.offline_emoji if offline else settings.online_emoji
    host = _hide_host(host=instance.host, streamer_mode=settings.streamer_mode)

    return settings.message_template.format(
        emoji=emoji,
        name=instance.name,
        host=host,
        ping_log=ping_log
    )


def get_server_instances(servers: dict[str, str]) -> list[Server]:
    instances = []
    for server in servers.items():
        instances.append(Server(name=server[0], host=server[1]))
    return instances


def send_telegram_warn(telegram: Telegram, warn: str):
    response = telegram.send_message(warn)
    if not response.ok:
        logger.error(f"{warn} telegram response is not ok. "
                     f"code: {response.error_code}, "
                     f"description: {response.description}.")
    else:
        logger.warning(f"{warn} telegram message successfully sent.")
