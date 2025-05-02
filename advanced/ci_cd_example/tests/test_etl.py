from src.etl import clean_data

def test_clean_data():
    assert clean_data(["  A", "B ", None]) == ["a", "b"]