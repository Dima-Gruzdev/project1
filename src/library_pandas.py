import csv
import pandas as pd


def reading_transactions_csv(path: str) -> list[dict]:
    """ Функция чтение CSV файла транзакции"""
    try:
        with open(path, "r", encoding="utf8") as file:
            reading_csv = csv.DictReader(file, delimiter=";")
            return list(reading_csv)
    except (FileNotFoundError, ValueError) as error:
        print(error)
        return []


def reading_transactions_excel(filename: str) -> list[dict]:
    """Функция чтения Excel файла транзакции"""
    try:
        return pd.read_excel(filename).to_dict(orient='records')
    except (FileNotFoundError, ValueError) as err:
        print(err)
        return []


if __name__ == "__main__":
    print(reading_transactions_csv('../data/transactions.csv'))
    print(reading_transactions_excel('../data/transactions_excel.xlsx'))
