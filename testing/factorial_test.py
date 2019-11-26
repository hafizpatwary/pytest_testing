import pytest
from python_exercise import factorial

def test_factorial():
	assert factorial.factorial(120) == 5, "failed zero factorial"

def test_string():
	assert factorial.factorial('hello') == 'none', "failed"

def test_negative():
	assert factorial.factorial(-120) == '-5', "failed"
