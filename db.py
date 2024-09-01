from datetime import date
import sqlite3


def user(chat_id,name, phone_number):
    
    cursor = None
    conn = None
    # Подключение к базе данных
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="khakimo1_id_rsa",
    #     password="Parol_100",
    #     database="khakimo1_date_base"
    # )
    conn = sqlite3.connect('bd.db')
    cursor = conn.cursor()

    # Проверка наличия таблицы и создание её при необходимости
    cursor.execute("SHOW TABLES LIKE 'user'")
    data = cursor.fetchone()
    
    if data is None:  # Если таблица не существует
        cursor.execute('''
            CREATE TABLE user (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                chat_id INTEGER,
                name TEXT,
                phone_number TEXT,
                indicator INTEGER DEFAULT 0,
                cashback INTEGER DEFAULT 0,
                date DATE
            )
        ''')
    
    else:
        cursor.execute("INSERT INTO user(chat_id,name,phone_number,indicator,cashback,date) VALUES (?, ?, ?, ?, ?, ?)",(chat_id,name,phone_number,'0','0',date.today()))
        

# Закрытие соединения
    conn.commit()
    cursor.close()
    conn.close()

def get_cashback(value):
    cursor = None
    conn = None
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="khakimo1_id_rsa",
    #     password="Parol_100",
    #     database="khakimo1_date_base"
    # )
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()
    cursor.execute(f'SELECT cashback FROM user WHERE chat_id = \'{value}\'')
 
    data = cursor.fetchone()[0]
    conn.commit()
    conn.close()

    return data

def get_indicator(value):
    cursor = None
    conn = None
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="khakimo1_id_rsa",
    #     password="Parol_100",
    #     database="khakimo1_date_base"
    # )
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()
    cursor.execute(f'SELECT indicator FROM user WHERE chat_id = \'{value}\'')
 
    data = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return data

def get_date(value):
    cursor = None
    conn = None
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="khakimo1_id_rsa",
    #     password="Parol_100",
    #     database="khakimo1_date_base"
    # )
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()
    cursor.execute(f'SELECT date FROM user WHERE chat_id = \'{value}\'')
 
    data = cursor.fetchone()[0]
    conn.commit()
    conn.close()

    return data

def change_value_of_indicator(chat_id,value):

    cursor = None
    conn = None
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="khakimo1_id_rsa",
    #     password="Parol_100",
    #     database="khakimo1_date_base"
    # )
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()

    cursor.execute(f'UPDATE user SET indicator = \'{value}\', date = \'{date.today()}\' WHERE chat_id = \'{chat_id}\'')
    conn.commit()
    conn.close()

def get_phone(value):
    cursor = None
    conn = None
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="khakimo1_id_rsa",
    #     password="Parol_100",
    #     database="khakimo1_date_base"
    # )
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()
    cursor.execute(f'SELECT phone_number FROM user WHERE chat_id = \'{value}\'')
 
    data = cursor.fetchone()[0]
    conn.commit()
    conn.close()

    return data

def get_chat_id(value):
    cursor = None
    conn = None
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="khakimo1_id_rsa",
    #     password="Parol_100",
    #     database="khakimo1_date_base"
    # )
    conn = sqlite3.connect('bd.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT chat_id FROM user WHERE phone_number = \'{value}\'')
 
    data = cursor.fetchone()[0]
    print(data)
    conn.commit()
    conn.close()

    return data

def take_cash(phone_number, sum):
    cursor = None
    conn = None
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="khakimo1_id_rsa",
    #     password="Parol_100",
    #     database="khakimo1_date_base"
    # )
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()
    update_query = f"""UPDATE user SET cashback = ?, date = ?  WHERE phone_number = ?"""

    cursor.execute(update_query,(sum, date.today(), phone_number))
    conn.commit()
    conn.close()

def get_cash_from_number(phone_number):
    cursor = None
    conn = None
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="khakimo1_id_rsa",
    #     password="Parol_100",
    #     database="khakimo1_date_base"
    # )
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()
    cursor.execute(f'SELECT cashback FROM user WHERE phone_number =\'{phone_number}\'')
    
    date = cursor.fetchone()[0]
    
    conn.commit()
    conn.close()
    return date

def get_all_user():

    cursor = None
    conn = None
    conn = sqlite3.connect.connect(
        host="localhost",
        user="khakimo1_id_rsa",
        password="Parol_100",
        database="khakimo1_date_base"
    )

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user')

    date = cursor.fetchall()
    
    conn.commit()
    conn.close()
    return date

def check_chat_id(chat_id):

    # Подключение к базе данных MySQL
    cursor = None
    conn = None
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="khakimo1_id_rsa",
    #     password="Parol_100",
    #     database="khakimo1_date_base"
    # )
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()

    # Запрос для проверки наличия chat_id
    cursor.execute("SELECT COUNT(*) FROM user WHERE chat_id = ?", (chat_id,))

    # Получение результата
    result = cursor.fetchone()

    if result[0] > 0:
        return 1  # Если запись найдена
    else:
        return 0  # Если запись не найдена

    conn.commit()
    conn.close()
   
def get_all_chat_id():
    cursor = None
    conn = None
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="khakimo1_id_rsa",
    #     password="Parol_100",
    #     database="khakimo1_date_base"
    # )
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()

    cursor.execute('SELECT chat_id FROM user')

    date = cursor.fetchall()
    
    conn.commit()
    conn.close()
    
    return date