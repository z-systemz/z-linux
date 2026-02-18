import pytest
from working import convert

def test_convert_correctly():
    assert convert("9:00 AM to 5:00 PM") == 8
    assert convert("9 AM to 5 PM") == 8
    assert convert("9:00 AM to 5 PM") == 8
    assert convert("9 AM to 5:00 PM") == 8

def test_convert_format_errors():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")