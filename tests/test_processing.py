from src.processing import filter_by_state, sort_by_date
from tests.conftest import test_filter_empty, sort_empty


# @pytest.mark.parametrize("entrance, x, exit", [
#     ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], "EXECUTED",
#     [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
#     ])
def test_processing(test_filter_by_state):
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]) == test_filter_by_state


def test_filter_one(test_filter_empty):
    assert filter_by_state([{"state": "Finland"}]) == test_filter_empty
    assert filter_by_state([{}]) == test_filter_empty



def test_sort_date(sort_date):
    assert sort_by_date([
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]) == sort_date

def test_sort_date_1(sort_ex):
    assert sort_by_date([
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
            {"id": 594226727, "state": "CANCELED", "date": "2018/09/12"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
        ]) == sort_ex
def test_sort_date_2(sort_empty):
    assert sort_by_date([]) == sort_empty
