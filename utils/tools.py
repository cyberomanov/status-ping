import re

from datatypes.config import Settings
from datatypes.ping import Packets
from datatypes.executor import Server


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


def get_ping_result(response: str) -> str:
    return re.findall('\d+.*?loss', response)[0]


def get_packets(ping_result: str) -> Packets:
    packets = re.findall('\d+', ping_result)
    return Packets(transmitted=int(packets[0]), received=int(packets[1]))
