import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_currency():
    result = list(filter_by_currency([], "RUB"))
    assert len(result) == 0


def test_filter_currency_empty(test_transactions):
    result = list(filter_by_currency(test_transactions, ""))
    assert len(result) == 0


@pytest.mark.parametrize("currency, counter", [
    ("USD", 3),
    ("RUB", 1),
])
def test_filter_currency_val(test_transactions, currency, counter, ):
    result = list(filter_by_currency(test_transactions, currency))
    assert len(result) == counter


@pytest.mark.parametrize("expected", [
    ["Перевод организации", "Перевод с карты на счет"],
])
def test_transaction_descriptions(transactions_desc, expected):
    descriptions = list(transaction_descriptions(transactions_desc))
    assert descriptions == expected


def test_transaction_descriptions_empty():
    descriptions = list(transaction_descriptions([]))
    assert len(descriptions) == 0


def test_card_number_generator():
    result = list(card_number_generator(1, 5))
    assert result == ["0000 0000 0000 0001",
                      "0000 0000 0000 0002",
                      "0000 0000 0000 0003",
                      "0000 0000 0000 0004"]


def test_card_number_generator_max():
    result = list(card_number_generator(9999999999999995, 9999999999999999))
    assert result == ["9999 9999 9999 9995",
                      "9999 9999 9999 9996",
                      "9999 9999 9999 9997",
                      "9999 9999 9999 9998"]
