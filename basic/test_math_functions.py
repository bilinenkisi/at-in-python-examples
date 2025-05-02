
def add(a, b):
    """İki sayıyı toplar"""
    return a + b


def test_add():
    """
    # add() fonksiyonunu test eder
    # Açıklama: Toplama işleminin doğru çalıştığını kontrol eder
    """
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

