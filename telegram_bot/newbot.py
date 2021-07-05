import requests
from avtootvet import settings
import json
from .models import Shop_telegram
from shoprequest.models import Shoprequest

#API для обращения к телеграмму
URL = f'https://api.telegram.org/bot{settings.TOKEN}/'

#Запись WebHook в файл
def write_json(data, filename = 'answer.json'):
    with open(f'static/{filename}', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

#Отправка сообщения
def send_message(chat_id, text='bla-bla-bla'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text':text}
    r = requests.post(url, json=answer)
    return r.json()

#Обработка в случаи получения сообщения с командой Login
def login (chat_id,unp):
    if Shoprequest.objects.filter(shopunp=unp[-1]):
        shop = Shoprequest.objects.get(shopunp=unp[-1])
        try:
            Shop_telegram.objects.create(shopname=shop, telegram_id=chat_id, subscribe=True)
        except Exception:
            send_message(chat_id, text=f'Вы уже авторизированы!')
        else:
            send_message(chat_id, text=f'Авторизация прошла успешно, заявки скоро появятся!')
    else:
        send_message(chat_id, text=f'Проверьте УНП или зарегестируйтесь на сайте АВТООТВЕТ')

#Обработка в случаи получения сообщения с командой Unsubscribe
def unsubscribe (chat_id):
    if Shop_telegram.objects.filter(telegram_id=chat_id):
        shop = Shop_telegram.objects.get(telegram_id=chat_id)
        shop.subscribe = False
        shop.save()
        send_message(chat_id, text='Вы больше не будите получать уведомлений =(')
    else:
        send_message(chat_id, text='Ваш профиль не найден!')

#Обработка в случаи получения сообщения с командой Subscribe
def subscribe (chat_id):
    if Shop_telegram.objects.filter(telegram_id=chat_id):
        shop = Shop_telegram.objects.get(telegram_id=chat_id)
        shop.subscribe = True
        shop.save()
        send_message(chat_id, text='Теперь Вы будите получать уведомления =)')
    else:
        send_message(chat_id, text='Ваш профиль не найден!')




# https://api.telegram.org/bot1814873441:AAEsaxbtbW7M0VxHMm9b2r77z5-7Xoaa7e4/setWebhook?url=https://avtootvet.herokuapp.com
# https://api.telegram.org/bot1814873441:AAEsaxbtbW7M0VxHMm9b2r77z5-7Xoaa7e4/deleteWebhook