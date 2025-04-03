from config import TRANSACTION_PATH_JSON, TRANSACTION_PATH_CSV, TRANSACTION_PATH_EXCEL
from src.library_pandas import reading_transactions_csv, reading_transactions_excel
from src.library_re_collections import entry_transactions
from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.utils import transactions_finance


def main():
    """Функция отвечает за основную логику проекта и связывает функциональности между собой.
    И возвращает информацию по транзакциям в зависимости от запроса"""
    while True:
        try:
            print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
            print("Выберите необходимый пункт меню:")
            while True:
                try:
                    choice = input("1. Получить информацию о транзакциях из JSON-файла\n"
                                   "2. Получить информацию о транзакциях из CSV-файла\n"
                                   "3. Получить информацию о транзакциях из XLSX-файла\n"
                                   "Пользователь: ").strip()
                    user_choice = int(choice)
                    if user_choice == 1:
                        print("Для обработки выбран JSON-файл")
                        transactions = transactions_finance(TRANSACTION_PATH_JSON)
                        break
                    elif user_choice == 2:
                        print("Для обработки выбран CSV-файл")
                        transactions = reading_transactions_csv(TRANSACTION_PATH_CSV)
                        break
                    elif user_choice == 3:
                        print("Для обработки выбран XLSX-файл")
                        transactions = reading_transactions_excel(TRANSACTION_PATH_EXCEL)
                        break
                    else:
                        print("Некорректный выбор. Пожалуйста выберите из 3 пунктов.")
                except ValueError as err:
                    print(f"Ошибка {err} при выборе пункта")
            while True:
                user_status = (input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                                     "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: ")
                               .strip()
                               .upper())
                if user_status not in ["EXECUTED", "CANCELED", "PENDING"]:
                    print(f"Ошибка статус {user_status} недоступен")
                    continue
                filtered_data = filter_by_state(transactions, user_status)
                print(f"Найдено операций: {len(filtered_data)}")
                if not filtered_data:
                    print("Нет транзакций с выбранном статусом.")
                    continue
                while True:
                    sort_choice = input("Отсортировать по дате? (да/нет): ").strip().lower()
                    if sort_choice in ["да", "нет"]:
                        break
                    else:
                        print("Ошибка введите ДА или НЕТ")
                if sort_choice == "да":
                    while True:
                        order_ascend_des = input(
                            "Отсортировать по возрастанию или по убыванию? \nПользователь: ").strip().lower()
                        if order_ascend_des in ["по возрастанию", "по убыванию"]:
                            break
                        else:
                            print("Ошибка введите либо ( по возрастанию) или (по убыванию)")
                    reverse = order_ascend_des == "по убыванию"
                    filtered_data = sort_by_date(filtered_data, reverse)
                while True:
                    rub_choice = input(
                        "Только рублевые транзакции? (да/нет): ").strip().lower()
                    if rub_choice in ["да", "нет"]:
                        break
                    else:
                        print("Введите да/нет")
                if rub_choice == "да":
                    filtered_data = [trans for trans in filtered_data
                                     if trans.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"]
                    print(f"Осталось рублевых  транзакций: {len(filtered_data)}")
                while True:
                    word_choice = input("Фильтровать по слову в описании? (да/нет)\n Пользователь: "
                                        ).strip().lower()
                    if word_choice in ["да", "нет"]:
                        break
                    else:
                        print("Введите ДА или НЕТ")
                if word_choice == "да":
                    keyword = input("Введите слово для поиска\n Пользователь: ").strip().lower()
                    if not keyword:
                        print("Ошибка введите слово")
                    else:
                        filtered_data = entry_transactions(filtered_data, keyword)
                        print(f" Найдено транзакций по слово {keyword}: {len(filtered_data)}")

                if not filtered_data:
                    print("Нет транзакцй по вашим критериям")
                else:
                    for i, transaction in enumerate(filtered_data, 1):
                        date = transaction.get("date", "нет даты")
                        descrip = transaction.get("description", "Без описания")
                        from_acc = transaction.get("from", "")
                        masked_from = ""
                        if from_acc:
                            try:
                                digits = "".join(b for b in from_acc if b.isdigit())
                                if "счет" in from_acc.lower():
                                    masked_from = from_acc.split()[0] + " " + get_mask_account(digits)
                                else:
                                    masked_from = " ".join(from_acc.split()[:-1]) + " " + get_mask_card_number(digits)
                            except Exception as error:
                                print(f"Ошибка {error}")
                                masked_from = from_acc
                        to_acc = transaction.get("to", "")
                        masked_to = ""
                        if to_acc:
                            try:
                                digits = "".join(c for c in to_acc if c.isdigit())
                                if "счет" in to_acc.lower():
                                    masked_to = to_acc.split()[0] + " " + get_mask_account(digits)
                                else:
                                    masked_to = " ".join(to_acc.split()[:-1] + " " + list(get_mask_card_number(digits)))
                            except Exception as err:
                                print(f"Ошибка маскировки {err}")
                                masked_to = to_acc
                        amount = transaction.get("operationAmount", {}).get("amount", "?")
                        currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", "")
                        print(f"\n{i}. {date} {descrip}")
                        if masked_from:
                            print(f" Откуда: {masked_from}")
                        print(f" Куда: {masked_to}")
                        print(f" Сумма: {amount} {currency}")
                    print(f"Всего операций: {len(filtered_data)}")
                while True:
                    continue_choice = input("Продолжить работу? (да/нет)").lower()
                    if continue_choice in ["да", "нет"]:
                        break
                    else:
                        print("Ошибка, введите ДА или НЕТ")
                if continue_choice == "нет":
                    break
        except Exception as er:
            print(f"Ошибка  при выполнение {er}")


if __name__ == "__main__":
    main()
