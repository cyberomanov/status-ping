from pydantic import BaseModel


class Settings(BaseModel):
    bot_api_key: str
    alarm_chat_id: str
    sleep_time_between_loops: int
    log_output: str
    log_rotation: str
    online_emoji: str
    offline_emoji: str
    message_template: str
    streamer_mode: bool


class Config(BaseModel):
    servers: dict[str, str]
    settings: Settings
