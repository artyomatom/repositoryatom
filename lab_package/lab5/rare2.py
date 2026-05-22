def repeat(n):

    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

if __name__ == "__main__":
    @repeat(3)
    def greet(name):
        return f"Hello, {name}!"

    # Вызываю функцию и печатаем результат
    result = greet("Alice")
    print(result)  # ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']

    @repeat(5)
    def add(a, b):
        return a + b

    print(add(2, 3))  # [5, 5, 5, 5, 5]

    @repeat(4)
    def square(x):
        return x ** 2

    print(square(4))  # [16, 16, 16, 16]