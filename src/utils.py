import json



def transactions_finance(path:str) -> any:
    """Функция которая с json файла возращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            transactions_dict = json.load(f)
            return transactions_dict
    except (json.JSONDecodeError, FileNotFoundError):
        return []


if __name__ == '__main__':
    print(transactions_finance('../data/operations.json'))


