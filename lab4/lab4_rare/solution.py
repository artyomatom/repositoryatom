"""
Лабораторная работа №4 - Рекурсия
Вариант 1
Уровень: Rare
"""

# ===== ЗАДАЧА 1: Подсчёт элементов в списках =====

def count_recursive(lst):
    """
    Подсчёт числа элементов в списке, включая вложенные списки (рекурсивно)
    """
    if not lst:
        return 0
    
    first = lst[0]
    rest = lst[1:]
    
    if isinstance(first, list):
        return count_recursive(first) + count_recursive(rest)
    else:
        return 1 + count_recursive(rest)


def count_iterative(lst):
    """
    Подсчёт числа элементов в списке, включая вложенные списки (итеративно)
    """
    count = 0
    stack = [lst]
    
    while stack:
        current = stack.pop()
        for item in current:
            if isinstance(item, list):
                stack.append(item)
            else:
                count += 1
    
    return count


# ===== ЗАДАЧА 2: Расчёт последовательности =====

def calculate_x_recursive(i):
    """
    Расчёт x_i по формуле:
    x_i = ((i-1)*x_{i-1})/3 + ((i-2)*x_{i-2})/4
    x_1 = 1, x_2 = -1/8
    (рекурсивно)
    """
    if i == 1:
        return 1
    elif i == 2:
        return -1/8
    else:
        return ((i-1) * calculate_x_recursive(i-1)) / 3 + \
               ((i-2) * calculate_x_recursive(i-2)) / 4


def calculate_x_iterative(i):
    """
    Расчёт x_i по формуле:
    x_i = ((i-1)*x_{i-1})/3 + ((i-2)*x_{i-2})/4
    x_1 = 1, x_2 = -1/8
    (итеративно)
    """
    if i == 1:
        return 1
    elif i == 2:
        return -1/8
    
    x_prev2 = 1  # x_1
    x_prev1 = -1/8  # x_2
    
    for n in range(3, i + 1):
        x_current = ((n-1) * x_prev1) / 3 + ((n-2) * x_prev2) / 4
        x_prev2 = x_prev1
        x_prev1 = x_current
    
    return x_prev1


# ===== ТЕСТИРОВАНИЕ =====
if __name__ == "__main__":
    print("=== ЗАДАЧА 1: Подсчёт элементов ===")
    print(f"count([]) = {count_recursive([])}")
    print(f"count([1, 2, 3]) = {count_recursive([1, 2, 3])}")
    print(f"count(['x', 'y', ['z']]) = {count_recursive(['x', 'y', ['z']])}")
    print(f"count([1, 2, [3, 4, [5]]]) = {count_recursive([1, 2, [3, 4, [5]]])}")
    
    print("\n=== ЗАДАЧА 2: Последовательность ===")
    for i in range(1, 11):
        print(f"x_{i} = {calculate_x_recursive(i):.6f}")