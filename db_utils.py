# Coded by: https://t.me/CryptoResearchLab
import sqlite3
import os

database_file = 'wallets.db'


def database_exists(db_file):
    return os.path.isfile(db_file)


def create_wallets_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS wallets (
                id INTEGER PRIMARY KEY,
                address TEXT UNIQUE,
                private_key TEXT,
                wallet_type TEXT
            )
        ''')
        connection.commit()
    except Exception as error:
        print(f" ! Возникла ошибка: {str(error)} ! ")


def check_if_database_exists():
    try:
        if not database_exists(database_file):
            print(f" ! База данных не обнаружена ! ")
            print(f" | Создаю базу данных: {database_file} | ")
            connection = sqlite3.connect(database_file)
            create_wallets_table(connection)
            connection.commit()
        else:
            print(f" | База данных {database_file} уже создана | ")
    except Exception as error:
        print(f" ! Возникла ошибка: {str(error)} ! ")


def add_new_wallet(wallet_address, private_key, wallet_type):
    try:
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO wallets (address, private_key, wallet_type) VALUES (?, ?, ?)',
                       (wallet_address, private_key, wallet_type))
        print(f" | Кошелек {wallet_address} успешно добавлен в базу данных | ")
        connection.commit()
    except Exception as error:
        print(f" ! Возникла ошибка: {str(error)} ! ")


def check_address_database(wallet_address, private_key, wallet_type):
    try:
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()
        cursor.execute('SELECT address FROM wallets WHERE address = ?', (wallet_address,))
        existing_address = cursor.fetchone()
        connection.commit()
        if existing_address:
            return "exists"
        else:
            add_new_wallet(wallet_address, private_key, wallet_type)
            return "added"
    except Exception as error:
        print(f" ! Возникла ошибка: {str(error)} ! ")


def fetch_all_wallets_by_type(wallet_type):
    try:
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()
        cursor.execute('SELECT address, private_key FROM wallets WHERE wallet_type = ?', (wallet_type,))
        wallets = cursor.fetchall()
        connection.commit()
        return wallets
    except Exception as error:
        print(f" ! Возникла ошибка: {str(error)} ! ")


def fetch_all_wallets():
    try:
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()
        cursor.execute('SELECT address, private_key, wallet_type FROM wallets')
        wallets = cursor.fetchall()
        connection.commit()
        return wallets
    except Exception as error:
        print(f" ! Возникла ошибка: {str(error)} ! ")
