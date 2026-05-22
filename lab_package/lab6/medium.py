import pytest
from rare_generator import make_random_generator


def test_deterministic_with_seed():
    """Один и тот же seed даёт одинаковую последовательность"""
    rng1 = make_random_generator(seed=42)
    rng2 = make_random_generator(seed=42)

    seq1 = [rng1(1, 100) for _ in range(10)]
    seq2 = [rng2(1, 100) for _ in range(10)]

    assert seq1 == seq2


def test_range_boundaries():
    """Числа всегда в пределах [min, max]"""
    rng = make_random_generator(seed=123)
    for _ in range(1000):
        num = rng(-50, 50)
        assert -50 <= num <= 50


def test_uniform_distribution_approx():
    """Проверка равномерности распределения"""
    rng = make_random_generator(seed=999)
    counts = {i: 0 for i in range(1, 6)}
    for _ in range(10000):
        num = rng(1, 5)
        counts[num] += 1

    # Все значения встречаются примерно одинаково часто
    avg = 10000 / 5
    for count in counts.values():
        assert abs(count - avg) < 500  # допустимое отклонение


def test_different_seeds_different_sequences():
    """Разные seed → разные последовательности"""
    rng1 = make_random_generator(seed=1)
    rng2 = make_random_generator(seed=2)

    seq1 = [rng1(1, 100) for _ in range(5)]
    seq2 = [rng2(1, 100) for _ in range(5)]

    assert seq1 != seq2