import requests

from bot.tg import _dc


class TgClient:
    def __init__(self, token):
        self.token = token

    def get_url(self, method: str):
        return f'https://api.telegram.org/bot{self.token}/{method}'

    def get_updates(self, offset: int = 0, timeout: int = 60) -> _dc.GetUpdatesResponse:
        url = self.get_url('getUpdates')

        response = requests.get(url, params={"offset": offset, "timeout": timeout})

        return _dc.GET_UPDETES_SCHEMA.load(response.json())

    def send_message(self, chat_id: int, text: str) -> _dc.SendMessageResponse:
        url = self.get_url('sendMessage')

        
        response = requests.post(url, params={"chat_id": chat_id, "text": text})

        return _dc.SEND_MESSAGE_RESPONSE_SCHEMA.load(response.json())
