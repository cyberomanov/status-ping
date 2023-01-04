import concurrent.futures
import os
import re

from loguru import logger

from datatypes.config import Settings
from datatypes.packets import Packets
from datatypes.server import Server
from sdk.telegram import Telegram

Perc = float
Sec = int


class PingExecutor:
    PING_COUNT = 5
    PING_INTERVAL: Sec = 1
    MAX_PACKETS_LOSS: Perc = 80

    def __init__(self, settings: Settings, telegram: Telegram, instances: list[Server]):
        self.settings = settings
        self.telegram = telegram
        self.instances = instances

        self.indexes = range(0, len(self.instances))

    def start(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self._main_executor, self.indexes)

    def _main_executor(self, index: int):
        instance = self.instances[index]
        ping = os.popen(f"ping {instance.host} -c {PingExecutor.PING_COUNT} -i {PingExecutor.PING_INTERVAL}").read()

        if not ping:
            self._print_warn(instance=instance, text='unknown host')
        else:
            ping_result = self._get_ping_result(ping=ping)
            packets = self._get_packets(ping_result=ping_result)

            if packets.transmitted:
                packets_loss = 100 - ((packets.received * 100) / packets.transmitted)
                if packets_loss > PingExecutor.MAX_PACKETS_LOSS:
                    self._print_warn(instance=instance, text=ping_result)
                else:
                    instance.is_offline = False
                    self._print_log(instance=instance, text=ping_result)

    def _print_warn(self, instance: Server, text: str):
        warn = self._generate_log_record(instance=instance, text=text)
        response = self.telegram.send_message(message=warn)
        if not response.ok:
            logger.error(
                f"{warn} telegram response is not ok. "
                f"code: {response.error_code}, "
                f"description: {response.description}."
            )
        else:
            logger.warning(
                f"{warn} telegram message successfully sent."
            )

    def _print_log(self, instance: Server, text: str):
        logger.info(
            self._generate_log_record(instance=instance, text=text)
        )

    def _generate_log_record(self, instance: Server, text: str):
        emoji = self.settings.offline_emoji if instance.is_offline else self.settings.online_emoji

        return self.settings.message_template.format(
            emoji=emoji,
            name=instance.name,
            host=self._hide_host(host=instance.host),
            text=text
        )

    def _hide_host(self, host: str):
        ip_regex = "^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\" \
                   ".(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\" \
                   ".(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\" \
                   ".(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

        if self.settings.streamer_mode and re.fullmatch(ip_regex, host):
            integers = re.findall('(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', host)
            integers[1] = integers[2] = 'x'
            host = '.'.join(integers)
        return host

    @staticmethod
    def _get_ping_result(ping: str) -> str:
        return re.findall('\d+.*?loss', ping)[0]

    @staticmethod
    def _get_packets(ping_result: str) -> Packets:
        packets = re.findall('\d+', ping_result)
        return Packets(transmitted=int(packets[0]), received=int(packets[1]))
