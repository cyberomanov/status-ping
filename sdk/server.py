import os
import re

from datatypes.ping import Ping, Packets


class Server:
    PING_COUNT = 5
    PING_INTERVAL = 2

    def __init__(self, host: str, name: str):
        self.host = host
        self.name = name

    @staticmethod
    def _parse_ping_log(response: str) -> str:
        return re.findall('\d+ packets transmitted, \d+ packets received', response)[0]

    @staticmethod
    def _get_packets(ping_log: str) -> Packets:
        packets = re.findall('\d+', ping_log)
        return Packets(transmitted=int(packets[0]), received=int(packets[1]))

    def ping(self) -> Ping:
        response = os.popen(f"ping {self.host} -c {Server.PING_COUNT} -i {Server.PING_INTERVAL}").read()
        if not response:
            return Ping(is_offline=True, ping_log=f'cannot resolve {self.host}: unknown host')
        else:
            ping_log = self._parse_ping_log(response=response)
            packets = self._get_packets(ping_log=ping_log)
            if packets.transmitted and packets.transmitted == packets.received:
                return Ping(is_offline=False, ping_log=ping_log)
            else:
                return Ping(is_offline=True, ping_log=ping_log)
