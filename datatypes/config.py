from pydantic import BaseModel


class Settings(BaseModel):
    bot_api_key: str
    alarm_chat_id: str
    log_output: str
    log_rotation: str
    online_emoji: str
    offline_emoji: str
    message_template: str
    streamer_mode: bool
    packets_loss_for_alarm: int


class Config(BaseModel):
    servers: dict[str, str]
    settings: Settings
