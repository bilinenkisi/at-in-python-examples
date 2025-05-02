import pytest
import sys


@pytest.mark.skip(reason="Bu test şu anda çalışmıyor")
def test_skipped():
    """
    # Açıklama: Bu test atlanacak
    # @pytest.mark.skip ile testleri atlayabiliriz
    """
    assert False  # Bu test çalıştırılmayacak


@pytest.mark.skipif(sys.version_info < (3, 10), reason="Python 3.10 gerektirir")
def test_python_version():
    """
    # Açıklama: Bu test sadece Python 3.10 ve üstünde çalışır
    # @pytest.mark.skipif ile koşullu test atlama yapabiliriz
    """
    assert sys.version_info >= (3, 10)

