import db
def test_fetch_data_from_db(mocker):
    mocker.patch("db.get_db_connection", return_value=True)
    assert db.fetch_data_from_db() == ["Alice", "Bob"]