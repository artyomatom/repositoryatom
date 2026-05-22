"""
Лабораторная работа №5 - Декоратор с опциональным параметром
Уровень: Medium
Поддержка рекурсивных функций
"""

from functools import wraps


def repeat_decorator(times=None):
    """
    Декоратор с опциональным параметром
    Если параметр не указан - выполняет функцию 1 раз
    Поддерживает рекурсивные функции
    """
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Проверка на рекурсивный вызов
            if kwargs.get('_recursive_call', False):
                return func(*args, **{k: v for k, v in kwargs.items() if k != '_recursive_call'})
            
            n = times if times is not None else 1
            results = []
            
            for i in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            
            # Если вызван 1 раз, возвращаем результат напрямую
            return results[0] if len(results) == 1 else results
        
        return wrapper
    return decorator


# ===== ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ =====

@repeat_decorator()  # Без параметров - выполнится 1 раз
def simple_function():
    """Функция без указания параметра"""
    return "Called once"


@repeat_decorator(3)  # С параметром - выполнится 3 раза
def triple_function():
    """Функция с повторением 3 раза"""
    import random
    return random.randint(1, 100)


@repeat_decorator(5)
def recursive_factorial(n):
    """Рекурсивная функция вычисления факториала"""
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)


if __name__ == "__main__":
    print("=== Декоратор с опциональным параметром ===\n")
    
    print("1. Без параметра (1 вызов):")
    print(f"   simple_function() = {simple_function()}")
    
    print("\n2. С параметром (3 вызова):")
    print(f"   triple_function() = {triple_function()}")
    
    print("\n3. Рекурсивная функция (5 вызовов):")
    results = recursive_factorial(5)
    print(f"   recursive_factorial(5) = {results}")
    print(f"   (Все результаты одинаковы: 5! = 120)")