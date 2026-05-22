import threading
import time
from concurrent.futures import ThreadPoolExecutor
from rare_generator import make_random_generator


class ThreadSafeRandomGenerator:
    def __init__(self, base_seed=42):
        self.base_seed = base_seed
        self.lock = threading.Lock()
        self.generators = {}  # key: thread_id, value: generator function

    def get_generator(self):
        tid = threading.get_ident()
        with self.lock:
            if tid not in self.generators:
                # Каждый поток получает свой генератор с уникальным seed
                seed = self.base_seed + tid % 1000
                self.generators[tid] = make_random_generator(seed=seed)
            return self.generators[tid]

    def random_int(self, min_val=0, max_val=100):
        gen = self.get_generator()
        return gen(min_val, max_val)


def generate_numbers_single_thread(n, min_val, max_val):
    rng = make_random_generator(seed=42)
    return [rng(min_val, max_val) for _ in range(n)]


def generate_numbers_multi_thread(n, min_val, max_val, num_threads=4):
    ts_rng = ThreadSafeRandomGenerator(base_seed=42)
    results = []

    def worker(count):
        return [ts_rng.random_int(min_val, max_val) for _ in range(count)]

    per_thread = n // num_threads
    remainder = n % num_threads

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for i in range(num_threads):
            count = per_thread + (1 if i < remainder else 0)
            futures.append(executor.submit(worker, count))

        for future in futures:
            results.extend(future.result())

    return results


if __name__ == "__main__":
    N = 1_000_000
    MIN, MAX = 1, 100

    print("️ Однопоточная генерация...")
    start = time.time()
    single_result = generate_numbers_single_thread(N, MIN, MAX)
    single_time = time.time() - start
    print(f"Время: {single_time:.4f} сек")

    print("\n⏱️ Многопоточная генерация (4 потока)...")
    start = time.time()
    multi_result = generate_numbers_multi_thread(N, MIN, MAX, num_threads=4)
    multi_time = time.time() - start
    print(f"Время: {multi_time:.4f} сек")

    print(f"\n Ускорение: {single_time / multi_time:.2f}x")
    print(f"Результаты совпадают по длине: {len(single_result) == len(multi_result)}")