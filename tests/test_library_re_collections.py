from src.library_re_collections import entry_transactions


def test_library_collections_win():
    transactions = [
        {"id": 1, "description": "Оплата за услуги", "amount": 100},
        {"id": 2, "description": "Покупка товара", "amount": 200},
        {"id": 3, "description": "Оплата за интернет", "amount": 50},
    ]
    search_categ = "Оплата"
    expected_result = [
        {"id": 1, "description": "Оплата за услуги", "amount": 100},
        {"id": 3, "description": "Оплата за интернет", "amount": 50},
    ]
    result = entry_transactions(transactions, search_categ)
    assert result == expected_result


def test_search_no_matching_transactions():
    transactions = [
        {"id": 1, "description": "Оплата за услуги", "amount": 100},
        {"id": 2, "description": "Покупка товара", "amount": 200},
        {"id": 3, "description": "Оплата за интернет", "amount": 50},
    ]
    search_string = "отмена"
    expected_result = []
    result = entry_transactions(transactions, search_string)
    assert result == expected_result


def test_search_empty_transactions():
    search_string = "оплата"
    result = entry_transactions([], search_string)
    assert result == []