def count_optimized(lst):
    total = 0
    stack = [lst]
    
    while stack:
        current = stack.pop()
        for item in current:
            if isinstance(item, list):
                total += 1
                stack.append(item)
            else:
                total += 1     
    return total

from functools import lru_cache

@lru_cache(maxsize=None)
def x(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1/8
    else:
        return ((n-1) * x(n-1)) / 3 + ((n-2) * x(n-2)) / 4