import pytest
from src.generators import card_number_generator, filter_by_currency


def test_card_number_generator():
    result = list(card_number_generator(1,5))
    assert result == ["0000 0000 0000 0001",
    "0000 0000 0000 0002",
    "0000 0000 0000 0003",
    "0000 0000 0000 0004"]

def test_filter_currency():
    result = list(filter_by_currency([],"руб"))
    assert len(result) == 0

