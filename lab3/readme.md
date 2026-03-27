# Задание: построение графиков в Python
## 1. Описание проделанной работы:
1. Я импортировал библиотеки matplotlib и numpy
2. Изучил уроки по построению графика
3. Создал график:
![вариант 1](images/scsc.png) на промежутке 0<=x<=1 и касательную с нему в точке x=0,5
## 2. Программа
```python
import numpy as np
import matplotlib.pyplot as plt

# определение кусочной функции
def f(x):
    result = np.zeros_like(x)
    
    # первая часть: cos(x + x^3) и 0 <= x <= 1
    mask1 = (x >= 0) & (x <= 1)
    result[mask1] = np.cos(x[mask1] + x[mask1]**3)
    
    # вторая часть: e^(-x^2) - x^2 + 2x и 1 < x <= 2
    mask2 = (x > 1) & (x <= 2)
    result[mask2] = np.exp(-x[mask2]**2) - x[mask2]**2 + 2*x[mask2]
    
    return result

# Создание массива значений x
x = np.linspace(0, 2, 1000)
y = f(x)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='f(x)')

# Добавление точки разрыва (x = 1)
plt.axvline(x=1, color='r', linestyle='--', alpha=0.5, label='x = 1')

# Оформление графика
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('График кусочной функции', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 2)

# Показ графика
plt.tight_layout()
plt.show()
```
## 3. Вывод
![график](images/image.png)
## Использованные источники:
[Devpractice Team. Библиотека Matplotlib](https://evil-teacher.orbiter.website/books/prog_pm/matplotlib.pdf)