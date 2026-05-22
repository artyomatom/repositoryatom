"""
Лабораторная работа №6 - Тесты pytest
Уровень: Medium
"""

import pytest
from lab6_rare.solution import random_number_generator


class TestRandomGenerator:
    """Тесты для генератора случайных чисел"""
    
    def test_range_bounds(self):
        """Проверка попадания в диапазон"""
        gen = random_number_generator(0, 10)
        for _ in range(100):
            value = next(gen)
            assert 0 <= value <= 10
    
    def test_negative_range(self):
        """Проверка отрицательного диапазона"""
        gen = random_number_generator(-10, -1)
        for _ in range(50):
            value = next(gen)
            assert -10 <= value <= -1
    
    def test_single_value_range(self):
        """Проверка диапазона с одним значением"""
        gen = random_number_generator(5, 5)
        for _ in range(10):
            value = next(gen)
            assert value == 5
    
    def test_distribution(self):
        """Проверка равномерности распределения"""
        gen = random_number_generator(0, 9)
        counts = [0] * 10
        
        # Генерируем 10000 чисел
        for _ in range(10000):
            value = next(gen)
            counts[value] += 1
        
        # Каждое число должно встретиться примерно 1000 раз (±30%)
        for count in counts:
            assert 700 <= count <= 1300
    
    def test_different_instances(self):
        """Проверка, что разные экземпляры генерируют разные последовательности"""
        gen1 = random_number_generator(0, 100)
        gen2 = random_number_generator(0, 100)
        
        seq1 = [next(gen1) for _ in range(10)]
        seq2 = [next(gen2) for _ in range(10)]
        
        # Последовательности должны отличаться (с очень высокой вероятностью)
        assert seq1 != seq2
    
    def test_infinite_generator(self):
        """Проверка, что генератор бесконечный"""
        gen = random_number_generator(0, 10)
        for _ in range(1000):
            value = next(gen)
            assert 0 <= value <= 10


if __name__ == "__main__":
    pytest.main([__file__, "-v"])