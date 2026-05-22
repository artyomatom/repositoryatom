"""
Лабораторная работа №6 - Генераторы
Вариант 1
Уровень: Rare
"""

import random


def random_number_generator(min_val=0, max_val=100):
    """
    Генератор случайных чисел в заданном диапазоне
    Не использует готовые реализации ГПСЧ
    Реализация на основе линейного конгруэнтного генератора
    """
    # Параметры LCG (Linear Congruential Generator)
    modulus = 2**31 - 1  # Простое число Мерсенна
    multiplier = 48271   # Множитель
    increment = 0        # Приращение
    
    # Начальное значение (seed)
    state = random.randint(1, modulus - 1)
    
    while True:
        # LCG формула: X_{n+1} = (a * X_n + c) mod m
        state = (multiplier * state + increment) % modulus
        
        # Преобразуем в нужный диапазон
        value = min_val + (state % (max_val - min_val + 1))
        
        yield value


def random_number_generator_simple(min_val=0, max_val=100):
    """
    Упрощённый генератор случайных чисел
    Использует системное время для генерации
    """
    import time
    
    state = int(time.time() * 1000) % 10000
    
    while True:
        # Простая псевдослучайная функция
        state = (state * 9301 + 49297) % 233280
        value = min_val + (state % (max_val - min_val + 1))
        yield value


