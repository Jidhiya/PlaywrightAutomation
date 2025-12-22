from my_math import add
import time

def test_add_positive_numbers():
    result = add(2, 3)
    time.sleep(5)
    assert result == 5

def test_add_negative_numbers():
    result = add(-2, -3)
    time.sleep(5)
    assert result == -5

def test_add_mixed_numbers_1():
    result = add(2, -3)
    time.sleep(5)
    assert result == -1

def test_add_mixed_numbers_2():
    result = add(-2, 3)
    time.sleep(5)
    assert result == 1    

def test_add_zero():
    result = add(0, 0)
    time.sleep(5)
    assert result == 0