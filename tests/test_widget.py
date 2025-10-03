import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_empty(empty_string):
    var = mask_account_card("") == empty_string


def test_mask_account_unaccep(unacceptable):
    assert mask_account_card("Maestro 700079228960636!") == unacceptable


@pytest.mark.parametrize("value, expected", [
    ("Maestro 7000792289606361", "Maestro 6361 79** **** 6361"),
    ("Счет 70007922896051826361", "Счет **6361"),
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize("date, trans_date", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("", "Дата отсутствует"),
    ("2024/03/11T02/26/18/671407", "Введите дату в правильном формате"),
])
def test_get_date(date, trans_date):
    assert get_date(date) == trans_date
