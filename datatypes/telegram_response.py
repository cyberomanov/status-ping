from pydantic import BaseModel


class TelegramResponse(BaseModel):
    ok: bool
    error_code: int | None
    description: str | None
