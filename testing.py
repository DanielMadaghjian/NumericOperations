from NumericOperations import multiply
from NumericOperations import division
from NumericOperations import addition
from NumericOperations import subtraction

def test_mult():
	assert multiply(10,11) == 110
def test_div():
	assert division(10,2) == 5
def test_add():
	assert addition(10,11) == 21
def test_sub():
	assert subtraction(10,11) == -1