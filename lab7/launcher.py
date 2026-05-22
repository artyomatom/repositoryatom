"""
Лабораторная работа №7
Запускающий модуль на основе Typer
CLI интерфейс для выбора и настройки параметров
"""

import typer
from typing import Optional
import json

from .lab4_rare.solution import count_recursive, count_iterative, calculate_x_recursive, calculate_x_iterative
from .lab5_rare.solution import make_calc, repeat
from .lab6_rare.solution import random_number_generator


app = typer.Typer(help="Лабораторная работа №7 - CLI интерфейс")


@app.command(name="count")
def count_elements(
    elements: str = typer.Argument(..., help="Список элементов в формате JSON"),
    method: str = typer.Option("recursive", "--method", "-m", help="Метод подсчёта (recursive/iterative)")
):
    """
    Подсчёт элементов в списке (включая вложенные)
    """
    try:
        lst = json.loads(elements)
    except json.JSONDecodeError:
        typer.echo("❌ Ошибка: некорректный JSON формат")
        raise typer.Exit(code=1)
    
    if method == "recursive":
        result = count_recursive(lst)
    elif method == "iterative":
        result = count_iterative(lst)
    else:
        typer.echo("❌ Ошибка: метод должен быть 'recursive' или 'iterative'")
        raise typer.Exit(code=1)
    
    typer.echo(f"✅ Результат ({method}): {result}")


@app.command(name="sequence")
def calculate_sequence(
    n: int = typer.Argument(..., help="Номер элемента последовательности"),
    method: str = typer.Option("iterative", "--method", "-m", help="Метод расчёта (recursive/iterative)")
):
    """
    Расчёт последовательности x_i
    """
    if n < 1:
        typer.echo("❌ Ошибка: n должно быть >= 1")
        raise typer.Exit(code=1)
    
    if method == "recursive":
        if n > 20:
            typer.echo("⚠️  Предупреждение: рекурсивный метод может быть медленным для больших n")
        result = calculate_x_recursive(n)
    elif method == "iterative":
        result = calculate_x_iterative(n)
    else:
        typer.echo("❌ Ошибка: метод должен быть 'recursive' или 'iterative'")
        raise typer.Exit(code=1)
    
    typer.echo(f"✅ x_{n} = {result:.10f}")


@app.command(name="calc")
def calculator(
    operation: str = typer.Argument(..., help="Операция (+, -, *, /)"),
    values: str = typer.Argument(..., help="Значения через запятую"),
    initial: float = typer.Option(0, "--initial", "-i", help="Начальное значение")
):
    """
    Калькулятор с замыканием
    """
    try:
        nums = [float(x.strip()) for x in values.split(",")]
    except ValueError:
        typer.echo("❌ Ошибка: некорректные числа")
        raise typer.Exit(code=1)
    
    calc = make_calc(operation, initial)
    
    for num in nums:
        result = calc(num)
    
    typer.echo(f"✅ Результат: {result}")


@app.command(name="random")
def generate_random(
    count: int = typer.Argument(10, help="Количество чисел"),
    min_val: int = typer.Option(0, "--min", help="Минимальное значение"),
    max_val: int = typer.Option(100, "--max", help="Максимальное значение")
):
    """
    Генератор случайных чисел
    """
    gen = random_number_generator(min_val, max_val)
    numbers = [next(gen) for _ in range(count)]
    
    typer.echo(f"✅ Случайные числа: {numbers}")


@app.command(name="demo")
def demo_all(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Подробный вывод")
):
    """
    Демонстрация всех возможностей пакета
    """
    typer.echo("=" * 60)
    typer.echo("ДЕМОНСТРАЦИЯ ВСЕХ ВОЗМОЖНОСТЕЙ ПАКЕТА")
    typer.echo("=" * 60)
    
    # Lab 4
    typer.echo("\n📦 Лабораторная №4 - Рекурсия")
    typer.echo("-" * 40)
    
    test_list = [1, 2, [3, 4, [5]], 6]
    count = count_recursive(test_list)
    typer.echo(f"count_recursive({test_list}) = {count}")
    
    x_10 = calculate_x_iterative(10)
    typer.echo(f"calculate_x_iterative(10) = {x_10:.6f}")
    
    # Lab 5
    typer.echo("\n📦 Лабораторная №5 - Замыкания")
    typer.echo("-" * 40)
    
    calc = make_calc('+', initial=0)
    calc(10)
    calc(5)
    typer.echo(f"calculator: {calc()}")
    
    # Lab 6
    typer.echo("\n📦 Лабораторная №6 - Генераторы")
    typer.echo("-" * 40)
    
    gen = random_number_generator(0, 100)
    numbers = [next(gen) for _ in range(10)]
    typer.echo(f"random numbers: {numbers}")
    
    typer.echo("\n" + "=" * 60)
    typer.echo("✅ Все демонстрации выполнены!")
    typer.echo("=" * 60)


@app.command(name="info")
def show_info():
    """
    Показать информацию о пакете
    """
    # Импортируем версии и список экспорта из текущего пакета
    from . import __version__, __all__

    typer.echo("=" * 60)
    typer.echo("ЛАБОРАТОРНАЯ РАБОТА №7")
    typer.echo("Пакеты и модули")
    typer.echo("=" * 60)
    typer.echo(f"\nВерсия: {__version__}")
    typer.echo(f"\nДоступные модули:")
    typer.echo("  • lab4 - Рекурсия")
    typer.echo("  • lab5 - Замыкания и декораторы")
    typer.echo("  • lab6 - Генераторы")
    typer.echo(f"\nДоступные функции: {len(__all__)}")
    typer.echo("\nИспользуйте 'lab7 --help' для списка команд")
    typer.echo("=" * 60)