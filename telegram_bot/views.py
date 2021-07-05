from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .newbot import write_json,send_message, login, unsubscribe, subscribe
import json



# Create your views here.
# Обработка Webhook от Телеграмма с вызовом фн бота
@csrf_exempt
def index (request):
    if request.method == 'POST':
        r = json.loads(request.body.decode())
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        first_name = r['message']['from']['first_name']
        if '/start' in message:
            send_message(chat_id, text=f'Здравствуйте,{first_name}! \nВас приветсвует бот компании АВТООТВЕТ!\nПройдите авторизацию использовав команду "/login №УНП" ')
        elif '/login' in message:
            unp=message.split(' ')
            login(chat_id,unp)
        elif '/unsubscribe' in message:
            unsubscribe(chat_id)
        elif '/subscribe' in message:
            subscribe(chat_id)
        else:
            send_message(chat_id, text='Я всего лишь бот и не знаю всех ответов =)')
        # write_json(r)
    return render(request,'home.html')