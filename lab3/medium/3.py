def find_numbers_with_two_divisors(start=174457, end=174505):
    """
    Находит числа в диапазоне [start, end], у которых ровно два собственных делителя
    (т.е. делителя, кроме 1 и самого числа).

    Args:
        start (int): начало диапазона (включительно).
        end (int): конец диапазона (включительно).

    Returns:
        list[tuple]: список кортежей (число, мин_делитель, макс_делитель),
                     отсортированный по возрастанию числа.
    """
    results = []

    for n in range(start, end + 1):
        divs = []

        for d in range(2, int(n**0.5) + 1):
            if n % d == 0:
                divs.append(d)
                if d != n // d:
                    divs.append(n // d)

        if len(divs) == 2:
            min_div = min(divs)
            max_div = max(divs)
            results.append((n, min_div, max_div))

    results.sort(key=lambda x: x[0])
    return results