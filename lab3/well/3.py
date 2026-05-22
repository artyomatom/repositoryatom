class DivisorAnalyzer:
    """
    Класс для анализа делителей чисел в заданном диапазоне.
    """

    def __init__(self, start=174457, end=174505):
        """
        Инициализация анализатора.

        Args:
            start (int): начало диапазона.
            end (int): конец диапазона.
        """
        self.start = start
        self.end = end

    def get_proper_divisors(self, n: int) -> list[int]:
        """
        Возвращает список собственных делителей числа n (кроме 1 и n).

        Args:
            n (int): анализируемое число.

        Returns:
            list[int]: список собственных делителей.
        """
        divs = []
        for d in range(2, int(n**0.5) + 1):
            if n % d == 0:
                divs.append(d)
                if d != n // d:
                    divs.append(n // d)
        return sorted(divs)

    def find_numbers_with_exact_divisors(self, count=2) -> list[tuple]:
        """
        Находит числа в диапазоне, у которых ровно `count` собственных делителей.

        Args:
            count (int): требуемое количество собственных делителей (по умолчанию 2).

        Returns:
            list[tuple]: список кортежей (число, мин_делитель, макс_делитель).
        """
        results = []
        for n in range(self.start, self.end + 1):
            divs = self.get_proper_divisors(n)
            if len(divs) == count:
                results.append((n, min(divs), max(divs)))
        return sorted(results, key=lambda x: x[0])