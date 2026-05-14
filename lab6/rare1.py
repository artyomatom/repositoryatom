def make_calc(op, initial=0):
    result = initial

    def calculator(value):
        nonlocal result
        if op == '+':
            result += value
        elif op == '-':
            result -= value
        elif op == '*':
            result *= value
        elif op == '/':
            if value != 0:
                result /= value
            else:
                raise ZeroDivisionError("Деление на ноль!")
        else:
            raise ValueError(f"Неподдерживаемая операция: {op}")
        return result

    return calculator


if __name__ == "__main__":
    # Создаю калькулятор умножения, начинающий с 1
    calc = make_calc("*", initial=1)
    
    print(calc(5))   # 5
    print(calc(2))   # 10
    
    calc_add = make_calc("+", initial=0)
    print(calc_add(3))   # 3
    print(calc_add(7))   # 10
    
    calc_div = make_calc("/", initial=10)
    print(calc_div(2))   # 5.0
    try:
        print(calc_div(0))   # Должно вызвать ошибку
    except ZeroDivisionError as e:
        print(e)             # "Деление на ноль!"