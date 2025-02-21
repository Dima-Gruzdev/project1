import pytest

@pytest.fixture
def mask_string():
    return "**2626"


@pytest.fixture
def  empty_string():
    return "Пустая строка"


@pytest.fixture
def len_string():
    return "Неверная длина счета"

@pytest.fixture
def unacceptable():
    return "Недопустимые символы"

@pytest.fixture
def test_filter_by_state():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]

@pytest.fixture
def test_filter_empty():
    return []