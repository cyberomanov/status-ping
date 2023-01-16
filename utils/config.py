import os

from yaml import safe_load

from datatypes.config import Config


def get_config(config_path: str = r"%s/config.yaml" % os.getcwd()) -> Config:
    with open(config_path, encoding='UTF-8') as data:
        return Config.parse_obj(safe_load(data))
