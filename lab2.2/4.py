import itertools
def solve_1():
    letters = "ТИМОФЕЙ"
    valid_count = 0
for combo in itertools.product(letters, repeat = 5):
    word = ''.join(combo)
    y_count = word.count('Й')
    
    if y_count > 1:
        continue
    if y_count == 1:
        idx = word.index('Й')
        if idx == 0 or idx == 4:
            continue
        if (idx > 0 and word[idx-1] == "И") or (idx < 4 and word[idx+1] == "И"):
            continue
    valid_count += 1
return valid_count

def solve_2():
    value = 4**2020 + 2**2017 - 15
    return bin(value).count('1')

def solve_3():
    results = []
    for n in range(174457, 174506):
        divs = []
        # Находим все делители в диапазоне (1, n)
        for d in range(2, int(n**0.5) + 1):
            if n % d == 0:
                divs.append(d)
                if d != n // d:
                    divs.append(n // d)
        
        if len(divs) == 2:
            divs.sort()  # Делители в строке по возрастанию
            # Произведение делителей равно самому числу n, сортировка по n
            results.append((n, divs[0], divs[1]))
            
    # Сортировка по возрастанию произведения делителей (т.е. по n)
    results.sort(key=lambda x: x[0])
    return results

if __name__ == "__main__":
    print("="*50)
    print("РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ЗАДАЧ")
    print("="*50)
    
    ans1 = solve_1()
    print(f"Задача 1. Количество кодов: {ans1}")
    
    ans2 = solve_2()
    print(f"Задача 2. Количество единиц в двоичной записи: {ans2}")
    
    print("\nЗадача 3. Пары делителей:")
    ans3 = solve_3()
    for n, d1, d2 in ans3:
        print(f"{d1} {d2}")
    print("="*50)