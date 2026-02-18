import pytest
from um import count

def test_um_matching():
    assert count("um") == 1
    assert count("um, um") == 2
    assert count("yum yum um um") == 2

def test_um_raises_errors():
    with pytest.raises(ValueError)    
