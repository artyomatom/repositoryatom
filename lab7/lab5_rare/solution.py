"""
Лабораторная работа №5 - Замыкания
Вариант 1
Уровень: Rare
"""

from functools import wraps


# ===== ЗАДАЧА 1: Замыкание-калькулятор =====

def make_calc(operation, initial=0):
    """
    Замыкание-калькулятор, накапливающее результат
    Поддерживает 4 арифметические операции: +, -, *, /
    """
    result = initial
    
    def calc(value=None):
        nonlocal result
        
        if value is None:
            return result
        
        if operation == '+':
            result += value
        elif operation == '-':
            result -= value
        elif operation == '*':
            result *= value
        elif operation == '/':
            if value != 0:
                result /= value
            else:
                raise ValueError("Деление на ноль!")
        else:
            raise ValueError(f"Неизвестная операция: {operation}")
        
        return result
    
    return calc


# ===== ЗАДАЧА 2: Декоратор повторения =====

def repeat(times):
    """
    Декоратор, который запускает функцию указанное число раз
    и возвращает последовательность результатов
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

