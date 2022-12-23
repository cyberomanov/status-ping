import requests

from datatypes.telegram_response import TelegramResponse


class Telegram:
    def __init__(self, bot_api_token: str, alarm_chat_id: str):
        self.bot_api_token = bot_api_token
        self.alarm_chat_id = alarm_chat_id

    def send_message(self, message: str) -> TelegramResponse:
        response = requests.post(
            f"https://api.telegram.org/bot{self.bot_api_token}/sendMessage",
            json={
                "chat_id": self.alarm_chat_id,
                "text": f"<code>{message}</code>",
                "parse_mode": "HTML",
            }
        ).json()
        return TelegramResponse.parse_obj(response)
