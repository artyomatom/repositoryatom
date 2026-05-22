"""
Лабораторная работа №5 - Тесты pytest
Уровень: Medium
"""

import pytest
from lab5_rare.solution import make_calc, repeat


class TestMakeCalc:
    """Тесты для замыкания-калькулятора"""
    
    def test_addition(self):
        calc = make_calc('+', initial=0)
        assert calc(5) == 5
        assert calc(3) == 8
        assert calc(2) == 10
    
    def test_subtraction(self):
        calc = make_calc('-', initial=10)
        assert calc(3) == 7
        assert calc(2) == 5
    
    def test_multiplication(self):
        calc = make_calc('*', initial=1)
        assert calc(5) == 5
        assert calc(4) == 20
        assert calc(2) == 40
    
    def test_division(self):
        calc = make_calc('/', initial=100)
        assert calc(10) == 10.0
        assert calc(2) == 5.0
    
    def test_division_by_zero(self):
        calc = make_calc('/', initial=10)
        with pytest.raises(ValueError):
            calc(0)
    
    def test_invalid_operation(self):
        with pytest.raises(ValueError):
            calc = make_calc('%', initial=0)
            calc(5)
    
    def test_get_result_without_args(self):
        calc = make_calc