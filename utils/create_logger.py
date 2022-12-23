from sys import stderr

from loguru import logger


def create_logger(log_output: str, log_rotation: str):
    logger.remove()
    logger.add(
        stderr,
        format="<bold><blue>{time:HH:mm:ss}</blue> | <level>{level}</level> | <level>{message}</level></bold>"
    )
    logger.add(sink=log_output, rotation=log_rotation)

    print(
        "┌ ----------------------------------------------- ┐\n"
        "|                    PING {sv}                    |\n"
        "| ----------------------------------------------- |\n"
        "|            with love by @cyberomanov            |\n"
        "└ ----------------------------------------------- ┘".format(sv='v2.0')
    )
