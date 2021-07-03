import requests
from avtootvet import settings
import json


URL = f'https://api.telegram.org/bot{settings.TOKEN}/'

def write_json(data, filename = 'answer.json'):
    with open(f'static/{filename}', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    # write_json(r.json())
    return r.json()

def send_message(chat_id, text='bla-bla-bla'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text':text}
    r = requests.post(url, json=answer)
    return r.json()

def main ():
    r = requests.get(URL + 'getMe')
    write_json(r.json())

# main()
# r = get_updates()
# chat_id = r['result'][-1]['message']['chat']['id']
# send_message(chat_id)


# https://api.telegram.org/bot1814873441:AAEsaxbtbW7M0VxHMm9b2r77z5-7Xoaa7e4/setWebhook?url=https://f29429491c5f.ngrok.io
# https://api.telegram.org/bot1814873441:AAEsaxbtbW7M0VxHMm9b2r77z5-7Xoaa7e4/deleteWebhook