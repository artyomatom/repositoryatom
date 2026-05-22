"""
Лабораторная работа №5 - Декоратор-класс
Уровень: Well-done
Реализация декоратора как класса вместо функции
"""

from functools import wraps


class RepeatDecorator:
    """
    Декоратор-класс, повторяющий вызов функции
    """
    
    def __init__(self, times=1):
        """
        Инициализация декоратора
        :param times: количество повторений
        """
        self.times = times
        self.call_count = 0
    
    def __call__(self, func):
        """
        Вызов декоратора
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(self.times):
                self.call_count += 1
                result = func(*args, **kwargs)
                results.append(result)
            
            return results[0] if len(results) == 1 else results
        
        wrapper.instance = self  # Сохраняем ссылку на экземпляр
        return wrapper


class CalculatorClosure:
    """
    Класс-калькулятор с замыканием
    Альтернатива функциональному подходу
    """
    
    def __init__(self, operation, initial=0):
        """
        Инициализация калькулятора
        """
        self.operation = operation
        self.result = initial
        self.history = [initial]
    
    def __call__(self, value=None):
        """
        Вызов калькулятора
        """
        if value is None:
            return self.result
        
        if self.operation == '+':
            self.result += value
        elif self.operation == '-':
            self.result -= value
        elif self.operation == '*':
            self.result *= value
        elif self.operation == '/':
            if value != 0:
                self.result /= value
            else:
                raise ValueError("Деление на ноль!")
        else:
            raise ValueError(f"Неизвестная операция: {self.operation}")
        
        self.history.append(self.result)
        return self.result
    
    def get_history(self):
        """Возвращает историю вычислений"""
        return self.history.copy()
    
    def reset(self, new_initial=0):
        """Сбрасывает калькулятор"""
        self.result = new_initial
        self.history = [new_initial]


# ===== ДОПОЛНИТЕЛЬНЫЙ ДЕКОРАТОР: КЭШИРОВАНИЕ =====

class CacheDecorator:
    """
    Декоратор-класс для кэширования результатов функции
    """
    
    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.hits = 0
        self.misses = 0
    
    def __call__(self, *args):
        if args in self.cache:
            self.hits += 1
            return self.cache[args]
        
        self.misses += 1
        result = self.func(*args)
        self.cache[args] = result
        return result
    
    def get_stats(self):
        """Возвращает статистику кэша"""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        return {
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': f"{hit_rate:.2f}%"
        }


