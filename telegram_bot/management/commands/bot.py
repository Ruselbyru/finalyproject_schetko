from django.core.management.base import BaseCommand
from avtootvet import settings
from telegram import Bot,Update
from telegram.ext import CallbackContext,Filters,MessageHandler,Updater
from telegram.utils.request import Request
from clientrequest.models import ClientRequest
from django.db.models.signals import post_save
from django.dispatch import receiver



#декоратор ошибок
def log_errors (f):
    def inner (*args,**kwargs):
        try:
            return f(*args,**kwargs)
        except Exception as e:
            error_message = f'Ошибка: {e}'
            print(error_message)
            raise e
    return inner

#echo bot
@log_errors
def do_echo (update: Update, context:CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    reply_text = f"Your ID= {chat_id}\n{text}"
    update.message.reply_text(text=reply_text)


class Command (BaseCommand):
    help = 'Telegram_bot'

    def handle(self, *args, **options):

        #connect
        request = Request(connect_timeout=0.5, read_timeout=1.0)

        bot = Bot (request=request, token=settings.TOKEN)
        print(bot.get_me())

        #обработчик сообщений
        updater = Updater(bot=bot, use_context=True)
        message_handler = MessageHandler(Filters.text,do_echo)
        updater.dispatcher.add_handler(message_handler)

        #запуск бесконечной обработки входящих сообщений
        updater.start_polling()
        updater.idle()