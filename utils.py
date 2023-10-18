# Coded by: https://t.me/CryptoResearchLab
from prettytable import PrettyTable
from web3 import Web3
import db_utils
import datetime
import config


def read_and_check_private_keys():
    try:
        w3 = Web3(Web3.HTTPProvider(""))
        added_wallets_count = 0
        existing_wallets_count = 0
        with open(config.private_keys_file, 'r') as wallets_file:
            private_keys = wallets_file.readlines()
            private_keys_count = len(private_keys)
            print("\n")
            print(f" | Прочитано {private_keys_count} приватных ключей из {config.private_keys_file}. | ")
            db_utils.check_if_database_exists()
            for private_key in private_keys:
                account = w3.eth.account.from_key(private_key.strip())
                account_address = account.address
                result = db_utils.check_address_database(account_address, private_key.strip(), "imported")
                if result == "added":
                    added_wallets_count += 1
                elif result == "exists":
                    existing_wallets_count += 1
            if added_wallets_count > 0:
                print(f" | В базу данных успешно импортированы {added_wallets_count}"
                      f" кошельков из {config.private_keys_file} | ")
            else:
                print(
                    f" | В базе данных уже имеются {existing_wallets_count} кошельков из {config.private_keys_file} | ")
        print(" | База данных успешно обновлена | ")
    except FileNotFoundError:
        print(f" ! Возникла ошибка: Файл не найден {config.private_keys_file} ! ")
    except Exception as error:
        print(f" ! Возникла ошибка: {str(error)} ! ")


def export_wallets():
    try:
        print("\n"
              " - | 1. Экспортировать импортированные в БД кошельки.\n"
              " - | 2. Экспортировать сгенерированные кошельки.\n"
              " - | 3. Экспортировать все кошельки.\n"
              "")

        user_action = int(input(" - | -  Пожалуйста выберите номер действия: "))

        current_datetime = datetime.datetime.now()
        date_time_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

        if user_action == int(1):
            wallets_imported = db_utils.fetch_all_wallets_by_type("imported")

            exported_wallets_file = f"data/output/export_imported_wallets_{date_time_str}.txt"

            for wallet in wallets_imported:
                wallet_address = wallet[0]
                wallet_private_key = wallet[1]

                exported_wallets = open(exported_wallets_file, 'a')
                exported_wallets.write(f"{wallet_address} | {wallet_private_key}\n")
                exported_wallets.close()

            print(f"\n | Файл с импортированными кошельками успешно сохранен в {exported_wallets_file} | ")

        elif user_action == int(2):
            wallets_generated = db_utils.fetch_all_wallets_by_type("generated")

            exported_wallets_file = f"data/output/export_generated_wallets_{date_time_str}.txt"

            for wallet in wallets_generated:
                wallet_address = wallet[0]
                wallet_private_key = wallet[1]

                exported_wallets = open(exported_wallets_file, 'a')
                exported_wallets.write(f"{wallet_address} | {wallet_private_key}\n")
                exported_wallets.close()

            print(f"\n | Файл с сгенерированными кошельками успешно сохранен в {exported_wallets_file} | ")

        elif user_action == int(3):
            wallets_all = db_utils.fetch_all_wallets()

            exported_wallets_file = f"data/output/export_all_wallets_{date_time_str}.txt"

            for wallet in wallets_all:
                wallet_address = wallet[0]
                wallet_private_key = wallet[1]
                wallet_type = wallet[2]

                exported_wallets = open(exported_wallets_file, 'a')
                exported_wallets.write(f"{wallet_address} | {wallet_private_key} | {wallet_type}\n")
                exported_wallets.close()

            print(f"\n | Файл со всеми кошельками успешно сохранен в {exported_wallets_file} | ")
        else:
            print(" ! Ошибка выбора действия ! ")
    except Exception as error:
        print(f" ! Возникла ошибка: {str(error)} ! ")


def show_wallets_table():
    try:
        wallets_table = PrettyTable(["Address", "Private Key", "Wallet Type"])
        wallets_all = db_utils.fetch_all_wallets()
        for wallet in wallets_all:
            wallet_address = wallet[0]
            wallet_private_key = wallet[1]
            wallet_type = wallet[2]
            wallets_table.add_row([wallet_address, wallet_private_key, wallet_type])
        print("\n")
        print(wallets_table)
    except Exception as error:
        print(f" ! Возникла ошибка: {str(error)} ! ")