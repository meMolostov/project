import pytest

from src.main import divide, calculate_logarithm, reverse_string


def test_divide():
    assert divide(2,1) == 2

    assert divide(2,0) == 0

def test_calc_log():
    assert calculate_logarithm(8,2) == 3.0
    assert calculate_logarithm(8,4) == 1.5

    with pytest.raises(ValueError) as exc_info:
        calculate_logarithm(0,2)
        assert str(exc_info.value) == "Логарифм можно вычислить только для положительных чисел"

    with pytest.raises(ValueError):
        calculate_logarithm(8, 0)

@pytest.mark.parametrize('value, expected', [
    ('123', '321'),
    ('hello', 'olleh'),
    ('world', 'dlrow')
])


def test_reverse_string(value, expected):
    assert reverse_string(value) == expected

# def test_reverse_string_numbers(numbers):
#     assert reverse_string("123") == numbers
#
# def test_reverse_string_letters(letters):
#     assert reverse_string("hello") == letters
