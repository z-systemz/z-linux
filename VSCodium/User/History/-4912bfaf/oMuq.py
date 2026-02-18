from working import convert

def test_raising_valueerror_for_bad_format():
    # Return True
    assert convert("9:00 AM to 5:00 PM")