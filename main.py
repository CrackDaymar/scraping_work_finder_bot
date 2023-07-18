from telethon.sync import TelegramClient
from telethon import events
from setting import api_bot_id, api_bot_hash, phone_bot_number, chats_name, answer_chat_id, black_list
from word_list import word_list

with TelegramClient(phone_bot_number, api_bot_id, api_bot_hash) as client:
    @client.on(events.NewMessage(chats=chats_name))
    async def handle_message(event):
        read = True
        chat = await event.get_chat()
        try:
            chat_link = f'https://t.me/{chat.username}'  # Ссылка на чат
        except:
            chat_link = 'error'
        user = await event.get_sender()
        try:
            user_link = f'https://t.me/{user.username}'
        except:
            user_link = 'error'
        check_user = await event.get_sender()
        for name in black_list:
            try:
                if name == check_user.username:
                    read = False
            except:
                pass
        for word in word_list:
            if event.message.text.lower().find(word) != -1 and read is True:
                message = event.message.text + " \n" + str(user_link) + " \n" + str(chat_link) + '\nссылка на сообщение: ' + \
                          '\n тригер фраза: ' + word
                await client.send_message(answer_chat_id, message)
                break
    client.run_until_disconnected()

