import pytest
from python_exercise import count

def test_count_zeros():
    assert count.count([0,0,0],0)==3, "failed"

def test_count_string():
    assert count.count(["a", "a", "a"],"a")==3, "failed"

def test_count_str():
    assert count.count(["a", "b", "a"],"a")==3, "failed test"
