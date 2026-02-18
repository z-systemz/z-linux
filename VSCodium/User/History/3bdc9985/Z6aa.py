import pytest
from um import count

def test_um_returns_right_count():
    assert count("um") == 1
    assert count("um, um") == 2

def test_um_ignores_case():
    assert count("um Um um") == 3
    assert count("UM um UM uM") == 4

def test_um_doesnot_count_inside_words():
    assert