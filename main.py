from telegram.client import Telegram
import requests

def log(msg):
    requests.post("http://pushmebot.ru/send", data={'key': '1a8a8768c2d7c7a674f3355c4a917dd8', 'message': msg})

tg = Telegram(
    api_id='846196',
    api_hash='8a83b26ce76d21f97851ac70329a9158',
    phone='+79649824012',
    database_encryption_key='randomkey'
)

tg.login()

log('login SUCCESS!')

def new_message_handler(update):
    message_content = update['message']['content'].get('text', {})
    message_text = message_content.get('text', '').lower()

    if message_text == 'ping':
        chat_id = update['message']['chat_id']
        log(f'Ping has been received from {chat_id}')
        tg.send_message(
            chat_id=chat_id,
            text='pong')

tg.add_message_handler(new_message_handler)
tg.idle()