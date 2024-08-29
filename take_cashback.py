import telebot 
from telebot import types
from db import take_cash, get_cash_from_number

bot = telebot.TeleBot('7376982557:AAG3oDY7FbREAvbKd8e2O9qC43V_SlS5Bmo')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    enter = types.InlineKeyboardButton(text='Вход')
    info = types.InlineKeyboardButton(text='Информация')
    markup.add(enter,info)
    bot.send_message(message.chat.id, text='Добро пожаловать на Besh Express Worker', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text(message): 
#Вход 
    if message.text == 'Вход':
        bot.send_message(message.chat.id, text='введите пароль пользователя')
        @bot.message_handler(content_types=['text'])
        def get_pass(message):
            global password
            password = message.text
            bot.delete_message(message.chat.id, message.message_id)
            try:
                float(password)
                if password == '2211':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    take_cashback = types.InlineKeyboardButton(text='Выдать кешбэк')
                    get_cashback = types.InlineKeyboardButton(text='Списать Кешбэк')
                    exit = types.InlineKeyboardButton(text='Выход')
                    markup.add(take_cashback,get_cashback)
                    markup.add(exit)
                    bot.send_message(message.chat.id, text='Правильный пароль', reply_markup=markup)
                else:
                    bot.send_message(message.chat.id, text='ввели не правильный пароль')
            except ValueError:
                bot.send_message(message.chat.id, text='ввели не правильный пароль') 
        bot.register_next_step_handler(message, get_pass)

#Выдача кешбэка     
    elif message.text == 'Выдать кешбэк':
        bot.send_message(message.chat.id, text='Введите номер телефона и сумму через пробел!')
        @bot.message_handler(content_types=['text'])
        def text(message):
            
            try:
                
                global text 
                text = str(message.text)
                word = text.split()
                number = str(word[0])
                sum = str((int(word[1]) // 100) + (int(get_cash_from_number(number)))  ) 
                take_cash(number, sum)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                take_cashback = types.InlineKeyboardButton(text='Выдать кешбэк')
                get_cashback = types.InlineKeyboardButton(text='Списать Кешбэк')
                exit = types.InlineKeyboardButton(text='Выход')
                markup.add(take_cashback,get_cashback)
                markup.add(exit)
                bot.send_message(message.chat.id, text='Кешбэк выдан')
            except ValueError:
                bot.send_message(message.chat.id, text='Ввели не правильно ')
        bot.register_next_step_handler(message, text)

#Списание кешбэка 
    elif message.text == 'Списать Кешбэк':
        bot.send_message(message.chat.id, text='Введите номер телефона и сумму для снятие через пробел')
        @bot.message_handler(content_types=['text'])
        def text(message):
            try:
                global tex 
                tex = str(message.text)
                num_and_sum = tex.split()
                num = str(num_and_sum[0])
                sum = int(num_and_sum[1])
                cash = int(get_cash_from_number(num))
                if cash >= sum:
                    cash = sum - cash
                    take_cash(num, cash)
                    bot.send_message(message.chat.id, text='Кешбэк был списан') 
                elif cash < sum:
                    bot.send_message(message.chat.id, text='Вы не сможите снять такую сумму так как она привышает суммы имеющийся!')
                else:
                    bot.send_message(message.chat.id, text='Не правильно ввели чтоб повторить повторно нажмите списать кешбэк')
            except ValueError:
                bot.send_message(message.chat.id, text="Ввели не правильные значение")
        bot.register_next_step_handler(message, text)

#Выход 
    elif message.text == 'Выход':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        enter = types.InlineKeyboardButton(text='Вход')
        info = types.InlineKeyboardButton(text='Информация')
        markup.add(enter,info)
        bot.send_message(message.chat.id, text='Выход', reply_markup=markup) 





if __name__ == '__main__':
    bot.polling(non_stop=True)