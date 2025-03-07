# Проект "Домашнее задание"

## Описание

Проект "домашнее задание" - написание  функции на языке Python
1. Модуль masks.py - функции маскировки карты и счета
2. Модуль processing.py - функции  сортировки списка словарей по определеным параметрам
3. Модуль widget.py - функция  так же маскировки счета или карты и преобразования даты в другой формат 
4. Модуль generator - в Модуле  3 генератора: filter_by_currency - фильтрует словарь по Валюте, transaction_descriptions - выводит итератор по переводам, card_number_generator генератор по выводу номера карты  
5. Модуль decorators - Декоратор который автоматически  будет логировать начало и конец выполнения функции,
а также ее результаты или возникшие ошибки и открывать в отдельном файле mylog.txt
## Установка 

1. Клонируйте репозиторий:
"SSH-ключ""
git clone git@github.com:Dima-Gruzdev/project1.git

2. Установите зависимости:
pip install -r requirements.txt

## Использование
1.  Откройте приложение с функцией на вашем компьютере
2.  В готовые функции подставляйте свои данные для получения результаты 

## Лицензия 
Этот проект лицензирован по [лицензии MIT] (LICENSE)

### Тестирование 
Для тестирование используется библиотека 'pytest'. Что бы запустить тесты, выполните команду:
"""bash
pytest"""
Тесты покрывают следующие модули:
1. masks.py
2. processing.py
3. widget.py
4. generator.py
5. decorators.py

### Автор
Груздев Дмитрий Александрович
e-mail: nubile4446@mail.ru