# Coded by: https://t.me/CryptoResearchLab
from prettytable import PrettyTable
from web3 import Web3
import db_utils
import datetime
import config


def generate_random_wallets():
    try:
        w3 = Web3(Web3.HTTPProvider(""))
        user_action_wallets_count = int(input("\n | -  Пожалуйста введите количество кошельков для генерации: "))
        user_action_db_insert = input(" | -  Добавлять сгенерированные кошельки в базу данных? (y-да / n-нет): ")
        print("\n")
        if user_action_db_insert == "y":
            current_datetime = datetime.datetime.now()
            date_time_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
            generated_wallets_file = f"data/output/generated_wallets_{date_time_str}.txt"

            for r in range(user_action_wallets_count):
                account = w3.eth.account.create()
                wallet_address = account.address
                wallet_private_key = Web3.to_hex(account._private_key)
                print(f" - | {wallet_address} | {wallet_private_key} | ")
                db_utils.add_new_wallet(wallet_address, wallet_private_key, "generated")
                generated_wallets = open(generated_wallets_file, 'a')
                generated_wallets.write(f"{wallet_address} | {wallet_private_key}\n")
                generated_wallets.close()
            print(f"\n | Файл с сгенерированными кошельками успешно сохранен в {generated_wallets_file} | ")

        elif user_action_db_insert == "n":
            current_datetime = datetime.datetime.now()
            date_time_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
            generated_wallets_file = f"data/output/generated_wallets_{date_time_str}.txt"

            for r in range(user_action_wallets_count):
                account = w3.eth.account.create()
                wallet_address = account.address
                wallet_private_key = Web3.to_hex(account._private_key)
                print(f" - | {wallet_address} | {wallet_private_key} | ")
                generated_wallets = open(generated_wallets_file, 'a')
                generated_wallets.write(f"{wallet_address} | {wallet_private_key}\n")
                generated_wallets.close()
            print(f"\n | Файл с сгенерированными кошельками успешно сохранен в {generated_wallets_file} | ")
        else:
            print(" ! Ошибка выбора действия ! ")
    except Exception as error:
        print(f" ! Возникла ошибка: {str(error)} ! ")


def show_wallets_transactions_table():
    try:
        print("\n"
              " - | 1. Показать статистику по транзакциям только импортированных кошельков.\n"
              " - | 2. Показать статистику по транзакциям только сгенерированных кошельков.\n"
              " - | 3. Показать статистику по транзакциям всех кошельков.\n"
              "")

        user_action = int(input(" - | -  Пожалуйста выберите номер действия: "))
        wallets_table = PrettyTable(["Address", "ETH", "OP", "ARB", "NOVA", "ZKS"])

        if user_action == int(1):
            wallets_imported = db_utils.fetch_all_wallets_by_type("imported")

            for wallet in wallets_imported:
                wallet_address = wallet[0]

                w3_eth = Web3(Web3.HTTPProvider(config.eth_rpc_url))
                eth_tx_count = w3_eth.eth.get_transaction_count(wallet_address)

                w3_op = Web3(Web3.HTTPProvider(config.op_rpc_url))
                op_tx_count = w3_op.eth.get_transaction_count(wallet_address)

                w3_arb = Web3(Web3.HTTPProvider(config.arbitrum_rpc_url))
                arb_tx_count = w3_arb.eth.get_transaction_count(wallet_address)

                w3_nova = Web3(Web3.HTTPProvider(config.arbitrum_nova_rpc_url))
                nova_tx_count = w3_nova.eth.get_transaction_count(wallet_address)

                w3_zks = Web3(Web3.HTTPProvider(config.zksync_rpc_url))
                zks_tx_count = w3_zks.eth.get_transaction_count(wallet_address)

                wallets_table.add_row([wallet_address,
                                       eth_tx_count,
                                       op_tx_count,
                                       arb_tx_count,
                                       nova_tx_count,
                                       zks_tx_count])

            print("\n")
            print(wallets_table)

        elif user_action == int(2):
            wallets_imported = db_utils.fetch_all_wallets_by_type("generated")

            for wallet in wallets_imported:
                wallet_address = wallet[0]

                w3_eth = Web3(Web3.HTTPProvider(config.eth_rpc_url))
                eth_tx_count = w3_eth.eth.get_transaction_count(wallet_address)

                w3_op = Web3(Web3.HTTPProvider(config.op_rpc_url))
                op_tx_count = w3_op.eth.get_transaction_count(wallet_address)

                w3_arb = Web3(Web3.HTTPProvider(config.arbitrum_rpc_url))
                arb_tx_count = w3_arb.eth.get_transaction_count(wallet_address)

                w3_nova = Web3(Web3.HTTPProvider(config.arbitrum_nova_rpc_url))
                nova_tx_count = w3_nova.eth.get_transaction_count(wallet_address)

                w3_zks = Web3(Web3.HTTPProvider(config.zksync_rpc_url))
                zks_tx_count = w3_zks.eth.get_transaction_count(wallet_address)

                wallets_table.add_row([wallet_address,
                                       eth_tx_count,
                                       op_tx_count,
                                       arb_tx_count,
                                       nova_tx_count,
                                       zks_tx_count])

            print("\n")
            print(wallets_table)

        elif user_action == int(3):
            wallets_imported = db_utils.fetch_all_wallets()

            for wallet in wallets_imported:
                wallet_address = wallet[0]

                w3_eth = Web3(Web3.HTTPProvider(config.eth_rpc_url))
                eth_tx_count = w3_eth.eth.get_transaction_count(wallet_address)

                w3_op = Web3(Web3.HTTPProvider(config.op_rpc_url))
                op_tx_count = w3_op.eth.get_transaction_count(wallet_address)

                w3_arb = Web3(Web3.HTTPProvider(config.arbitrum_rpc_url))
                arb_tx_count = w3_arb.eth.get_transaction_count(wallet_address)

                w3_nova = Web3(Web3.HTTPProvider(config.arbitrum_nova_rpc_url))
                nova_tx_count = w3_nova.eth.get_transaction_count(wallet_address)

                w3_zks = Web3(Web3.HTTPProvider(config.zksync_rpc_url))
                zks_tx_count = w3_zks.eth.get_transaction_count(wallet_address)

                wallets_table.add_row([wallet_address,
                                       eth_tx_count,
                                       op_tx_count,
                                       arb_tx_count,
                                       nova_tx_count,
                                       zks_tx_count])

            print("\n")
            print(wallets_table)

        else:
            print(" ! Ошибка выбора действия ! ")
    except Exception as error:
        print(f" ! Возникла ошибка: {str(error)} ! ")
