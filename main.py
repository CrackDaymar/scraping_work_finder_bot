from telethon.sync import TelegramClient
from telethon import events
from setting import api_id, api_hash, phone_number, word_list, chats_name, answer_chat_id


with TelegramClient(phone_number, api_id, api_hash) as client:
    @client.on(events.NewMessage(chats=chats_name))
    async def handle_message(event):
        try:
            chat = await event.get_chat()
            chat_link = f'https://t.me/{chat.username}'  # Ссылка на чат
        except:
            chat_link = 'error'
        try:
            user = await event.get_sender()
            user_link = f'https://t.me/{user.username}'
        except:
            user_link = 'error'
        for word in word_list:
            if event.message.text.lower().find(word) != -1:
                message = event.message.text + " \n" + user_link + " \n" + chat_link
                await client.send_message(answer_chat_id, message)
                break
    client.run_until_disconnected()

