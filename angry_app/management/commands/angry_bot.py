import telebot
import os
from django.core.management.base import BaseCommand
from django.shortcuts import redirect
from dotenv import load_dotenv, find_dotenv
# from django.contrib.auth.models import User
from users.models import User

load_dotenv(find_dotenv())


class Command(BaseCommand):
    help = 'Run your Telegram-bot'

    def handle(self, *args, **options):
        """Make a bot and start work."""
        bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))

        @bot.message_handler(commands=['wow'])
        def ww(message):
            bot.send_message(message.chat.id, 'WOW')

        @bot.message_handler(commands=['start'])
        def start(message):
            telegram_id = message.chat.id
            user = User.objects.create_user(f'TG_{telegram_id}', 'none@none.com', "12345")
            markup = telebottypes.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton("на сайт", url=f'http://{os.getenv("DOMAIN")}/'))
            bot.send_message(message.chat.id, "Вернуться", reply_markup=markup)



        bot.infinity_polling()
