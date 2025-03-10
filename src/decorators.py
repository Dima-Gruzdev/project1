from functools import wraps
from typing import Optional


def log(filename: Optional[any]) -> Optional[any]:
    """Декаратор который автоматически  будет логировать начало и конец выполнения функции,
     а также ее результаты или возникшие ошибки"""
    def my_decarator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"\n{function.__name__} ok")
                else:
                    print(f"\n{function.__name__} ok")
                return result
            except Exception as err:
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"\n{function.__name__} error: {err}. Inputs: {args}, {kwargs}")
                else:
                    print(f"\n{function.__name__} error: {err}. Inputs: {args}, {kwargs}")
                raise err
        return wrapper
    return my_decarator


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция складывает 2 числа для проверки"""
    return x + y


if __name__ == "__main__":
    print(my_function(1, 5))