# Отчет

## Графики с учебника matplotlib 1.1 - 3.29

**1.1**

![1.1](/lab2/photo_graphics/Figure_1.png)

**1.3**

![1.3](/lab2/photo_graphics/Figure_13.png)

**1.4**

![1.4](/lab2/photo_graphics/Figure_14.png)

**1.5**

![1.5](/lab2/photo_graphics/Figure_15.png)

**1.6**

![1.6](/lab2/photo_graphics/Figure_16.png)

**1.7**

![1.7](/lab2/photo_graphics/Figure_17.png)

**1.8**

![1.8](/lab2/photo_graphics/Figure_18.png)

**2.1**

![2.1](/lab2/photo_graphics/Figure_2.png)

**2.2**

![2.2](/lab2/photo_graphics/Figure_22.png)

**2.3**

![2.3](/lab2/photo_graphics/Figure_23.png)

**2.4**

![2.4](/lab2/photo_graphics/Figure_24.png)

**2.5**

![2.5](/lab2/photo_graphics/Figure_25.png)

**2.6**

![2.6](/lab2/photo_graphics/Figure_26.png)

**2.7**

![2.7](/lab2/photo_graphics/Figure_27.png)

**2.8**

![2.8](/lab2/photo_graphics/Figure_28.png)

**2.9**

![2.9](/lab2/photo_graphics/Figure_29.png)

**2.10**

![2.10](/lab2/photo_graphics/Figure_210.png)

**2.10.1**

![2.10.1](/lab2/photo_graphics/Figure_2101.png)

**2.11**

![2.11](/lab2/photo_graphics/Figure_211.png)

**3.1**

![3.1](/lab2/photo_graphics/Figure_31.png)

**3.2**

![3.2](/lab2/photo_graphics/Figure_32.png)

**3.3**

![3.3](/lab2/photo_graphics/Figure_33.png)

**3.4**

![3.4](/lab2/photo_graphics/Figure_34.png)

**3.5**

![3.5](/lab2/photo_graphics/Figure_35.png)

**3.6**

![3.6](/lab2/photo_graphics/Figure_36.png)

**3.7**

![3.7](/lab2/photo_graphics/Figure_37.png)

**3.8**

![3.8](/lab2/photo_graphics/Figure_38.png)

**3.9**

![3.9](/lab2/photo_graphics/Figure_39.png)

**3.10**

![3.10](/lab2/photo_graphics/Figure_310.png)

**3.11**

![3.11](/lab2/photo_graphics/Figure_311.png)

**3.12**

![3.12](/lab2/photo_graphics/Figure_312.png)

**3.13**

![3.13](/lab2/photo_graphics/Figure_313.png)

**3.14**

![3.14](/lab2/photo_graphics/Figure_314.png)

**3.15**

![3.15](/lab2/photo_graphics/Figure_315.png)

**3.16**

![3.16](/lab2/photo_graphics/Figure_316.png)

**3.17**

![3.17](/lab2/photo_graphics/Figure_317.png)

**3.18**

![3.18](/lab2/photo_graphics/Figure_318.png)

**3.19**

![3.19](/lab2/photo_graphics/Figure_319.png)

**3.20**

![3.20](/lab2/photo_graphics/Figure_320.png)

**3.21**

![3.21](/lab2/photo_graphics/Figure_321.png)

**3.22**

![3.22](/lab2/photo_graphics/Figure_322.png)

**3.23**

![3.23](/lab2/photo_graphics/Figure_323.png)

**3.23.1**

![3.23.1](/lab2/photo_graphics/Figure_3231.png)

**3.24**

![3.24](/lab2/photo_graphics/Figure_324.png)

**3.25**

![3.25](/lab2/photo_graphics/Figure_325.png)

**3.26**

![3.26](/lab2/photo_graphics/Figure_326.png)

**3.27**

![3.27](/lab2/photo_graphics/Figure_327.png)

**3.28**

![3.28](/lab2/photo_graphics/Figure_328.png)

**3.29**

![3.29](/lab2/photo_graphics/Figure_329.png)

# Отчет

# Задание Вариант 1

## 1. Описание проделанной работы:
1. Я импортировал библиотеки matplotlib и numpy
2. Изучил уроки по построению графика
3. Создал график:
![вариант 1](images/scsc.png) на промежутке 0<=x<=1
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

## Список использованных источников

1. [NumPy documentation — numpy.where](https://numpy.org/doc/stable/reference/generated/numpy.where.html)
2. [Matplotlib documentation](https://matplotlib.org/stable/contents.html)
3. [Matplotlib cheatsheets and handouts](https://matplotlib.org/cheatsheets/)
4. [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
5. [Writing mathematical expressions on GitHub](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)

# medium
Применены современные стили оформления
Обеспечена читаемость и информативность графиков
# well-done
Создан интерактивный график функции №3 в Plotly
Реализован экспорт в HTML с подключением через CDN
Обеспечена возможность публикации по ссылке