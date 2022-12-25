from loguru import logger

from sdk.telegram import Telegram
from utils.create_logger import create_logger
from utils.get_config import get_config
from utils.tools import get_server_instances, ping_pool


def ping():
    try:
        config = get_config()
        settings, servers = config.settings, config.servers
        create_logger(log_output=settings.log_output, log_rotation=settings.log_rotation)
        telegram = Telegram(bot_api_token=settings.bot_api_key, alarm_chat_id=settings.alarm_chat_id)
        server_instances = get_server_instances(servers=servers, settings=settings)
    except Exception as e:
        logger.exception(e)
    else:
        try:
            ping_pool(server_instances=server_instances, telegram=telegram, settings=settings)
        except Exception as e:
            logger.exception(e)
        except KeyboardInterrupt:
            exit()


if __name__ == '__main__':
    ping()
