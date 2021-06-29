from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot,Update
from telegram.ext import CallbackContext,Filters,MessageHandler,Updater
from telegram.utils.request import Request




class Command (BaseCommand):
    help = 'Telegram_bot'

    def handle(self, *args, **options):
        #connect
        request = Request(connect_timeout=0.5, read_timeout=1.0)

        bot = Bot (request=request, token=settings.TOKEN, base_url=settings.PROXY_URL)
        print(bot.get_me())