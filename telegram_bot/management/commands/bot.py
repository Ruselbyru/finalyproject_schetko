from django.core.management.base import BaseCommand
from avtootvet import settings
from clientrequest.models import ClientRequest
from django.db.models.signals import post_save
from django.dispatch import receiver
import telebot




class Command (BaseCommand):
    help = 'Telegram_bot'


    def handle(self, *args, **options):

        bot = telebot.TeleBot(settings.TOKEN)

        @bot.message_handler(commands=['start'])
        def welcome (message):
            sticer = open('static/sticker.webp', 'rb')
            bot.send_sticker(message.chat.id, sticer)
            bot.send_message(message.chat.id, 'Welcome')

        @bot.message_handler(content_types=['text'])
        def echo (message):
            bot.send_message(message.chat.id,f'ваш id {message.from_user.id}')


        @bot.message_handler()
        def testing(self):
            bot.send_message(586349284, '1')

        testing('kop')



        bot.polling(none_stop=True)


