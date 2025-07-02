import pytest
from pytemplate1.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3
    assert calc.add(-1, 1) == 0
    assert calc.add(-1, -1) == -2

def test_sub():
    calc = Calculator()
    assert calc.sub(5, 2) == 3
    assert calc.sub(2, 5) == -3
    assert calc.sub(-1, -1) == 0

def test_mul():
    calc = Calculator()
    assert calc.mul(2, 3) == 6
    assert calc.mul(-2, 3) == -6
    assert calc.mul(-2, -3) == 6
    assert calc.mul(0, 5) == 0

def test_div():
    calc = Calculator()
    assert calc.div(6, 2) == 3
    assert calc.div(5, 2) == 2.5
    assert calc.div(-6, 2) == -3
    assert calc.div(6, -2) == -3

def test_div_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        calc.div(1, 0)
