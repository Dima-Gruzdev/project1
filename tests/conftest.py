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