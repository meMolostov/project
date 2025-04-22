import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("cards, expected",[('1234 5678 9123 4567','1234 56** **** 4567'),
                                            ('','Введите корректный номер'),
                                            ('12345 67890','Введите корректный номер'),
                                            ('0987654321123456','0987 65** **** 3456')])
def test_get_mask_card_number(cards,expected):
    assert get_mask_card_number(cards) == expected


# @pytest.mark.parametrize('accounts, expected', ['**4305',
#                                                 '**1111',
#                                                 '**2020'])
# def test_get_mask_account(accounts, expected):
#     assert get_mask_account(accounts) == expected


