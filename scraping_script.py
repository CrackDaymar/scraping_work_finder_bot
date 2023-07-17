from telethon.sync import TelegramClient
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import datetime
from setting import api_id, api_hash, phone_number, chats_name, answer_chat_id, black_list
import pandas as pd
from word_list import word_list


with TelegramClient(phone_number, api_id, api_hash) as client:
    date_start = datetime.date(datetime.date.today().year, 6, 6)
    list = []
    for chat_id in chats_name:
        # Получение сообщений из чата, начиная с начала текущего года
        messages = client.iter_messages(chat_id, offset_date=date_start)
        for message in messages:
            if message.from_id:
                try:
                    sender = client.get_entity(message.from_id)  # Получение информации об отправителе
                    sender_name = sender.first_name if hasattr(sender, 'first_name') else ''
                    sender_username = sender.username if hasattr(sender, 'username') else ''
                    message_text = message.text if message.text else ''

                    chat_entity = client.get_entity(chat_id)
                    chat_link = f"https://t.me/{chat_entity.username}"

                    # Получение ссылки на пользователя
                    sender_link = f"https://t.me/{sender_username}" if sender_username else ''

                    for word in word_list:
                        if message_text.lower().find(word) != -1:
                            list.append('Ссылка на телеграмм канал: ' + chat_link +
                                        '\nссылка на человека, написавшего сообщение' + sender_link + '\n' + message_text +
                                        '\nтригер'+word)
                            print('Ссылка на телеграмм канал: ' + chat_link +
                                        '\nссылка на человека, написавшего сообщение' + sender_link + '\n' + message_text +
                                        '\nтригер'+word)
                except Exception as ex:
                    print(ex)

    data = pd.DataFrame(list)
    data.to_excel('data.xlsx')

            # Здесь вы можете выполнять необходимую обработку сообщений и извлекать нужную информацию



    # Обработка и распарсинг сообщений
