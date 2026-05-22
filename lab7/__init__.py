"""
Пакет с лабораторными работами №4-6
Лабораторная работа №7 - Комплексное применение
"""

# ===== ИМПОРТЫ ИЗ LAB4 (РЕКУРСИЯ) =====
# Из lab4_rare (базовые функции)
from .lab4_rare.solution import count_recursive, count_iterative, calculate_x_recursive, calculate_x_iterative

# Из lab4_well (оптимизированные версии)
from .lab4_well.optimized import count_optimized, calculate_x_memoized, calculate_x_optimized

# ===== ИМПОРТЫ ИЗ LAB5 (ЗАМЫКАНИЯ) =====
# Из lab5_rare (базовые замыкания)
from .lab5_rare.solution import make_calc, repeat

# Из lab5_medium (декоратор с опциональным параметром)
from .lab5_medium.optional_param import repeat_decorator

# Из lab5_well (декораторы-классы)
from .lab5_well.class_decorator import RepeatDecorator, CalculatorClosure, CacheDecorator

# ===== ИМПОРТЫ ИЗ LAB6 (ГЕНЕРАТОРЫ) =====
# Из lab6_rare (базовые генераторы)
from .lab6_rare.solution import random_number_generator, random_number_generator_simple

# Из lab6_well (многопоточные и дополнительные генераторы)
from .lab6_well.multi_generator import (
    SimpleRandomGenerator,
    MultithreadedRandomGenerator,
    fibonacci_generator,
    prime_generator
)

# ===== СПИСОК ЭКСПОРТИРУЕМЫХ ОБЪЕКТОВ =====
__all__ = [
    # Lab 4
    'count_recursive',
    'count_iterative',
    'calculate_x_recursive',
    'calculate_x_iterative',
    'count_optimized',
    'calculate_x_memoized',
    'calculate_x_optimized',

    # Lab 5
    'make_calc',
    'repeat',
    'repeat_decorator',
    'RepeatDecorator',
    'CalculatorClosure',
    'CacheDecorator',

    # Lab 6
    'random_number_generator',
    'random_number_generator_simple',
    'SimpleRandomGenerator',
    'MultithreadedRandomGenerator',
    'fibonacci_generator',
    'prime_generator'
]

__version__ = '1.0.0'
