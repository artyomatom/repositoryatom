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


# ===== ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ =====

if __name__ == "__main__":
    print("=== ЗАДАЧА 1: Калькулятор ===")
    
    # Сложение
    add_calc = make_calc('+', initial=0)
    print(f"add_calc(5) = {add_calc(5)}")  # 5
    print(f"add_calc(3) = {add_calc(3)}")  # 8
    print(f"add_calc() = {add_calc()}")    # 8
    
    print()
    
    # Умножение
    mul_calc = make_calc('*', initial=1)
    print(f"mul_calc(5) = {mul_calc(5)}")  # 5
    print(f"mul_calc(4) = {mul_calc(4)}")  # 20
    
    print("\n=== ЗАДАЧА 2: Декоратор repeat ===")
    
    @repeat(5)
    def get_random():
        import random
        return random.randint(1, 100)
    
    print(f"get_random() = {get_random()}")
    
    @repeat(3)
    def greet(name):
        return f"Hello, {name}!"
    
    print(f"greet('Alice') = {greet('Alice')}")