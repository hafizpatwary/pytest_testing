import pytest
from python_exercise import multiply_list

def test_product():
    assert multiply_list.product([5,5]) == 25
