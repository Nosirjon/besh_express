import telebot
<<<<<<< HEAD
from telebot import types
from db import user,get_cashback, get_indicator,get_date, change_value_of_indicator, get_phone,check_chat_id, get_all_chat_id
from info_brands import name_brands, photo_brands, info_brands, uzb_info_brads
import schedule
import time
=======
>>>>>>> b24668d2292b15d4b1c78d68a610dc545e3dbdf3

bot = telebot.TeleBot('6992564836:AAHWId4lFuR0N0iImdIMcJ9VG7RFFdMvjFw')


@bot.meesage_handler(comands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='Бот работает')


<<<<<<< HEAD
#  кнопка назад на русском 
    elif message.text =='🔙Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keshback = types.InlineKeyboardButton(text='Кешбэк💰')
        catalog = types.InlineKeyboardButton(text='Каталог📂')
        last_change_oil = types.InlineKeyboardButton(text='Последняя дата замены масла📆')
        submit = types.InlineKeyboardButton(text='Оставить заявку📝')
        markup.add(keshback,catalog)
        markup.add(last_change_oil)
        markup.add(submit)
        bot.send_message(message.chat.id, text=f'Главное меню', reply_markup=markup)

# на узбекском
    elif message.text == '🔙Orqaga':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keshback = types.InlineKeyboardButton(text='Keshbek💰')
        catalog = types.InlineKeyboardButton(text='Katalog📂')
        last_change_oil = types.InlineKeyboardButton(text='Oxirgi moy almashtrilgan sana📆')
        submit = types.InlineKeyboardButton(text='Ariza qoldirish📝')
        markup.add(keshback,catalog)
        markup.add(last_change_oil)
        markup.add(submit)
        bot.send_message(message.chat.id, text=f'Bosh menyu', reply_markup=markup)


    elif message.text =='Каталог📂':
        markup = types.InlineKeyboardMarkup(row_width=5)
        button = (types.InlineKeyboardButton(text=x, callback_data=x) for x in name_brands)
        markup.add(*button)
        bot.send_message(message.chat.id, text='Каталог брендов', reply_markup=markup)
                       

    elif message.text == 'Katalog📂':
        markup = types.InlineKeyboardMarkup(row_width=5)
        button = (types.InlineKeyboardButton(text=x, callback_data=x) for x in name_brands)
        markup.add(*button)
        bot.send_message(message.chat.id, text='Brendlar katalogi', reply_markup=markup)

    #  отвечает если нет такой команды
    else:
        bot.send_message(message.chat.id, text='Вы ввели не правильную команду!')
    

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    
    global language
    id = call.message.chat.id
    index = check_chat_id(id)
    
    id_message = call.message.message_id 
    
    # тут идет проверка есть ли катой пользователь если есть то ему не стоит выводить кнопку поделитесь контактом 
    
    if call.data =='Rus' and index == 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keshback = types.InlineKeyboardButton(text='Кешбэк💰')
        catalog = types.InlineKeyboardButton(text='Каталог📂')
        last_change_oil = types.InlineKeyboardButton(text='Последняя дата замены масла📆')
        submit = types.InlineKeyboardButton(text='Оставить заявку📝')
        markup.add(keshback,catalog)
        markup.add(last_change_oil)
        markup.add(submit)
        bot.send_message(call.message.chat.id, text=f'Главное меню!', reply_markup=markup)
        bot.delete_message(call.message.chat.id, id_message)

    elif call.data == 'Rus' and index == 0:    
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        mar = types.KeyboardButton(text='Поделиться контактом 📰', request_contact=True)
        markup.add(mar)
        bot.send_message(call.message.chat.id, text='Добро пожаловать на наш бот!\nДля продолжение вам необходимо поделить контактом!', reply_markup=markup)
        language = 'Rus'
        bot.delete_message(call.message.chat.id, id_message)
    
    elif call.data == 'Uzb' and index == 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keshback = types.InlineKeyboardButton(text='Keshbek💰')
        catalog = types.InlineKeyboardButton(text='Katalog📂')
        last_change_oil = types.InlineKeyboardButton(text='Oxirgi moy almashtirilgan sana📆')
        submit = types.InlineKeyboardButton(text='Ariza qoldirish📝')
        markup.add(keshback,catalog)
        markup.add(last_change_oil)
        markup.add(submit)
        bot.send_message(call.message.chat.id, text=f'Bosh menyu!', reply_markup=markup)
        bot.delete_message(call.message.chat.id, id_message)  
    
    elif call.data == 'Uzb' and index == 0:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        mar = types.KeyboardButton(text='Kontaktizblan bo\'lishing 📰', request_contact=True)
        markup.add(mar)
        bot.send_message(call.message.chat.id, text='Assalomu alaykum telegram botimizga xush kelibsiz\nDavom etish uchun kontaktiz blan bo\'lishing', reply_markup=markup)
        language ='Uzb'
        bot.delete_message(call.message.chat.id, id_message)


# --------------GULF -----------------------------
    # На русском
    elif call.data == 'Gulf' and language == 'Rus':  
        markup = types.InlineKeyboardMarkup()
        with open(photo_brands[0], 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo)
        btn = types.InlineKeyboardButton(text='Уточнить цену', callback_data='Price_Gulf')
        markup.add(btn)    
        bot.send_message(call.message.chat.id, text=info_brands[0], reply_markup=markup)
   
    elif call.data == 'Price_Gulf' and language == 'Rus':
        bot.send_message(call.message.chat.id, text='В скором времени будет установлена цена!')

    # На узбекском
    elif call.data == 'Gulf' and language == 'Uzb':
        markup = types.InlineKeyboardMarkup()
        with open(photo_brands[0], 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo)
        btn = types.InlineKeyboardButton(text='Narx aniqlash', callback_data='Price_Gulf')
        markup.add(btn)    
        bot.send_message(call.message.chat.id, text=uzb_info_brads[0], reply_markup=markup)
    
    elif call.data == 'Price_Gulf' and language == 'Uzb':
        bot.send_message(call.message.chat.id, text='Yaqin orada narx qoyiladi!')



# -----------------LUKOIL--------------------------------------------
    elif call.data == 'Lukoil' and language == 'Rus':
        markup = types.InlineKeyboardMarkup()
        with open(photo_brands[1], 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo)
        btn = types.InlineKeyboardButton(text='Уточнить цену', callback_data='Price_Lukoil')
        markup.add(btn)    
        bot.send_message(call.message.chat.id, text=info_brands[1], reply_markup=markup)
    elif call.data == 'Price_Lukoil' and language == 'Rus':
        bot.send_message(call.message.chat.id, text='В скором времени будет установлена цена!')

    # На узбекском
    elif call.data == 'Lukoil' and language == 'Uzb':
        markup = types.InlineKeyboardMarkup()
        with open(photo_brands[1], 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo)
        btn = types.InlineKeyboardButton(text='Narx aniqlash', callback_data='Price_Lukoil')
        markup.add(btn)    
        bot.send_message(call.message.chat.id, text=uzb_info_brads[1], reply_markup=markup)
    elif call.data == 'Price_Lukoil' and language == 'Uzb':
        bot.send_message(call.message.chat.id, text='Yaqin orada narx qoyiladi!')

# -----------------MOBIL---------------------------------------------------------
    elif call.data == 'Mobil' and language == 'Rus':
        markup = types.InlineKeyboardMarkup()
        with open(photo_brands[2], 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo)
        btn = types.InlineKeyboardButton(text='Уточнить цену', callback_data='Price_Mobil')
        markup.add(btn)    
        bot.send_message(call.message.chat.id, text=info_brands[2], reply_markup=markup)
    
    elif call.data == 'Price_Mobil' and language == 'Rus':
        bot.send_message(call.message.chat.id, text='В скором времени будет установлена цена!')

    # На узбекском
    elif call.data == 'Mobil' and language == 'Uzb':
        markup = types.InlineKeyboardMarkup()
        with open(photo_brands[2], 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo)
        btn = types.InlineKeyboardButton(text='Narx aniqlash', callback_data='Price_Mobil')
        markup.add(btn)    
        bot.send_message(call.message.chat.id, text=uzb_info_brads[2], reply_markup=markup)
    elif call.data == 'Price_Mobil' and language == 'Uzb':
        bot.send_message(call.message.chat.id, text='Yaqin orada narx qoyiladi!')


# -------------------SHELL--------------------------------------------------------------
    elif call.data == 'Shell' and language == 'Rus':
        markup = types.InlineKeyboardMarkup()
        with open(photo_brands[3], 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo)
        btn = types.InlineKeyboardButton(text='Уточнить цену', callback_data='Price_Shell')
        markup.add(btn)    
        bot.send_message(call.message.chat.id, text=info_brands[3], reply_markup=markup)
    elif call.data == 'Price_Shell' and language == 'Rus':
        bot.send_message(call.message.chat.id, text='В скором времени будет установлена цена!')

    # На узбекском
    elif call.data == 'Shell' and language == 'Uzb':
        markup = types.InlineKeyboardMarkup()
        with open(photo_brands[3], 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo)
        btn = types.InlineKeyboardButton(text='Narx aniqlash', callback_data='Price_Shell')
        markup.add(btn)    
        bot.send_message(call.message.chat.id, text=uzb_info_brads[3], reply_markup=markup)
    elif call.data == 'Price_Shell' and language == 'Uzb':
        bot.send_message(call.message.chat.id, text='Yaqin orada narx qoyiladi!')

# ------------------TATNEFT--------------------------------------
    elif call.data == 'Tatneft' and language == 'Rus':
        markup = types.InlineKeyboardMarkup()
        with open(photo_brands[4], 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo)
        btn = types.InlineKeyboardButton(text='Уточнить цену', callback_data='Price_Tatneft')
        markup.add(btn)    
        bot.send_message(call.message.chat.id, text=info_brands[4], reply_markup=markup)
    elif call.data == 'Price_Tatneft' and language == 'Rus':
        bot.send_message(call.message.chat.id, text='В скором времени будет установлена цена!')

    # На узбекском
    elif call.data == 'Tatneft' and language == 'Uzb':
        markup = types.InlineKeyboardMarkup()
        with open(photo_brands[4], 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo)
        btn = types.InlineKeyboardButton(text='Narx aniqlash', callback_data='Price_Tatneft')
        markup.add(btn)    
        bot.send_message(call.message.chat.id, text=uzb_info_brads[4], reply_markup=markup)
    elif call.data == 'Price_Tatneft' and language == 'Uzb':
        bot.send_message(call.message.chat.id, text='Yaqin orada narx qoyiladi!')


# если получить геолокациюs
@bot.message_handler(content_types=['location'])
def location (message):
    global language
#     на русском
    if message.location is not None and language == 'Rus':
        bot.send_message(zayavka_chat_id, text=f'У вас есть новый заказ\n Имя : {message.from_user.first_name}\n Номер телефона : +{get_phone(message.chat.id)}')
        bot.send_location(zayavka_chat_id, latitude=message.location.latitude, longitude=message.location.longitude)
        bot.send_message(message.chat.id, text='Заявка успешно отправлена, в скором времении с вами свяжутся ')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keshback = types.InlineKeyboardButton(text='Кешбэк💰')
        catalog = types.InlineKeyboardButton(text='Каталог📂')
        last_change_oil = types.InlineKeyboardButton(text='Последняя дата замены масла📆')
        submit = types.InlineKeyboardButton(text='Оставить заявку📝')
        markup.add(keshback,catalog)
        markup.add(last_change_oil)
        markup.add(submit)
        bot.send_message(message.chat.id, text=f'Главное меню', reply_markup=markup)
    
#На узбекском
    elif message.location is not None and language == 'Uzb':
        bot.send_message(zayavka_chat_id, text=f'У вас есть новый заказ\n Имя : {message.from_user.first_name}\n Номер телефона : +{get_phone(message.chat.id)}')
        bot.send_location(zayavka_chat_id, latitude=message.location.latitude, longitude=message.location.longitude)
        bot.send_message(message.chat.id, text='Ariza muvaffaqiyatli yuborildi, tez orada siz bilan bog\'lanasiz')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keshback = types.InlineKeyboardButton(text='Keshbek💰')
        catalog = types.InlineKeyboardButton(text='Katalog📂')
        last_change_oil = types.InlineKeyboardButton(text='Oxirgi moy almashtirilgan sana📆')
        submit = types.InlineKeyboardButton(text='Ariza qoldirish📝')
        markup.add(keshback,catalog)
        markup.add(last_change_oil)
        markup.add(submit)
        bot.send_message(message.chat.id, text=f'Bosh menyu', reply_markup=markup)



# def send_message():
#         for i in get_all_chat_id():
#             of = i[0]
#             bot.send_photo(f'{of}', photo=open('1.jpg','rb'))
#             bot.send_message(f'{of}', text='Assalomu Aleykum azizlar, muqaddas Juma ayyomi muborak bo\'lsin!')        

if __name__ =='__main__': 
    
    # schedule.every().friday.at('09:00').do(send_message)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    bot.polling(non_stop=True)
=======
bot.polling(none_stop=True)
>>>>>>> b24668d2292b15d4b1c78d68a610dc545e3dbdf3
