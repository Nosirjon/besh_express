
from datetime import date
import sqlite3
import mysql.connector 


def user(chat_id,name, phone_number):
    
    cursor = None
    conn = None
    # Подключение к базе данных
    conn = mysql.connector.connect(
        username = 'doadmin'
        password = 'AVNS_VSLcWQ0vFSrPTS7QO88'
        host = 'private-db-mysql-nyc3-12595-do-user-16381338-0.k.db.ondigitalocean.com'
        port = '25060'
        database = 'defaultdb'
        sslmode = 'REQUIRED'
        
    )

    cursor = conn.cursor()

    # Проверка наличия таблицы и создание её при необходимости
    cursor.execute("SHOW TABLES LIKE 'bot_express'")
    data = cursor.fetchone()
    
    if data is None:  # Если таблица не существует
        cursor.execute('''
            CREATE TABLE bot_express (
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
        cursor.execute("INSERT INTO bot_express(chat_id,name,phone_number,indicator,cashback,date) VALUES (%s, %s, %s, %s, %s, %s)",(chat_id,name,phone_number,'0','0',date.today()))
        

# Закрытие соединения
    conn.commit()
    cursor.close()
    conn.close()

def get_cashback(value):
    cursor = None
    conn = None
    conn = mysql.connector.connect(
        username = 'doadmin'
        password = 'AVNS_VSLcWQ0vFSrPTS7QO88'
        host = 'private-db-mysql-nyc3-12595-do-user-16381338-0.k.db.ondigitalocean.com'
        port = '25060'
        database = 'defaultdb'
        sslmode = 'REQUIRED'
        
    )

    cursor = conn.cursor()
    cursor.execute(f'SELECT cashback FROM bot_express WHERE chat_id = \'{value}\'')
 
    data = cursor.fetchone()[0]
    conn.commit()
    conn.close()

    return data

def get_indicator(value):
    cursor = None
    conn = None
    conn = mysql.connector.connect(
        username = 'doadmin'
        password = 'AVNS_VSLcWQ0vFSrPTS7QO88'
        host = 'private-db-mysql-nyc3-12595-do-user-16381338-0.k.db.ondigitalocean.com'
        port = '25060'
        database = 'defaultdb'
        sslmode = 'REQUIRED'
        
    )

    cursor = conn.cursor()
    cursor.execute(f'SELECT indicator FROM bot_express WHERE chat_id = \'{value}\'')
 
    data = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return data

def get_date(value):
    cursor = None
    conn = None
    conn = mysql.connector.connect(
        username = 'doadmin'
        password = 'AVNS_VSLcWQ0vFSrPTS7QO88'
        host = 'private-db-mysql-nyc3-12595-do-user-16381338-0.k.db.ondigitalocean.com'
        port = '25060'
        database = 'defaultdb'
        sslmode = 'REQUIRED'
        
    )

    cursor = conn.cursor()
    cursor.execute(f'SELECT date FROM bot_express WHERE chat_id = \'{value}\'')
 
    data = cursor.fetchone()[0]
    conn.commit()
    conn.close()

    return data

def change_value_of_indicator(chat_id,value):

    cursor = None
    conn = None
    conn = mysql.connector.connect(
        username = 'doadmin'
        password = 'AVNS_VSLcWQ0vFSrPTS7QO88'
        host = 'private-db-mysql-nyc3-12595-do-user-16381338-0.k.db.ondigitalocean.com'
        port = '25060'
        database = 'defaultdb'
        sslmode = 'REQUIRED'
        
    )

    cursor = conn.cursor()

    cursor.execute(f'UPDATE bot_express SET indicator = \'{value}\', date = \'{date.today()}\' WHERE chat_id = \'{chat_id}\'')
    conn.commit()
    conn.close()

def get_phone(value):
    cursor = None
    conn = None
    conn = mysql.connector.connect(
        username = 'doadmin'
        password = 'AVNS_VSLcWQ0vFSrPTS7QO88'
        host = 'private-db-mysql-nyc3-12595-do-user-16381338-0.k.db.ondigitalocean.com'
        port = '25060'
        database = 'defaultdb'
        sslmode = 'REQUIRED'
        
    )

    cursor = conn.cursor()
    cursor.execute(f'SELECT phone_number FROM bot_express WHERE chat_id = \'{value}\'')
 
    data = cursor.fetchone()[0]
    conn.commit()
    conn.close()

    return data

def get_chat_id(value):
    cursor = None
    conn = None
    conn = mysql.connector.connect(
        username = 'doadmin'
        password = 'AVNS_VSLcWQ0vFSrPTS7QO88'
        host = 'private-db-mysql-nyc3-12595-do-user-16381338-0.k.db.ondigitalocean.com'
        port = '25060'
        database = 'defaultdb'
        sslmode = 'REQUIRED'
        
    )

    cursor = conn.cursor()
    cursor.execute(f'SELECT chat_id FROM bot_express WHERE phone_number = \'{value}\'')
 
    data = cursor.fetchone()[0]
    print(data)
    conn.commit()
    conn.close()

    return data

def take_cash(phone_number, sum):
    cursor = None
    conn = None
    conn = mysql.connector.connect(
        username = 'doadmin'
        password = 'AVNS_VSLcWQ0vFSrPTS7QO88'
        host = 'private-db-mysql-nyc3-12595-do-user-16381338-0.k.db.ondigitalocean.com'
        port = '25060'
        database = 'defaultdb'
        sslmode = 'REQUIRED'
        
    )

    cursor = conn.cursor()
    update_query = f"""UPDATE bot_express SET cashback = ?, date = ?  WHERE phone_number = ?"""

    cursor.execute(update_query,(sum, date.today(), phone_number))
    conn.commit()
    conn.close()

def get_cash_from_number(phone_number):
    cursor = None
    conn = None
    conn = mysql.connector.connect(
        username = 'doadmin'
        password = 'AVNS_VSLcWQ0vFSrPTS7QO88'
        host = 'private-db-mysql-nyc3-12595-do-user-16381338-0.k.db.ondigitalocean.com'
        port = '25060'
        database = 'defaultdb'
        sslmode = 'REQUIRED'
        
    )

    cursor = conn.cursor()
    cursor.execute(f'SELECT cashback FROM bot_express WHERE phone_number =\'{phone_number}\'')
    
    date = cursor.fetchone()[0]
    
    conn.commit()
    conn.close()
    return date

def get_all_user():

    cursor = None
    conn = None
    conn = mysql.connector.connect(
        username = 'doadmin'
        password = 'AVNS_VSLcWQ0vFSrPTS7QO88'
        host = 'private-db-mysql-nyc3-12595-do-user-16381338-0.k.db.ondigitalocean.com'
        port = '25060'
        database = 'defaultdb'
        sslmode = 'REQUIRED'
        
    )

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user')

    date = cursor.fetchall()
    
    conn.commit()
    conn.close()
    return date

def check_chat_id(chat_id):
    try:
        # Подключение к базе данных MySQL
        cursor = None
        conn = None
        conn = mysql.connector.connect(
        username = 'doadmin'
        password = 'AVNS_VSLcWQ0vFSrPTS7QO88'
        host = 'private-db-mysql-nyc3-12595-do-user-16381338-0.k.db.ondigitalocean.com'
        port = '25060'
        database = 'defaultdb'
        sslmode = 'REQUIRED'
        
    )

        cursor = conn.cursor()

        # Запрос для проверки наличия chat_id
        query = "SELECT COUNT(*) FROM bot_express WHERE chat_id = %s"
        cursor.execute(query, (chat_id,))

        # Получение результата
        result = cursor.fetchone()

        if result[0] > 0:
            return 1  # Если запись найдена
        else:
            return 0  # Если запись не найдена

    except mysql.connector.Error as err:
        print(f"Ошибка: {err}")
        return 0  # Возврат 0 при ошибке

    finally:
        # Закрытие соединения
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def get_all_chat_id():
    cursor = None
    conn = None
    conn = mysql.connector.connect(
        username = 'doadmin'
        password = 'AVNS_VSLcWQ0vFSrPTS7QO88'
        host = 'private-db-mysql-nyc3-12595-do-user-16381338-0.k.db.ondigitalocean.com'
        port = '25060'
        database = 'defaultdb'
        sslmode = 'REQUIRED'
        
    )

    cursor = conn.cursor()

    cursor.execute('SELECT chat_id FROM bot_express')

    date = cursor.fetchall()
    
    conn.commit()
    conn.close()
    
    return date
