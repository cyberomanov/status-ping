from enum import Enum

from pydantic import BaseModel


class Status(Enum):
    log = 'log'
    warn = 'warning'
    error = 'error'


class Executor(BaseModel):
    status: Status
    message: str
