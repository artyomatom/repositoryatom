class BinaryCounter:
    """
    Класс для работы с двоичными представлениями больших чисел.
    """

    @staticmethod
    def count_ones(expression: str) -> int:
        """
        Вычисляет значение выражения и считает единицы в его двоичной записи.

        Args:
            expression (str): строковое представление математического выражения.

        Returns:
            int: количество единиц в двоичной записи результата.

        Example:
            >>> BinaryCounter.count_ones("4**2020 + 2**2017 - 15")
            ... # вернёт конкретное число
        """
        # В реальном проекте лучше использовать безопасный парсер, но для учебных целей — eval
        value = eval(expression)
        return bin(value).count('1')

    @classmethod
    def from_formula(cls, base1_exp1=2020, base2_exp2=2017, subtract=15) -> int:
        """
        Альтернативный способ вычисления через параметры.

        Args:
            base1_exp1 (int): степень для 4 (т.е. 4^base1_exp1)
            base2_exp2 (int): степень для 2 (т.е. 2^base2_exp2)
            subtract (int): вычитаемое значение

        Returns:
            int: количество единиц в двоичной записи.
        """
        value = 4**base1_exp1 + 2**base2_exp2 - subtract
        return bin(value).count('1')