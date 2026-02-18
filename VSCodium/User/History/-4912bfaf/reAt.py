import pytest
from working import convert

def test_convert_correctly():
    assert convert("9:00 AM to 5:00 PM") == 8
    assert convert("9 AM to 5 PM") == 8
    assert convert("9:00 AM to 5 PM") == 8
    assert convert("9 AM to 5:00 PM") == 8

def test_convert_format_errors():
    with pytest.raises(ValueError):
        convert("9 am to 5 PM")
        convert("9 AM to 5 pm")
        convert("9 AM")
        convert("8AMto5PM")
        convert("8 AM to 5")
        convert("8 to 6 PM")

def test_convert_value_errors():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
        convert("10 AM to 13 PM")
        convert("12:60 AM to 12 PM")
        convert("12")