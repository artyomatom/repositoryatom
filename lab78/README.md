# ОТЧЕТ ПО ЛАБОРАТОРНОЙ РАБОТЕ 6
## ЗАМЫКАНИЯ
Замыкание — это механизм, позволяющий функции «запоминать» переменные из той области, где она была создана, даже после того, как эта область перестала существовать.

#### Как это работает в коде (простыми словами):
Мы создаём внешнюю функцию make_random_generator(seed).
Внутри неё объявляем переменную state, которая хранит текущее «семя» (число) для алгоритма.
Внутри объявляем внутреннюю функцию random_int(), которая:
Берёт текущее значение state.
Вычисляет новое случайное число по формуле.
Обновляет state для следующего раза.
Внешняя функция возвращает эту внутреннюю функцию random_int.
Когда мы вызываем полученную функцию много раз, она каждый раз помнит последнее значение state, потому что оно «замкнуто» внутри неё.

# rare
```
```

# medium
Модульное тестирование (Unit Testing) — это процесс проверки отдельных частей программы (в нашем случае — функции-генератора) на корректность работы. Я использовал библиотеку pytest, которая позволяет автоматически запускать набор проверок.

Генератор псевдослучайных чисел (ГПСЧ) кажется хаотичным, но на самом деле он детерминирован. Это значит, что при одинаковых начальных условиях (seed) он всегда выдает одну и ту же последовательность. Тесты помогают убедиться в:

1. Детерминизм: Если мы зададим одно и то же семя (seed=42), генератор должен выдать одинаковые числа.
2. Границы значений: Генератор никогда не должен выдать число меньше минимума или больше максимума диапазона.
3. Равномерность распределения: При большом количестве вызовов все числа из диапазона должны появляться примерно с одинаковой частотой. Если какие-то числа выпадают чаще других — алгоритм смещен (biased).

Мы пишем функции, начинающиеся с test_. Внутри каждой функции мы вызываем наш генератор и используем утверждения assert. Если условие неверно (например, число вышло за границы), тест с ошибкой.
```def test_deterministic_with_seed():
 """Один и тот же seed даёт одинаковую последовательность"""
    rng1 = make_random_generator(seed=42)
    rng2 = make_random_generator(seed=42)

    seq1 = [rng1(1, 100) for _ in range(10)]
    seq2 = [rng2(1, 100) for _ in range(10)]

assert seq1 == seq2```


# well-done
В чем разница между последовательным и параллельным выполнением?
1. В обычной программе задачи выполняются одна за другой. В многопоточной программе несколько задач могут выполняться одновременно, используя ресурсы процессора более эффективно.
Проблема общего состояния (Race Condition)
Наш генератор хранит состояние в переменной state. Если два потока попытаются изменить эту переменную одновременно, произойдет гонка данных (race condition): один поток перезапишет значение другого, и последовательность чисел станет неверной или предсказуемой.

решение: Изоляция состояния
Вместо того чтобы блокировать доступ к одному генератору, мы создали по отдельному генератору (замыканию) для каждого потока.
Каждый поток получает свой собственный экземпляр функции-генератора со своим уникальным seed.
Поскольку у каждого потока своя локальная переменная state, они не мешают друг другу. Блокировки (locks) нужны только в момент создания нового генератора, но не во время генерации чисел.
```
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
```



### Используемые материалы

- [Linear congruential generator — Wikipedia](https://en.wikipedia.org/wiki/Linear_congruential_generator)
- [Python Closures — Real Python](https://realpython.com/closures-python/)
- [pytest documentation](https://docs.pytest.org/)
- [concurrent.futures — Python Docs](https://docs.python.org/3/library/concurrent.futures.html)