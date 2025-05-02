import pytest

@pytest.fixture
def sample_data():
    """
    # Açıklama: Test için örnek veri hazırlayan bir fixture
    # Fixture'lar testler için ortak hazırlık kodunu içerir
    """
    return {"name": "Ahmet", "age": 25, "city": "Istanbul"}


def test_name_in_data(sample_data):
    """
    # Açıklama: sample_data fixture'ını kullanarak veri kontrolü yapar
    # Fixture'lar test fonksiyonlarına parametre olarak eklenir
    """
    assert "name" in sample_data
    assert sample_data["name"] == "Ahmet"

def test_age_in_data(sample_data):
    assert "age" in sample_data
    assert sample_data["age"] > 10