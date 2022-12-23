from pydantic import BaseModel


class Ping(BaseModel):
    is_offline: bool
    ping_log: str


class Packets(BaseModel):
    transmitted: int
    received: int
