import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_default_state(sample_transactions) -> None:
    """Тестирование фильтрации по умолчанию (state='EXECUTED')"""
    assert filter_by_state(sample_transactions) == [{"id": 1, "state": "EXECUTED", "amount": 100},
                                                    {"id": 3, "state": "EXECUTED", "amount": 300}
                                                    ]


def test_filter_empty_result(sample_transactions) -> None:
    """Тестирование, когда state не указан"""
    assert filter_by_state(sample_transactions, "FAILED") == []


@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [{"id": 1, "state": "EXECUTED", "amount": 100}, {"id": 3, "state": "EXECUTED", "amount": 300}]),
    ("PENDING", [{"id": 2, "state": "PENDING", "amount": 200}]),
    ("CANCELED", [{"id": 4, "state": "CANCELED", "amount": 400}]),
    ("UNKNOWN", []),
])
def test_filter_with_different_states(sample_transactions, state, expected)  -> None:
    """Параметризованный тест для разных значений state"""
    assert filter_by_state(sample_transactions, state) == expected


def test_sort_by_date_default(date_list) -> None:
    """Тестирование фильтрации по умолчанию - убывание date"""
    assert sort_by_date(date_list) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
                                       ]


def test_sort_by_date_increase(date_list) -> None:
    """Тестирование фильтрации по возрастанию date"""
    assert sort_by_date(date_list, False) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]
