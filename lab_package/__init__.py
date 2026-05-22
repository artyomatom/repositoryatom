"Пакет с лабораторными работами №4-6"

# Импорты из lab4
from .lab4.1 import count
from .lab4.2 import x_recursive
from .lab4.3 import count_optimized

# Импорты из lab5
from .lab5.rare1 import make_calc
from .lab5.rare2 import decorator
from .lab5.medium import decorator
from .lab5.well import register_methods


# Импорты из lab6
from .lab6.rare import make_random_generator
from .lab6.medium import test_deterministic_with_seed
from .lab6.well import get_generator

# Список того, что будет доступно
__all__ = [
    'count',
    'x_recursive',
    'count_optimized',
    'make_calc',
    'decorator',
    'register_methods',
    'make_random_generator'
    'test_deterministic_with_seed'
    'get_generator'
]