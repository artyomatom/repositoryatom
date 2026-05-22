def make_random_generator(seed=None, a=1103515245, c=12345, m=2**31):
    if seed is None:
        import time
        seed = int(time.time() * 1000) % m
    state = [seed]  # использую список, чтобы можно было менять внутри nested function

    def random_int(min_val=0, max_val=100):
        state[0] = (a * state[0] + c) % m
        # масштабируем под диапазон [min_val, max_val]
        return min_val + (state[0] % (max_val - min_val + 1))

    return random_int


# пример использования:
if __name__ == "__main__":
    rng = make_random_generator(seed=42)
    print("Первые 5 чисел:")
    for _ in range(5):
        print(rng(1, 100))