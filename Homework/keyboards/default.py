from typing import Optional
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from config import TEXTS, ADMINS


def phone_button(name):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(name, request_contact=True)
    markup.add(btn)
    return markup


def make_buttons(names: list, row_width: int = 2, back: bool = False, lang: str = "uz", admin_id: Optional[int] = None):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
    buttons = []
    for name in names:
        btn = KeyboardButton(name)
        buttons.append(btn)
    markup.add(*buttons)

    if admin_id in ADMINS:
        btn = KeyboardButton("👮Admin buyruqlari")
        markup.add(btn)

    if back:
        if lang:
            text = "⬅️ Ortga"
            if lang == "uz":
                text = "⬅️ Ortga"
            elif lang == "ru":
                text = "⬅️ Назад"
            elif lang == "en":
                text = "⬅️ Back"
            btn = KeyboardButton(text)
            markup.add(btn)

    return markup