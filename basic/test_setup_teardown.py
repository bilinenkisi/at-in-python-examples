import pytest


@pytest.fixture
def create_temp_file(tmp_path):
    """
    # Açıklama: Test için geçici dosya oluşturan ve test sonrası temizleyen fixture
    # tmp_path pytest'in built-in bir fixture'ıdır
    """
    file_path = tmp_path / "test.txt"
    # Setup - dosyayı oluştur
    file_path.write_text("Bu bir test dosyasıdır")
    # Yield ile test fonksiyonuna dosya yolu verilir
    yield file_path
    # Teardown - herhangi bir temizlik işlemi buraya yazılabilir
    # (tmp_path otomatik silinecektir)



def test_file_content(create_temp_file):
    """
    # Açıklama: Geçici dosyanın içeriğini kontrol eder
    """
    assert create_temp_file.read_text() == "Bu bir test dosyasıdır"
    assert create_temp_file.exists()