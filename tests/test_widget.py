from src.widget import mask_account_card, get_date


def test_mask_account_card():
    """Базовая проверка"""
    assert mask_account_card('Visa Platinum 7000792289606361') == 'Visa Platinum 7000 79** **** 6361'
    assert mask_account_card('Счет 73654108430135874305') == 'Счет **4305'
    assert mask_account_card('Мир 19841984') == 'Введите корректные данные'
    assert mask_account_card('') == 'Введите корректные данные'


def test_get_date():
    """Базовая проверка"""
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'
    assert get_date('') == 'Введите корректные данные'
