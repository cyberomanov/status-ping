from pydantic import BaseModel


class Server(BaseModel):
    host: str
    name: str
    is_offline: bool = True
