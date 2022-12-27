from pydantic import BaseModel


class Packets(BaseModel):
    transmitted: int
    received: int
