import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#настройка sea
sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams["figure.figsize"] = (10, 6)

def f1(x):
    result = np.full_like(x, np.nan)
    cond1 = (x >= 0) & (x <= 1)
    cond2 = (x > 1) & (x <= 2)
    result[cond1] = np.cos(x[cond1] + x[cond1]**3)
    result[cond2] = np.exp(-x[cond2]) - x[cond2]**2 + 2*x[cond2]
    return result
x1 = np.linspace(0, 2, 500)
y1 = f1(x1)

plt.figure()
sns.lineplot(x=x1, y=y1, linewidth=2.5)
plt.title('Функция 1: f(x) = {cos(x+x³), 0≤x≤1; e^(-x)-x²+2x, 1<x≤2}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()


ef f2(x):
    result = np.full_like(x, np.nan)
    cond1 = (x >= 0) & (x <= 0.25)
    cond2 = (x > 0.25) & (x <= 0.5)
    result[cond1] = np.exp(np.sin(x[cond1]))
    result[cond2] = np.exp(x[cond2]) - 1/np.sqrt(x[cond2])
    return result

x2 = np.linspace(0.001, 0.5, 500)  # начинаем с 0.001 чтобы избежать деления на 0
y2 = f2(x2)

plt.figure()
sns.lineplot(x=x2, y=y2, linewidth=2.5, color='orange')
plt.title('Функция 2: f(x) = {e^(sin x), 0≤x≤1/4; e^x-1/√x, 1/4<x≤1/2}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()


def f3(x):
    result = np.full_like(x, np.nan)
    cond1 = (x >= 0) & (x <= 1)
    cond2 = (x > 1) & (x <= 2)
    result[cond1] = np.cos(x[cond1]) * np.exp(-x[cond1]**2)
    result[cond2] = np.log(x[cond2] + 1) - np.sqrt(4 - x[cond2]**2)
    return result

x3 = np.linspace(0, 2, 500)
y3 = f3(x3)

plt.figure()
sns.lineplot(x=x3, y=y3, linewidth=2.5, color='green')
plt.title('Функция 3: f(x) = {cos(x)·e^(-x²), 0≤x≤1; ln(x+1)-√(4-x²), 1<x≤2}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

def f4(x):
    result = np.full_like(x, np.nan)
    cond1 = (x >= 0) & (x <= 1)
    cond2 = (x > 1) & (x <= 2)
    result[cond1] = np.sqrt(x[cond1] + 1) - np.sqrt(x[cond1]) - 0.5
    result[cond2] = np.exp(-x[cond2] - 1/x[cond2])
    return result

x4 = np.linspace(0.001, 2, 500)
y4 = f4(x4)

plt.figure()
sns.lineplot(x=x4, y=y4, linewidth=2.5, color='red')
plt.title('Функция 4: f(x) = {√(x+1)-√x-1/2, 0≤x≤1; e^(-x-1/x), 1<x≤2}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

def f5(x):
    result = np.full_like(x, np.nan)
    cond1 = (x >= 0) & (x <= 1.5)
    cond2 = (x > 1.5) & (x <= 3)
    result[cond1] = 2**x[cond1] - 2 + x[cond1]**2
    result[cond2] = np.sqrt(x[cond2]) * np.exp(-x[cond2]**2)
    return result

x5 = np.linspace(0, 3, 500)
y5 = f5(x5)

plt.figure()
sns.lineplot(x=x5, y=y5, linewidth=2.5, color='purple')
plt.title('Функция 5: f(x) = {2^x-2+x², 0≤x≤1.5; √x·e^(-x²), 1.5<x≤3}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

def f6(x):
    result = np.full_like(x, np.nan)
    cond1 = (x >= 0) & (x <= 1)
    cond2 = (x > 1) & (x <= 2)
    result[cond1] = 8 * x[cond1]**3 * np.cos(x[cond1])
    result[cond2] = np.log(1 + np.sqrt(x[cond2])) - np.cos(x[cond2])
    return result

x6 = np.linspace(0, 2, 500)
y6 = f6(x6)

plt.figure()
sns.lineplot(x=x6, y=y6, linewidth=2.5, color='brown')
plt.title('Функция 6: f(x) = {8x³cos x, 0≤x≤1; ln(1+√x)-cos x, 1<x≤2}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

def f7(x):
    result = np.full_like(x, np.nan)
    cond1 = (x >= -1) & (x <= 1)
    cond2 = (x > 1) & (x <= 2)
    result[cond1] = np.exp(-2 * np.sin(x[cond1]))
    result[cond2] = x[cond2]**2 - 1/np.tan(x[cond2])  # ctg x = 1/tan x
    return result

x7 = np.linspace(-1, 2, 500)
y7 = f7(x7)

plt.figure()
sns.lineplot(x=x7, y=y7, linewidth=2.5, color='pink')
plt.title('Функция 7: f(x) = {e^(-2sin x), -1≤x≤1; x²-ctg x, 1<x≤2}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

def f8(x):
    result = np.full_like(x, np.nan)
    cond1 = (x >= 0) & (x <= 0.6)
    cond2 = (x > 0.6) & (x <= 1.6)
    result[cond1] = 1 / (1 + 25 * x[cond1]**2)
    result[cond2] = (x[cond2] + 2 * x[cond2]**4) * np.sin(x[cond2]**2)
    return result

x8 = np.linspace(0, 1.6, 500)
y8 = f8(x8)

plt.figure()
sns.lineplot(x=x8, y=y8, linewidth=2.5, color='cyan')
plt.title('Функция 8: f(x) = {1/(1+25x²), 0≤x≤0.6; (x+2x⁴)sin(x²), 0.6<x≤1.6}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

def f9(x):
    result = np.full_like(x, np.nan)
    cond1 = (x >= -1.5) & (x <= 0)
    cond2 = (x > 0) & (x <= 1.5)
    result[cond1] = (x[cond1]**2 - 2 * x[cond1]**3) * np.cos(x[cond1]**2)
    result[cond2] = np.exp(np.sin(2 * x[cond2]))
    return result

x9 = np.linspace(-1.5, 1.5, 500)
y9 = f9(x9)

plt.figure()
sns.lineplot(x=x9, y=y9, linewidth=2.5, color='magenta')
plt.title('Функция 9: f(x) = {(x²-2x³)cos(x²), -1.5≤x≤0; e^(sin 2x), 0<x≤1.5}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

def f10(x):
    result = np.full_like(x, np.nan)
    cond1 = (x >= 0) & (x <= 1)
    cond2 = (x > 1) & (x <= 2)
    result[cond1] = -np.cos(np.exp(x[cond1]))
    result[cond2] = np.log(2 * x[cond2] + np.sin(x[cond2]**2))
    return result

x10 = np.linspace(0, 2, 500)
y10 = f10(x10)

plt.figure()
sns.lineplot(x=x10, y=y10, linewidth=2.5, color='olive')
plt.title('Функция 10: f(x) = {-cos(e^x), 0≤x≤1; ln(2x+sin(x²)), 1<x≤2}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

def f11(x):
    result = np.full_like(x, np.nan)
    cond1 = (x >= 0) & (x <= 1)
    cond2 = (x > 1) & (x <= 2)
    result[cond1] = x[cond1]**2 * np.arctan(x[cond1])
    result[cond2] = np.sin(1 / x[cond2])
    return result

x11 = np.linspace(0.001, 2, 500)
y11 = f11(x11)

plt.figure()
sns.lineplot(x=x11, y=y11, linewidth=2.5, color='navy')
plt.title('Функция 11: f(x) = {x²·arctg x, 0≤x≤1; sin(1/x), 1<x≤2}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

def f12(x):
    result = np.full_like(x, np.nan)
    cond1 = (x >= -2) & (x <= 0)
    cond2 = (x > 0) & (x <= 1)
    result[cond1] = x[cond1]**2 * np.sin(np.cbrt(x[cond1]) - 3)  # cbrt - кубический корень
    result[cond2] = np.sqrt(x[cond2]) * np.cos(2 * x[cond2])
    return result

x12 = np.linspace(-2, 1, 500)
y12 = f12(x12)

plt.figure()
sns.lineplot(x=x12, y=y12, linewidth=2.5, color='teal')
plt.title('Функция 12: f(x) = {x²sin(³√x-3), -2≤x≤0; √x·cos 2x, 0<x≤1}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
