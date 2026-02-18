import pytest
from um import count

def test_um_matching():
    assert count("um") == 1
    assert count("um, um") == 2
    assert count("yum yum um um") == 2

def test_um_ignores_case():
    assert count("um Um um") == 3
    assert count("UM um UM uM") == 4

def test_um