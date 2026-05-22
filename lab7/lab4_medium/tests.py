"""
Лабораторная работа №4 - Тесты pytest
Уровень: Medium
"""

import pytest
from lab4_rare.solution import (
    count_recursive, count_iterative,
    calculate_x_recursive, calculate_x_iterative
)


class TestCountElements:
    """Тесты для функции подсчёта элементов"""
    
    def test_empty_list(self):
        assert count_recursive([]) == 0
        assert count_iterative([]) == 0
    
    def test_simple_list(self):
        assert count_recursive([1, 2, 3]) == 3
        assert count_iterative([1, 2, 3]) == 3
    
    def test_nested_list(self):
        assert count_recursive(['x', 'y', ['z']]) == 3
        assert count_iterative(['x', 'y', ['z']]) == 3
    
    def test_deep_nested(self):
        assert count_recursive([1, 2, [3, 4, [5]]]) == 5
        assert count_iterative([1, 2, [3, 4, [5]]]) == 5
    
    def test_mixed_types(self):
        assert count_recursive([1, [2, 'a'], [[3]]]) == 4
        assert count_iterative([1, [2, 'a'], [[3]]]) == 4


class TestCalculateSequence:
    """Тесты для функции расчёта последовательности"""
    
    def test_base_cases(self):
        assert abs(calculate_x_recursive(1) - 1.0) < 1e-10
        assert abs(calculate_x_recursive(2) - (-1/8)) < 1e-10
        assert abs(calculate_x_iterative(1) - 1.0) < 1e-10
        assert abs(calculate_x_iterative(2) - (-1/8)) < 1e-10
    
    def test_recursive_vs_iterative(self):
        """Проверка, что рекурсивная и итеративная функции дают одинаковый результат"""
        for i in range(1, 15):
            rec_result = calculate_x_recursive(i)
            iter_result = calculate_x_iterative(i)
            assert abs(rec_result - iter_result) < 1e-10, f"Расхождение на i={i}"
    
    def test_sequence_values(self):
        """Проверка конкретных значений последовательности"""
        expected_values = {
            1: 1.0,
            2: -0.125,
            3: -0.041666666666666664,
        }
        
        for i, expected in expected_values.items():
            result = calculate_x_iterative(i)
            assert abs(result - expected) < 1e-10, f"Неверное значение для x_{i}"
