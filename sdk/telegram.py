import requests

from datatypes.telegram import Response


class Telegram:
    def __init__(self, bot_api_token: str, alarm_chat_id: str):
        self.bot_api_token = bot_api_token
        self.alarm_chat_id = alarm_chat_id

    def send_message(self, message: str) -> Response:
        response = requests.post(
            f"https://api.telegram.org/bot{self.bot_api_token}/sendMessage",
            json={
                "chat_id": self.alarm_chat_id,
                "text": f"<code>{message}</code>",
                "parse_mode": "HTML",
            }
        ).json()
        return Response.parse_obj(response)
