import requests
import json
from telegram.client import Telegram

# loading config
with open('config.json', 'r', encoding='utf8') as f:
	conf = json.load(f)

# log to PushMe bot
def pushme(msg):
    requests.post("http://pushmebot.ru/send", data={'key': conf['pushmekey'], 'message': msg})

pushme("Restarting worker...")

try:
    tg = Telegram(
        api_id=conf['auth']['id'],
        api_hash=conf['auth']['hash'],
        phone=conf['auth']['phone'],
        database_encryption_key=conf['auth']['database_key'])

    tg.login()
except Exception:
    pushme('Login ERROR(')
else:
    pushme('Login success!')

def new_message_handler(update):
    message_content = update['message']['content'].get('text', {})
    message_text = message_content.get('text', '').lower()
    if message_text == 'ping':
        chat_id = update['message']['chat_id']
        pushme(f'Received new message from {chat_id}')
        tg.send_message(chat_id=chat_id, text='pong')


tg.add_message_handler(new_message_handler)
pushme("Build OK!")
tg.idle()