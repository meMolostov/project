import pytest

from src.decorators import log


def test_log_console(capsys):
    """Проверка вывода ошибок в консоль"""
    @log()
    def bad_divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        bad_divide(1, 0)

    captured = capsys.readouterr()
    assert "bad_divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_success(capsys):
    """Проверка корректной работы"""
    @log()
    def test_func(a, b):
        return a + b

    test_func(1, 2)
    captured = capsys.readouterr()
    assert 'test_func ok' in captured.out
