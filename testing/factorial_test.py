import pytest
from python_exercise import factorial

def test_factorial():
	assert factorial.factorial(120) == 5, "failed zero factorial"
