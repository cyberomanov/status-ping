from loguru import logger

from sdk.utils import init_logger, ping_servers

if __name__ == '__main__':
    init_logger()
    while True:
        try:
            ping_servers()
        except Exception as e:
            logger.exception(e)
