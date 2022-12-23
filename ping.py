import time

from loguru import logger

from sdk.telegram import Telegram
from utils.create_logger import create_logger
from utils.get_config import get_config
from utils.tools import send_telegram_warn, generate_log_record, get_server_instances


def ping():
    try:
        config = get_config()
        settings, servers = config.settings, config.servers
        create_logger(log_output=settings.log_output, log_rotation=settings.log_rotation)
        telegram = Telegram(bot_api_token=settings.bot_api_key, alarm_chat_id=settings.alarm_chat_id)
        server_instances = get_server_instances(servers=servers)
    except Exception as e:
        logger.exception(e)
    else:
        while True:
            try:
                for instance in server_instances:
                    if instance.is_offline():
                        warn = generate_log_record(settings=settings, instance=instance, offline=True)
                        send_telegram_warn(telegram=telegram, warn=warn)
                    else:
                        logger.info(generate_log_record(settings=settings, instance=instance, offline=False))
                logger.success(f"next check-up in {settings.sleep_time_between_loops} sec/s.")
                time.sleep(settings.sleep_time_between_loops)
            except Exception as e:
                logger.exception(e)
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    ping()
