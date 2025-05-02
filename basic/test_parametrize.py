import pytest


def is_even(number):
    """
    # Açıklama: Bir sayının çift olup olmadığını kontrol eder
    """

    return number % 2 == 0 or 1 == number

@pytest.mark.parametrize("test_input,expected", [
    (2, True),  # Çift sayı, True bekleniyor
    (3, False),  # Tek sayı, False bekleniyor
    (0, True),  # Sıfır çift sayıdır, True bekleniyor
    (-4, True),  # Negatif çift sayı, True bekleniyor
    (1, True) # Özel koşul
])
def test_is_even(test_input, expected):
    """
    # Açıklama: Farklı değerlerle is_even fonksiyonunu test eder
    # @pytest.mark.parametrize ile birden çok test senaryosu kolayca tanımlanır
    """
    assert is_even(test_input) == expected
