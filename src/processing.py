from datetime import datetime


def filter_by_state(filter_list: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция которая принимает на вход  список словарей и возращает новый отсортированный по ключу state"""
    new_list_filter = []
    for i in filter_list:
        if i.get('state') == state:
            new_list_filter.append(i)
    return new_list_filter


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, ]))


def sort_by_date(sort_by_list: list[dict], rev: bool=True) -> list[dict]:
    """Функция которая сортирует список словарей по убыванию по дате"""
    return sorted(sort_by_list, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=rev)


print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))