from mypy.server.objgraph import Iterable
from src.tranzit import transactions


def filter_by_currency(transactions: list[dict], currency: str) -> Iterable[dict]:
    """Функция которая  фильтрует транзакции по определенной валюте"""
    return (x for x in transactions if x["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions: list[dict]) -> Iterable[str]:
    """Функция  которая принимает на вход  список словарей и возращает  итератор по очереди перевод"""
    for trans in transactions:
        if "description" in trans:
            yield trans["description"]


def card_number_generator(start, stop):
    """Генератор который выдает банковские карты в формате XXXX XXXX XXXX XXXX, где X— цифра номера
        в диапазоне  от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for number in range(start, stop):
        yield (f"{str(number).zfill(16)[:4]} {str(number).zfill(16)[4:8]} "
               f"{str(number).zfill(16)[8:12]} {str(number).zfill(16)[12:]}")


if __name__ == "__main__":
    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(2):
        print(next(usd_transactions))
    for card_number in card_number_generator(9999999999999995, 9999999999999999):
        print(card_number)
    descriptions = transaction_descriptions(transactions)
    for _ in range(2):
        print(next(descriptions))
