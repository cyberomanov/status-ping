from pydantic import BaseModel


class Server(BaseModel):
    host: str
    name: str
