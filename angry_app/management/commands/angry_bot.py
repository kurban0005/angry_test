import telebot
import os

from django.contrib.auth import login, authenticate
from django.core.management.base import BaseCommand
from django.shortcuts import redirect

from dotenv import load_dotenv, find_dotenv
from users.models import User

load_dotenv(find_dotenv())
bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))


class Command(BaseCommand):
    help = 'Run your Telegram-bot'

    def handle(self, *args, **options):
        bot.infinity_polling()


@bot.message_handler(commands=['start'])
def start(message):
    telegram_id = message.chat.id
    token = message.text.split()[1] if len(message.text.split()) > 1 else None
    if token is not None:
        try:
            user = User.objects.update_or_create(username=message.from_user.username,
                                                 telegram_id=telegram_id,
                                                 token=token)
            bot.send_message(chat_id=telegram_id,
                             text=f"Вход выполнен успешно")
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton("на сайт", url=f'http://{os.getenv("DOMAIN")}/'))
            bot.send_message(message.chat.id, "Вернуться", reply_markup=markup)

        except Exception as e:
            print(f'Ошибка при обработке сообщения: {e}')
            bot.send_message(chat_id=telegram_id,
                             text="Произошла ошибка при попытке входа. Попробуйте еще раз.")
    else:
        bot.send_message(chat_id=telegram_id,
                         text="Для того, что-бы войти в аккаунт перейдите по ссылке на сайте")