# import pytest
#
# from src.widget import mask_account_card
#
# @pytest.mark.parametrize("value", "expected", [
#     ("Maestro 7000792289606361", "Maestro 6361 79** **** 6361"),
#     ("Счет 70007922896051826361", "Счет **6361"),
# ])
# def test_mask_account_card(value, expected):
#     assert mask_account_card(value) == expected
