from telethon.sync import TelegramClient
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import datetime
from setting import api_scrap_id, api_scrap_hash, phone_scrap_number, chats_name, answer_chat_id, black_list
import pandas as pd
from word_list import word_list


with TelegramClient(phone_scrap_number, api_scrap_id, api_scrap_hash) as client:
    date_start = datetime.date(datetime.date.today().year, 6, 6)
    list = []
    for chat_id in chats_name:
        # Получение сообщений из чата, начиная с начала текущего года
        try:
            messages = client.iter_messages(chat_id, offset_date=date_start, limit=2000)
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
                        read = True
                        data = message.date
                        for word in word_list:
                            if message_text.lower().find(word) != -1:
                                for name in black_list:
                                    try:
                                        if name == sender.username:
                                            read = False
                                    except:
                                        pass
                                if read is True:
                                    list.append([chat_link, (sender_link + '\n' + message_text), word, data])
                                    break
                    except Exception as ex:
                        print(ex)
        except Exception as ex:
            print(str(chat_id) + ' cant find message' + ' \n')
            print(ex)
    coll = ['Ссылка на телеграмм канал', 'Ссылка на человека, написавшего сообщение', 'Тригер', 'Дата']
    data = pd.DataFrame(data = list, columns=coll)
    data.to_excel('data.xlsx')
