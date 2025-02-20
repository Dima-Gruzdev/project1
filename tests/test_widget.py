import pytest

from src.widget import mask_account_card
from tests.conftest import unacceptable


def test_mask_account_empty(empty_string):
    var = mask_account_card("") == empty_string


def test_mask_account_unaccep(unacceptable):
    assert  mask_account_card("Maestro 700079228960636!") == unacceptable


@pytest.mark.parametrize("value, expected", [
    ("Maestro 7000792289606361", "Maestro 6361 79** **** 6361"),
    ("Счет 70007922896051826361", "Счет **6361"),
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected
