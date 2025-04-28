import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("cards, expected", [('1234 5678 9123 4567', '1234 56** **** 4567'),
                                             ('1234567891234567', '1234 56** **** 4567'),
                                             ('1111222233334444', '1111 22** **** 4444'),
                                             ('0000000000000000', '0000 00** **** 0000'),
                                             ('9999 9999 9999 9999', '9999 99** **** 9999'),
                                             ('', 'Введите корректные данные'),
                                             ('qwerty', 'Введите корректные данные'),
                                             ('12345 67890', 'Введите корректные данные'),
                                             ('12345 678906789067890', 'Введите корректные данные'),
                                             ('0987654321123456', '0987 65** **** 3456')
                                             ])
def test_get_mask_card_number(cards, expected):
    """Тестирование правильности маскирования номера карты"""
    assert get_mask_card_number(cards) == expected


def test_get_mask_card_number_non_string():
    """Проверка обработки некорректных входных данных"""
    with pytest.raises(AttributeError):
        get_mask_card_number(1234567890123456)
    with pytest.raises(AttributeError):
        get_mask_card_number(None)


@pytest.mark.parametrize('accounts, expected', {('73654108430135874305', '**4305'),
                                                ('9999 9999 9999 9999 9999', '**9999'),
                                                ('99999999999999999999', '**9999'),
                                                ('ytrewq', 'Введите корректные данные'),
                                                ('00000 00000 00000 00000', '**0000'),
                                                ('1234 5678 9012 3456 7890', '**7890'),
                                                ('123', 'Введите корректные данные'),
                                                ('12345', 'Введите корректные данные'),
                                                ('123456789', 'Введите корректные данные'),
                                                ('7365410843013587430500000', 'Введите корректные данные'),
                                                ('', 'Введите корректные данные'),
                                                ('1919191919191919191', 'Введите корректные данные')})
def test_get_mask_account(accounts, expected):
    """Тестирование правильности маскирования номера счета"""
    assert get_mask_account(accounts) == expected


def test_get_mask_account_non_string():
    """Проверка обработки нестроковых входных данных"""
    with pytest.raises(AttributeError):
        get_mask_account(12345678901234567890)  # Число вместо строки
    with pytest.raises(AttributeError):
        get_mask_account(None)  # None вместо строки
