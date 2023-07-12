from telethon.sync import TelegramClient
from telethon import events
from setting import api_id, api_hash, phone_number, word_list


with TelegramClient(phone_number, api_id, api_hash) as client:
    # Получаем все сообщения из группы
    @client.on(events.NewMessage(chats=['itentre', 'kipr_it', 'dubai_it360', 'forum_sri_lanka', 'singapore_it',
                                        'people360_it', 'turkish_nomands', 'itgermania', 'thetechkzchat',
                                        'Dubai_Networkk', 'networkers_bali', 'BIZDXB24', 'biznesdvigusa',
                                        'businesss_chat', 'Bulgaria_network', 'DubaiChatik', 'dubai_biznesss',
                                        'coworking_in_dubai', 'dubaiexpert1', 'aiimxo', 'thetechkzchat', 'proect_x',
                                        'samarabusinesschat', 'Bizdecbiz', 'chat_predprinimateley', 'cyb2b',
                                        'cyprus_uslugi', 'jobcyprusonline', 'biznesky', 'dubyisk', 'bulgarianbussines',
                                        'uae_ads', 'business_chat_usa', 'top1businessusa', 'canadajobsnrentalservice',
                                        'PolandF', 'chat_predprin', 'biz_on_club', 'biznes_ispania',
                                        'Sofia_Bulgaria_business', 'servicio24', 'GirneTRSK', 'bisnes_chatt',
                                        'DubaiForum24', 'law_taxes', 'produckty', 'SPBSparta', 'dubaichatik1',
                                        'NFTCommunityUkraine', 'bizneshelpall_chat', 'joingroupforEntrepreneurs',
                                        'QQQFoundersDAO', 'Web3_Global', 'Web3CryptoClub', 'definityfifoundersgroup',
                                        'humansdao', 'web3foundersclub', 'Cryptofounder2122', 'ncider', 'rudubaichat',
                                        'ipgeorgiachat', 'business_club_experts', 'businesss_msk', 'businessmenclub',
                                        'Kipr_Go', 'investgroup_1', 'biznesgermany', 'biznesfrance', 'bisnes_chatt',
                                        'business_chat_ua', 'MIAMI_HELP', 'UAE_chat', 'ChatRussianDubai',
                                        'DotNetRuJobs', 'dubai_russng', 'rust_jobs', 'Phuketpar', 'kazannetwork',
                                        'ITgrants', 'antalya_go', 'UAbcGeo', 'gruzia_ip', 'ceoindigital',
                                        'BiznesKontakti', 'predprinimateli_kiev', 'trabajar_espana',
                                        'business_dubai_uae', 'biznesdvigmoskva', 'founders2founders', 'businesss_chat',
                                        'bussiness_georgia', 'ip_ge', 'Bizness_Bali', 'cyprus_uslugi', 'dubaika_ara',
                                        'busines_kzn', 'biznes4ru', 'ukrainian_business_europe', 'Thailand_Busines',
                                        'business_monopoly_dubai', 'dubai_netv', 'forum_sri_lanka', 'test12345koval']))
    async def handle_message(event):
        chat_id = -790083076
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
        if event.message.text.lower().find("ищу маркетинговое агентство") != -1:
            message = event.message.text + " \n" + user_link + " \n" + chat_link
            await client.send_message(chat_id, message)
        elif event.message.text.lower().find("ищу маркетолога") != -1:
            message = event.message.text + " \n" + user_link + " \n" + chat_link
            await client.send_message(chat_id, message)
        elif event.message.text.lower().find("маркетинговое агентство") != -1:
            message = event.message.text + " \n" + user_link + " \n" + chat_link
            await client.send_message(chat_id, message)
        # elif event.message.text.lower().find("заз") != -1:
        #     message = event.message.text + " \n" + user_link + " \n" + chat_link
        #     await client.send_message(chat_id, message)
    client.run_until_disconnected()

# bot = Bot(token='6349440490:AAFcDtT-fFh9h2JM9xNhxfDj-ANYvAHGqVI')
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
# logger.add('debug.log', format="{time} {level} {message}",
#            level='DEBUG', rotation="10KB", compression='zip')
#
#
# # Start
# @logger.catch()
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await bot.send_message(message.chat.id, "Hi")
#
#
# @dp.message_handler(commands=['my_id'])
# async def my_id(message: types.Message):
#     chat = message.chat.id
#     await bot.send_message(message.chat.id, chat)
#
#
# @dp.message_handler()
# async def text(message: types.Message):
#     if message.text.find("ищу маркетинговое агентство") != -1:
#         text = ('Текст сообщения: ' + str(message.text) + ' \nимя пользователя: ' + str(message.from_user.first_name) +
#             ' \nusername: ' + str(message.from_user.username) + ' \nИмя группы: ' + str(message.chat.username))
#         await bot.send_message(message.chat.id, text)
#     elif message.text.find("ищу маркетолога") != -1:
#         text = ('Текст сообщения: ' + str(message.text) + ' \nимя пользователя: ' + str(message.from_user.first_name) +
#                 ' \nusername: ' + str(message.from_user.username) + ' \nИмя группы: ' + str(message.chat.username))
#         await bot.send_message(message.chat.id, text)
#     elif message.text.find("маркетинговое агентство") != -1:
#         text = ('Текст сообщения: ' + str(message.text) + ' \nимя пользователя: ' + str(message.from_user.first_name) +
#             ' \nusername: ' + str(message.from_user.username) + ' \nИмя группы: ' + str(message.chat.username))
#         await bot.send_message(message.chat.id, text)
#
#
# @logger.catch(level="info")
# def main():
#     logger.info('Start')
#     executor.start_polling(dp, skip_updates=True)
#
#
# if __name__ == '__main__':
#     main()
