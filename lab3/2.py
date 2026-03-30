import numpy as np
import matplotlib.pyplot as plt

# (вариант 2) определение кусочной функции
def f(x):
    result = np.zeros_like(x)
# frist part
    mask1 = (x >= 0) & (x <= 0.25)
    result[mask1] = np.exp(np.sin(x[mask1]**2))

#second part

    mask2 = (x > 0.25) & (x <= 0.5)
    result[mask2] = np.exp(x[mask2]**2) - 1/(x[mask2]**0.5)

    return result

#make massive

x = np.linspace(0, 0.5, 1000)
y = f(x)

#make graf
plt.figure(figsize = (10, 6))
plt.plot(x, y,'-g', linewidth = 2, label = "f(x)" )

# point

plt.axvline(x=0.25, color='r', linestyle='--', alpha=0.5, label='x = 0.25')

#styling
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('График кусочной функции', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 0.5)

# showw
plt.tight_layout()
plt.show()



