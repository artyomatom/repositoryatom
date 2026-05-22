def repeat_safe(n):

    def decorator(func):
        call_depth = 0  # отслеживаем глубину вызова

        def wrapper(*args, **kwargs):
            nonlocal call_depth
            call_depth += 1
            try:
                if call_depth == 1:
                    # Только первый вызов повторяется
                    results = []
                    for _ in range(n):
                        results.append(func(*args, **kwargs))
                    return results
                else:
                    # Рекурсивные вызовы выполняются как обычно
                    return func(*args, **kwargs)
            finally:
                call_depth -= 1
        return wrapper
    return decorator