from config import TRANSACTION_PATH_JSON, TRANSACTION_PATH_CSV, TRANSACTION_PATH_EXCEL
from src.library_pandas import reading_transactions_csv, reading_transactions_excel
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
                        print("Некорректный выбор. Завершение программы.")
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
                        filtered_data = [

                        ]



        finally:
            print("XX")

if __name__ == "__main__":
    main()