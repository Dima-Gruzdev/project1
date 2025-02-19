from src.masks import get_mask_account, get_mask_card_number
import pytest

from tests.conftest import empty_string


def test_get_mask_account(mask_string):
    assert get_mask_account("52523623584258622626") == mask_string


def test_get_mask_empty(empty_string):
    assert get_mask_account("") == empty_string


def test_get_mask_len(len_string):
    assert get_mask_account("52523623584258622626")