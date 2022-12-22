from dataclasses import field
from typing import List, Optional, ClassVar, Type, List

from marshmallow_dataclass import dataclass
from marshmallow import EXCLUDE
import marshmallow_dataclass

@dataclass
class MessageFrom:
    """Telegram API: https://core.telegram.org/bots/api#user"""
    id: int
    is_bot: bool
    first_name: str | None
    last_name: str | None
    username: str

    
    class Meta:
        unknown = EXCLUDE


@dataclass
class Chat:
    """Telegram API: https://core.telegram.org/bots/api#chat"""
    
    id: int
    first_name: str | None
    username: str | None
    last_name: str | None
    type: str
    title: str | None

    class Meta:
        unknown = EXCLUDE


@dataclass
class Message:
    """Telegram API: https://core.telegram.org/bots/api#message"""

    message_id: int
    from_: MessageFrom = field(metadata={'data_key': 'from'})
    chat: Chat
    date: int
    text: str | None

    class Meta:
        unknown = EXCLUDE


@dataclass
class UpdateObj:
    """Telegram API: https://core.telegram.org/bots/api#getting-updates"""
    update_id: int
    message: Message


    class Meta:
        unknown = EXCLUDE


@dataclass
class GetUpdatesResponse:
    """https://core.telegram.org/bots/api#getupdates"""
    ok: bool
    result: List[UpdateObj]
    class Meta:
        unknown = EXCLUDE
    

@dataclass
class SendMessageResponse:
    """https://core.telegram.org/bots/api#sendmessage"""
    ok: bool
    result: Message
    class Meta:
        unknown = EXCLUDE


GET_UPDETES_SCHEMA = marshmallow_dataclass.class_schema(GetUpdatesResponse)()
SEND_MESSAGE_RESPONSE_SCHEMA = marshmallow_dataclass.class_schema(SendMessageResponse)()
