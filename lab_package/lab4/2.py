from functools import lru_cache

@lru_cache(maxsize=None)
def x_recursive(n):
    """
    Вычисляет n-й член последовательности по формуле:
    x_i = ((i-1)*x_{i-1})/3 + ((i-2)*x_{i-2})/4
    x_1 = 1, x_2 = -1/8
    Возвращает float.
    """
    if n == 1:
        return 1.0
    elif n == 2:
        return -1/8
    else:
        return ((n - 1) * x_recursive(n - 1)) / 3 + ((n - 2) * x_recursive(n - 2)) / 4


class TestCountFunction:
    """Тесты для функции подсчета элементов"""

    def test_empty_list(self):
        assert count([]) == 0

    def test_flat_list(self):
        assert count([1, 2, 3]) == 3

    def test_nested_list_simple(self):

        assert count(["x", "y", ["z"]]) == 4

    def test_deeply_nested_list(self):

        assert count([1, 2, [3, 4, [5]]]) == 7

    def test_mixed_types(self):
        assert count([True, None, [1, "a"]]) == 4 # T, N, List, 1, a

    def test_single_nested(self):
        assert count([[[]]]) == 2


class TestSequenceFunction:
    """Тесты для рекуррентной формулы"""

    def test_base_case_1(self):
        assert x_recursive(1) == 1

    def test_base_case_2(self):
        assert x_recursive(2) == -0.125

    def test_third_element_manual_calc(self):

        assert x_recursive(3) == pytest.approx(expected)

    def test_fourth_element(self):
        expected = 5 / 48
        assert x_recursive(4) == pytest.approx(expected)

    def test_larger_n_performance(self):
        result = x_recursive(50)
        assert isinstance(result, float)
        assert result > -1000
