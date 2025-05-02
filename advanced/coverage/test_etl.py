from etl import clean_data,clean_data_title,print_o
import pytest
def test_clean_data():
    assert clean_data(["  A", "B ", None]) == ["a", "b"]
#
# def test_clean_data_title():
#     assert clean_data_title(["  a", "b ", None]) == ["A","B"]
#
# def test_print():
#     print_o("test")
