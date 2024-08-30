# -*- coding: utf-8 -*- 
import telebot
from telebot import types
from db import user,get_cashback, get_indicator,get_date, change_value_of_indicator, get_phone,check_chat_id, get_all_chat_id
from info_brands import name_brands, photo_brands, info_brands, uzb_info_brads
import schedule
import time

bot = telebot.TeleBot('7326806711:AAFGgOZnZUAncC7pNOC1WdV7F1txt7ZHKyU')

zayavka_chat_id = -4254884051
language = ''
id_message = ''

# start
@bot.message_handler(commands=['start'])
def start(message):
    
    global id_message
    markup = types.InlineKeyboardMarkup(row_width=2)
    Rus = types.InlineKeyboardButton(text='Rus🇷🇺', callback_data='Rus')
    Uzb = types.InlineKeyboardButton(text='Uzb🇺🇿', callback_data='Uzb')
    markup.add(Rus, Uzb)
    bot.send_message(message.chat.id, text='Выбирите язык 🇷🇺 \nTil tanlang 🇺🇿', reply_markup=markup)
    
    

# Из меню выбор язык
@bot.message_handler(commands=['language'])
def language(message):
   
    markup = types.InlineKeyboardMarkup(row_width=2)
    Rus = types.InlineKeyboardButton(text='Rus🇷🇺', callback_data='Rus')
    Uzb = types.InlineKeyboardButton(text='Uzb🇺🇿', callback_data='Uzb')
    markup.add(Rus, Uzb)
    bot.send_message(message.chat.id, text='Выбирите язык 🇷🇺 \nTil tanlang 🇺🇿', reply_markup=markup)
   

@bot.message_handler(commands=['info'])
def info(message):
    global language
    if language == 'Rus':
        bot.send_message(message.chat.id, text='С этого бота можно заказать замены масла!')
    elif language == 'Uzb':
        bot.send_message(message.chat.id, text='Ushbu bot orqali joyda moyalmashtrish arizasini qoldirish mumkin!')
    else:
        bot.send_message(message.chat.id, text="Вы еще не выбрали язык\n Siz til tanlamadingiz")
#  ------------главное меню бота--------------- 

@bot.message_handler(content_types=['contact'])
def contact(message):
    global language
    global id_message
    nomer = message.contact.phone_number
    get_nomer = nomer[-9:]
    take_nomer = '+998'+get_nomer 
    
    bot.delete_message(message.chat.id, message.message_id)
    
    if language == 'Rus':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keshback = types.InlineKeyboardButton(text='Кешбэк💰')
        catalog = types.InlineKeyboardButton(text='Каталог📂')
        last_change_oil = types.InlineKeyboardButton(text='Последняя дата замены масла📆')
        submit = types.InlineKeyboardButton(text='Оставить заявку📝')
        markup.add(keshback,catalog)
        markup.add(last_change_oil)
        markup.add(submit)
        bot.send_message(message.chat.id, text=f'Вы прошли регистрацию ✅', reply_markup=markup)
        user(message.chat.id, message.contact.first_name, take_nomer)

    elif language == 'Uzb':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keshback = types.InlineKeyboardButton(text='Keshbek💰')
        catalog = types.InlineKeyboardButton(text='Katalog📂')
        last_change_oil = types.InlineKeyboardButton(text='Oxirgi moy almashtirilgan sana📆')
        submit = types.InlineKeyboardButton(text='Ariza qoldirish📝')
        markup.add(keshback,catalog)
        markup.add(last_change_oil)
        markup.add(submit)
        bot.send_message(message.chat.id, text=f'Ro\'yxatdan o\'tdingiz✅', reply_markup=markup)
        user(message.chat.id, message.contact.first_name, take_nomer)
#------------конец главной меню ------------------------- 

# Начало заявки
@bot.message_handler(content_types=['text'])
def text(message):

#    на русском кэшбек
    if message.text =='Кешбэк💰':
        cashback = get_cashback(message.chat.id)
        bot.send_message(message.chat.id, text=f'Уважаемый {message.from_user.first_name} ваш кэшбэк равен {cashback} сум!')

#  на узбекском кэшбек
    elif message.text == 'Keshbek💰':
        cashback = get_cashback(message.chat.id)
        bot.send_message(message.chat.id, text=f'Xurmatli {message.from_user.first_name} sizning keshbekingiz {cashback} so\'mga teng!')

#  на русском 
    elif message.text == 'Оставить заявку📝':
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_geo = types.KeyboardButton(text="Отправить местоположение📍", request_location=True)
        keyboard.add(button_geo)
        bot.send_message(message.chat.id, "Поделитесь местоположением!", reply_markup=keyboard)

# на узбекском 
    elif message.text == 'Ariza qoldirish📝':
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_geo = types.KeyboardButton(text="Lokaciya blan bo\'lishish📍", request_location=True)
        keyboard.add(button_geo)
        bot.send_message(message.chat.id, "Arizangiz ko\'ribchiqilishi uchu lokaciyangiz blan bo\'lishing!", reply_markup=keyboard)

# последняя дата замены даты на русском 
    elif message.text == 'Последняя дата замены масла📆':
        date = get_date(message.chat.id)
        indicator = get_indicator(message.chat.id)
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_date = types.InlineKeyboardButton(text='🔄Обновить')
        btn_back = types.InlineKeyboardButton(text='🔙Назад')
        keyboard.add(button_date,btn_back)
        bot.send_message(message.chat.id, text=f'Показатели \nИндикатор : {indicator} \nДата : {date}', reply_markup=keyboard)

# на узбекском
    elif message.text =='Oxirgi moy almashtirilgan sana📆':
        date = get_date(message.chat.id)
        indicator = get_indicator(message.chat.id)
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_date = types.InlineKeyboardButton(text='🔄Yagilash')
        btn_back = types.InlineKeyboardButton(text='🔙Orqaga')
        keyboard.add(button_date,btn_back)
        bot.send_message(message.chat.id, text=f'Ko\'rsatgichlar \nIndikator : {indicator} \nSana : {date}', reply_markup=keyboard)
      
# ------------------обновлене  индикатора ----------------------
#   на русском
    elif message.text =='🔄Обновить':
        
        bot.send_message(message.chat.id, text='Отправьте значение индикатора')        
        @bot.message_handler(content_types=['text'])
        def save(message):
            global text 
            text = message.text
            try:
                float(text)
                change_value_of_indicator(message.chat.id, text)
                bot.send_message(message.chat.id, text='Записан')
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                keshback = types.InlineKeyboardButton(text='Кешбэк💰')
                catalog = types.InlineKeyboardButton(text='Каталог📂')
                last_change_oil = types.InlineKeyboardButton(text='Последняя дата замены масла📆')
                submit = types.InlineKeyboardButton(text='Оставить заявку📝')
                markup.add(keshback,catalog)
                markup.add(last_change_oil)
                markup.add(submit)
                bot.send_message(message.chat.id, text=f'Главное меню', reply_markup=markup)
            except ValueError:
                bot.send_message(message.chat.id, text='Вы ввели не правильное знаечение, если хотите все же добавить нажмите на кнопку ОБНОВИТЬ и введите цыфры а не буквы!')
              
        bot.register_next_step_handler(message, save)    

#  на узбекском
    elif message.text =='🔄Yngilash':
        bot.send_message(message.chat.id, text = 'Boshqaruv panelidagi INDIKATOR qiymatini kiriting')
        @bot.message_handler(content_types=['text'])
        def save(message):
            global text 
            text = message.text
            try:
                float(text)
                change_value_of_indicator(message.chat.id, text)
                bot.send_message(message.chat.id, text='Muvaffaqiyatli yozib olindi!')
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                keshback = types.InlineKeyboardButton(text='Keshbek💰')
                catalog = types.InlineKeyboardButton(text='Katalog📂')
                last_change_oil = types.InlineKeyboardButton(text='Oxirgi moy almashtirilgan sana📆')
                submit = types.InlineKeyboardButton(text='Ariza qoldirish📝')
                markup.add(keshback,catalog)
                markup.add(last_change_oil)
                markup.add(submit)
                bot.send_message(message.chat.id, text=f'Bosh menyu', reply_markup=markup)
            except ValueError:
                bot.send_message(message.chat.id, text='Siz noto\'g\'ri qiymat kiritdingiz, agar siz hali ham qo\'shmoqchi bo\'lsangiz, Yangilash tugmasini bosing va harflarni emas, raqamlarni kiriting!')
              
        bot.register_next_step_handler(message, save)


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
    index = check_chat_id(call.message.chat.id)
    
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
