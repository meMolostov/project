import pytest

from src.masks import get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number('1234 5678 9123 4567') == '1234 56** **** 4567'
    assert get_mask_card_number('') == ''
    assert get_mask_card_number()
