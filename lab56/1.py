def count(lst):
    total = 0 # начинаем с 0
    
    for item in lst:  # идём по каждому элементу списка
        if isinstance(item, list):  # ечли элемент — тоже список
            total += 1              # считаем сам этот список за 1 элемент
            total += count(item)    # РЕКУРСИЯ: считаем всё внутри этого списка
        else:
            total += 1              # обычный элемент — просто +1
    return total  # возвращаю общее количество



def x(n):
    if n == 1: return 1
    if n == 2: return -1/8
    return ((n-1)*x(n-1))/3 + ((n-2)*x(n-2))/4


