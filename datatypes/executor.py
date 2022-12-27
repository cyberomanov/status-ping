from enum import Enum

from pydantic import BaseModel


class Status(Enum):
    LOG = 'log'
    WARN = 'warning'
    ERROR = 'error'


class Executor(BaseModel):
    status: Status
    message: str

class Server(BaseModel):
    host: str
    name: str
