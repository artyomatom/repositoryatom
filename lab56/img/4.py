def count_elements_recursive(data):
    """Рекурсивный подсчёт элементов во вложенных списках"""
    if not isinstance(data, list):
        return 1
    total = 0
    for item in data:
        total += count_elements_recursive(item)
    return total


def count_elements_iterative(data):
    """Итеративный подсчёт с использованием стека"""
    stack = [data]
    count = 0
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current)
        else:
            count += 1
    return count