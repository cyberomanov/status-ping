from loguru import logger

from sdk.executor import PingExecutor
from sdk.telegram import Telegram
from utils.config import get_config
from utils.instance import get_server_instances
from utils.logger import add_logger


def ping():
    try:
        add_logger()
        servers, settings = get_config().servers, get_config().settings

        telegram = Telegram(
            bot_api_token=settings.bot_api_key,
            alarm_chat_id=settings.alarm_chat_id
        )
        instances = get_server_instances(servers=servers)

        PingExecutor(
            settings=settings,
            telegram=telegram,
            instances=instances
        ).start()
    except Exception as e:
        logger.exception(e)
    except KeyboardInterrupt:
        exit()


if __name__ == '__main__':
    ping()
