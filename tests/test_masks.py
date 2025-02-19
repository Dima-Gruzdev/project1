from src.masks import get_mask_account, get_mask_card_number

from tests.conftest import empty_string


def test_get_mask_account(mask_string):
    assert get_mask_account("52523623584258622626") == mask_string


def test_get_mask_empty(empty_string):
    assert get_mask_account("") == empty_string


def test_get_mask_len(len_string):
    assert get_mask_account("525236235842626") == len_string


def test_get_mask_card_number():
    assert get_mask_card_number("7005007857712585") == "2585 00** **** 2585"
    assert get_mask_card_number("") == "Пустая строка"
    assert get_mask_card_number("700500478577125824") == "Неверное количество цифр"


# @pytest.mark.parametrize('string', 'mask_card', [
#     ("7005007857712585", "2585 00** **** 2585"),
#     ("", "Пустая строка"),
#     ("700500478577125824", "Неверное количество цифр"),
# ])
# def test_get_mask_card_number(string, mask_card):
#     assert get_mask_card_number(string) == mask_card
