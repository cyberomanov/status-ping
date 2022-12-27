import concurrent.futures
import itertools
import os

from loguru import logger

from datatypes.config import Settings
from datatypes.executor import Executor, Status, Server
from sdk.telegram import Telegram
from utils.tools import generate_log_record, get_packets, get_ping_result


Perc = float


class PingExecutor:
    PING_COUNT = 5
    PING_INTERVAL = 1
    MAX_PACKETS_LOSS: Perc = 80

    def __init__(self, instances: list[Server], telegram: Telegram, settings: Settings):
        self.instances = instances
        self.telegram = telegram
        self.settings = settings
        self.indexes = range(0, len(self.instances))

    def start(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(self._main_executor, self.indexes)

        for result in results:
            if result.status.value == 'log':
                logger.info(result.message)
            if result.status.value == 'warn':
                logger.warning(result.message)
            if result.status.value == 'error':
                logger.error(result.message)

    def _main_executor(self, index: int):
        instance = self.instances[index]
        ping = os.popen(f"ping {instance.host} -c {PingExecutor.PING_COUNT} -i {PingExecutor.PING_INTERVAL}").read()

        if not ping:
            return self._generate_warn(instance=instance, text='unknown host')
        else:
            ping_result = get_ping_result(response=ping)
            packets = get_packets(ping_result=ping_result)

            if packets.transmitted:
                packets_loss = 100 - ((packets.received * 100) / packets.transmitted)
                if packets_loss > PingExecutor.MAX_PACKETS_LOSS:
                    return self._generate_warn(instance=instance, text=ping_result)
                else:
                    return self._generate_log(instance=instance, text=ping_result)

    def _generate_warn(self, instance: Server, text: str) -> Executor:
        warn = generate_log_record(settings=self.settings,
                                   instance=instance,
                                   offline=True,
                                   ping_log=text)
        response = self.telegram.send_message(warn)
        if not response.ok:
            return Executor(
                status=Status.ERROR,
                message=f"{warn} telegram response is not ok. "
                        f"code: {response.error_code}, "
                        f"description: {response.description}."
            )
        else:
            return Executor(
                status=Status.WARN,
                message=f"{warn} telegram message successfully sent."
            )

    def _generate_log(self, instance: Server, text: str) -> Executor:
        return Executor(
            status=Status.LOG,
            message=generate_log_record(
                settings=self.settings,
                instance=instance,
                offline=False,
                ping_log=text
            )
        )
