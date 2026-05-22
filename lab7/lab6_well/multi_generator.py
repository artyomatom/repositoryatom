"""
Лабораторная работа №6 - Многопоточная версия генератора
Уровень: Well-done
Демонстрация повышения производительности
"""

import random
import time
from threading import Thread, Lock
from queue import Queue


class SimpleRandomGenerator:
    """
    Одноканальный генератор случайных чисел
    (базовая версия для сравнения)
    """
    
    def __init__(self, min_val=0, max_val=100):
        self.min_val = min_val
        self.max_val = max_val
        self.state = random.randint(0, 2**31 - 1)
    
    def next(self):
        """Генерация следующего числа"""
        self.state = (self.state * 48271) % (2**31 - 1)
        return self.min_val + (self.state % (self.max_val - self.min_val + 1))


class MultithreadedRandomGenerator:
    """
    Многопоточный генератор случайных чисел
    Использует несколько потоков для повышения производительности
    """
    
    def __init__(self, min_val=0, max_val=100, num_threads=4):
        self.min_val = min_val
        self.max_val = max_val
        self.num_threads = num_threads
        self.queue = Queue()
        self.lock = Lock()
        self.generators = []
        self.running = False
        
        # Создаём несколько независимых генераторов
        for _ in range(num_threads):
            gen = SimpleRandomGenerator(min_val, max_val)
            self.generators.append(gen)
    
    def _worker(self, gen_id, count):
        """Рабочий поток для генерации чисел"""
        gen = self.generators[gen_id]
        results = []
        
        for _ in range(count):
            value = gen.next()
            results.append(value)
        
        with self.lock:
            for val in results:
                self.queue.put(val)
    
    def generate(self, count):
        """
        Генерация заданного количества случайных чисел
        с использованием многопоточности
        """
        self.queue = Queue()
        self.running = True
        
        # Распределяем работу между потоками
        numbers_per_thread = count // self.num_threads
        threads = []
        
        for i in range(self.num_threads):
            thread_count = numbers_per_thread
            if i == self.num_threads - 1:
                # Последний поток берёт остаток
                thread_count += count % self.num_threads
            
            thread = Thread(target=self._worker, args=(i, thread_count))
            threads.append(thread)
            thread.start()
        
        # Ждём завершения всех потоков
        for thread in threads:
            thread.join()
        
        # Собираем результаты
        results = []
        while not self.queue.empty():
            results.append(self.queue.get())
        
        return results


def benchmark():
    """
    Сравнение производительности одноканальной 
    и многопоточной версий генератора
    """
    
    print("=== СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===\n")
    
    count = 1000000  # Количество чисел для генерации
    
    # Тест 1: Одноканальный генератор
    print(f"Генерация {count:,} случайных чисел:\n")
    
    print("1. Одноканальный генератор:")
    gen = SimpleRandomGenerator(0, 100)
    start = time.time()
    for _ in range(count):
        gen.next()
    single_time = time.time() - start
    print(f"   Время: {single_time:.4f} сек")
    print(f"   Скорость: {count/single_time:,.0f} чисел/сек")
    
    # Тест 2: Многопоточный генератор
    print("\n2. Многопоточный генератор (4 потока):")
    mt_gen = MultithreadedRandomGenerator(0, 100, num_threads=4)
    start = time.time()
    mt_gen.generate(count)
    multi_time = time.time() - start
    print(f"   Время: {multi_time:.4f} сек")
    print(f"   Скорость: {count/multi_time:,.0f} чисел/сек")
    
    # Расчёт ускорения
    speedup = single_time / multi_time
    print(f"\n=== РЕЗУЛЬТАТ ===")
    print(f"Ускорение: {speedup:.2f}x")
    
    if speedup >= 2:
        print("✓ Требование выполнено: ускорение >= 2x")
    else:
        print("⚠ Ускорение меньше 2x (зависит от количества ядер CPU)")
    
    return speedup


# ===== ДОПОЛНИТЕЛЬНЫЕ ГЕНЕРАТОРЫ =====

def fibonacci_generator():
    """Генератор чисел Фибоначчи"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator():
    """Генератор простых чисел"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

