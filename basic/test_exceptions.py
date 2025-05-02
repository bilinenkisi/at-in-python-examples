import pytest


def divide(a, b):
    """
    # Açıklama: İki sayıyı böler
    # Bölen sıfır ise ZeroDivisionError fırlatır
    """
    return a / b


def test_divide_by_zero():
    """
    # Açıklama: Sıfıra bölme durumunda istisna fırlatıldığını test eder
    # pytest.raises ile bir istisnanın fırlatıldığını kontrol edebiliriz
    """
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

