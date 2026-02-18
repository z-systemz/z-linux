import pytest
from working import convert

def test_raising_valueerror_for_bad_format():
    # Return value
    assert convert("9:00 AM to 5:00 PM") == 8
    assert convert("9 AM to 5 PM") == 8
    assert convert("9:00 AM to 5 PM") == 8
    assert convert("9 AM to 5:00 PM") == 8
    # Raises ValueError
    with pytest.raises(ValueError):
        