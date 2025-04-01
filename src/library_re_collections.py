import re


def entry_transactions(transactions_en: list[dict], search_string: str) -> list[dict]:
    """Функция принимающая данные с транзакциями , а возращает  список словарей по описанию данной строки"""
    pattern = re.compile(search_string, re.I)
    same_transactions = [transaction for transaction in transactions_en
                         if "description" in transaction and pattern.search(transaction["description"])]
    return same_transactions


if __name__ == "__main__":
    matched = entry_transactions([
        {"id": 1, "description": "Оплата за услуги", "amount": 100},
        {"id": 2, "description": "Покупка товара", "amount": 200},
        {"id": 3, "description": "Оплата за интернет", "amount": 50},
    ], "Покупка")

    for transaction in matched:
        print(transaction)
