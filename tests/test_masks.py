import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("cards, expected",[('1234 5678 9123 4567','1234 56** **** 4567'),
                                            ('','Введите корректные данные'),
                                            ('12345 67890','Введите корректные данные'),
                                            ('0987654321123456','0987 65** **** 3456')])
def test_get_mask_card_number(cards,expected):
    assert get_mask_card_number(cards) == expected


@pytest.mark.parametrize('accounts, expected', [('73654108430135874305','**4305'),
                                                ('','Введите корректные данные'),
                                                ('1919191919191919191','Введите корректные данные')])
def test_get_mask_account(accounts, expected):
    assert get_mask_account(accounts) == expected


