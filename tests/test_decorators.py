import pytest

from src.decorators import my_function


def test_decor():
    with pytest.raises(TypeError, match="can only concatenate str"):
        my_function(x="", y=2)


def test_decor_str():
    with pytest.raises(TypeError, match="unsupported operand type\\(s\\) for \\+: 'int' and 'str'"):
        my_function(1, "f")


def test_decor_empty():
    with pytest.raises(TypeError, match="my_function\\(\\) missing 2 required positional arguments: 'x' and 'y'"):
        my_function()