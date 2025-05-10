import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_usd_currency(list_dict_transactions):
    """Тест работы функции"""
    filter_by_usd_currency = filter_by_currency(list_dict_transactions, "USD")
    result = list(filter_by_usd_currency)
    assert len(result) == 3


def test_filter_by_rub_currency(list_dict_transactions):
    """Тест работы функции"""
    filter_by_rub_currency = filter_by_currency(list_dict_transactions, "RUB")
    result = list(filter_by_rub_currency)
    assert len(result) == 2


def test_no_matching_currency(list_dict_transactions):
    """Тест при отсутствии запрашиваемой валюты"""
    rub_transactions = filter_by_currency(list_dict_transactions, "EUR")
    result = list(rub_transactions)
    assert len(result) == 0


def test_empty_transactions_list():
    """Тест при пустом списке"""
    empty_transactions = filter_by_currency([], "USD")
    result = list(empty_transactions)
    assert len(result) == 0


def test_transaction_descriptions(list_dict_transactions):
    """Тест работы функциит"""
    transaction_description = transaction_descriptions(list_dict_transactions)
    assert next(transaction_description) == "Перевод организации"
    assert next(transaction_description) == "Перевод со счета на счет"
    assert next(transaction_description) == "Перевод со счета на счет"
    assert next(transaction_description) == "Перевод с карты на карту"
    assert next(transaction_description) == "Перевод организации"


def test_empty_transaction_descriptions():
    """Тест при пустом списке"""
    transaction_description = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(transaction_description)


def test_normal_range():
    """Тест генерации в обычном диапазоне"""
    generator = card_number_generator(1, 5)
    results = list(generator)

    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]

    assert results == expected
    assert len(results) == 5


def test_single_value():
    """Тест генерации единственного номера"""
    generator = card_number_generator(42, 42)
    results = list(generator)

    assert results == ["0000 0000 0000 0042"]
    assert len(results) == 1


def test_format_correctness():
    """Тест корректности форматирования номеров"""
    generator = card_number_generator(1234567812345678, 1234567812345678)
    results = list(generator)

    assert results == ["1234 5678 1234 5678"]
    assert len(results[0]) == 19
