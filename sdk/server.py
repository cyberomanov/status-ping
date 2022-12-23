import os
import subprocess


class Server:
    PING_COUNT = 5

    def __init__(self, host: str, name: str):
        self.host = host
        self.name = name

    def is_offline(self) -> bool:
        with open(os.devnull, 'w') as DEVNULL:
            try:
                subprocess.check_call(
                    ['ping', '-c', f'{Server.PING_COUNT}', f'{self.host}'],
                    stdout=DEVNULL,
                    stderr=DEVNULL
                )
            except subprocess.CalledProcessError:
                return True
            else:
                return False
