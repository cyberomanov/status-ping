from loguru import logger

from sdk.executor import PingExecutor
from sdk.telegram import Telegram
from utils.config import get_config
from utils.logger import add_logger
from utils.tools import get_server_instances


def ping():
    try:
        add_logger()
        config = get_config()
        PingExecutor(
            instances=get_server_instances(servers=config.servers),
            telegram=Telegram(
                bot_api_token=config.settings.bot_api_key,
                alarm_chat_id=config.settings.alarm_chat_id
            ),
            settings=config.settings
        ).start()
    except Exception as e:
        logger.exception(e)
    except KeyboardInterrupt:
        exit()


if __name__ == '__main__':
    ping()
