from telebot.types import Message, ReplyKeyboardRemove

from data.loader import db, bot
from keyboards.default import make_buttons
from config import ADMINS

admin_buttons_names = [
        "➕ Sayohatlar qo'shish",
        "➕ Mashhur joylar qo'shish",
        "➕ Ekskursiya jadvali qo'shish"
    ]

TRAVEL = {}

@bot.message_handler(func=lambda message: message.text == "👮Admin buyruqlari")
def reaction_to_admin_commands(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    if from_user_id in ADMINS:
        bot.send_message(chat_id, "Admin buyruqlari",
                        reply_markup=make_buttons(admin_buttons_names, back=True))

@bot.message_handler(func=lambda message: message.text == "➕ Sayohatlar qo'shish")
def reaction_to_admin_commands(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    if from_user_id in ADMINS:
        msg = bot.send_message(chat_id, "Sayohat nomini kiriting",
                               reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, get_name_travel)

def get_name_travel(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    TRAVEL[from_user_id] = {
        "name": message.text
    }
    msg = bot.send_message(chat_id, "Sayohat narxini kiriting")
    bot.register_next_step_handler(msg, get_price_travel)

def get_price_travel(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    TRAVEL[from_user_id]["price"] = message.text
    msg = bot.send_message(chat_id, "Sayohat davomiyligini(kun) kiriting")
    bot.register_next_step_handler(msg, get_days_travel)

def get_days_travel(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    days = int(message.text)
    name = TRAVEL[from_user_id]["name"]
    price = float(TRAVEL[from_user_id]["price"])
    db.insert_travel(name, price, days)
    bot.send_message(chat_id, "Sayohat saqlandi!",
                     reply_markup=make_buttons(admin_buttons_names, back=True))