from pydantic import BaseModel


class Settings(BaseModel):
    bot_api_key: str
    alarm_chat_id: str

    streamer_mode: bool

    online_emoji: str
    offline_emoji: str
    message_template: str


class Config(BaseModel):
    servers: dict[str, str]
    settings: Settings
