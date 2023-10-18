# Coded by: https://t.me/CryptoResearchLab
from pyfiglet import Figlet
import evm_utils
import utils

if __name__ == "__main__":

    f = Figlet(font='slant', width=100)
    print("\n")
    print(f.renderText(" Wallets Manager "))
    print(" |  v0.1  |\n")
    print(" |  - Coded by: t.me/CryptoResearchLab  |\n")

    while True:
        print("\n"
              " | 1. Обновить базу данных кошельков.\n"
              " | 2. Сгенерировать новые кошельки.\n"
              " | 3. Экспортировать кошельки из базы дынных в .txt файл.\n"
              " | 4. Статистика транзакций по кошелькам из базы данных.\n"
              " | 5. Просмотр кошельков из базы данных.\n"
              "")

        user_action = int(input(" | -  Пожалуйста выберите номер действия: "))
        if user_action == int(1):
            utils.read_and_check_private_keys()
        elif user_action == int(2):
            evm_utils.generate_random_wallets()
        elif user_action == int(3):
            utils.export_wallets()
        elif user_action == int(4):
            evm_utils.show_wallets_transactions_table()
        elif user_action == int(5):
            utils.show_wallets_table()
        else:
            print(" ! Ошибка выбора действия ! ")