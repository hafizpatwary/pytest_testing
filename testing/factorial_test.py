import pytest
from python_execricses import factorial

def test_factorial():
	assert factorial.factorial(120) == 5, "failed zero factorial"