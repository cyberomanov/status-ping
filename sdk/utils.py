import time
from sys import stderr

from loguru import logger

from config import *
from sdk.server import Server
from sdk.telegram import TelegramBot


def init_logger(output_log_path: str = OUTPUT_LOG_PATH, rotation: str = "500 MB"):
    logger.remove()
    logger.add(stderr, format="<bold><blue>{time:HH:mm:ss}</blue>"
                              " | <level>{level}</level>"
                              " | <level>{message}</level></bold>")
    logger.add(sink=output_log_path, rotation=rotation)


def ping_servers():
    telegram = TelegramBot()
    for server in SERVERS:
        ip = SERVERS[server]
        instance = Server(ip=ip)
        if not instance.is_server_online():
            logger.warning(f"{OFFLINE_EMOJI}  {server} /// {ip} {OFFLINE_EMOJI}")
            telegram.send_message(message=f"<code>{OFFLINE_EMOJI} {server} /// {ip} {OFFLINE_EMOJI}</code>")
        else:
            logger.info(f"{ONLINE_EMOJI}  {server} /// {ip} {ONLINE_EMOJI}")
    time.sleep(TIME_SLEEP_BETWEEN_PINGS_SEC)
