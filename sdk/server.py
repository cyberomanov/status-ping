import os
import re

from datatypes.config import Settings
from datatypes.ping import Ping, Packets


class Server:
    PING_COUNT = 50
    PING_INTERVAL = 1

    def __init__(self, host: str, name: str, settings: Settings):
        self.host = host
        self.name = name
        self.settings = settings

    @staticmethod
    def _parse_ping_log(response: str) -> str:
        return re.findall('\d+.*?loss', response)[0]

    @staticmethod
    def _get_packets(ping_log: str) -> Packets:
        packets = re.findall('\d+', ping_log)
        return Packets(transmitted=int(packets[0]), received=int(packets[1]))

    def ping(self) -> Ping:
        response = os.popen(f"ping {self.host} -c {Server.PING_COUNT} -i {Server.PING_INTERVAL}").read()
        if not response:
            return Ping(is_offline=True, ping_log=f'unknown host')
        else:
            ping_log = self._parse_ping_log(response=response)
            packets = self._get_packets(ping_log=ping_log)
            if packets.transmitted:
                packets_loss = 100 - ((packets.received * 100) / packets.transmitted)
                if packets_loss > self.settings.packets_loss_for_alarm:
                    return Ping(is_offline=True, ping_log=ping_log)
                else:
                    return Ping(is_offline=False, ping_log=ping_log)
