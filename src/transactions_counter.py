from collections import Counter


def counter_transaction(transactions_q: list[dict], categories_serv: list) -> dict:
    """Функция принимает список словарей и
    возвращает словарь, в котором ключи — это названия категорий,
     а значения — это количество операций в каждой категории."""
    category_counter = Counter()
    for transaction in transactions_q:
        if "description" in transaction:
            description = transaction["description"]
            category_counter[description] += 1
    result = {category: category_counter[category] for category in categories_serv}
    return result


if __name__ == "__main__":
    transactions_q = [
        {"id": 1, "description": "Оплата за услуги", "amount": 100},
        {"id": 2, "description": "Покупка товара", "amount": 2000},
        {"id": 3, "description": "Оплата за интернет", "amount": 350},
        {"id": 3, "description": "Оплата за интернет", "amount": 900},
        {"id": 4, "description": "Оплата за услуги", "amount": 200},
        {"id": 4, "description": "Оплата за услуги", "amount": 150},
    ]
    categories = [
        "Оплата за услуги",
        "Покупка товара",
        "Оплата за интернет",
        "Неправильная категория",
    ]
    transactions_count = counter_transaction(transactions_q, categories)
    print(transactions_count)
