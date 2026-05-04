import numpy as np
import matplotlib.pyplot as plt

def f(x):
    result = np.zeros_like(x)
    
    # First part: [0, 0.25]
    mask1 = (x >= 0) & (x <= 0.25)
    result[mask1] = np.exp(np.sin(x[mask1]**2))

    # Second part: (0.25, 0.5]
    mask2 = (x > 0.25) & (x <= 0.5)
    
    # Проверка на наличие нулей во второй части (на всякий случай), 
    # хотя при x > 0.25 это безопасно.
    if np.any(x[mask2] <= 0):
        raise ValueError("Вторая часть функции требует x > 0")
        
    result[mask2] = np.exp(x[mask2]**2) - 1/(np.sqrt(x[mask2]))

    return result

# Create array
x = np.linspace(0, 0.5, 1000)
y = f(x)

# Plot graph
plt.figure(figsize=(10, 6))
plt.plot(x, y, '-g', linewidth=2, label="f(x)")

# Vertical line at junction
plt.axvline(x=0.25, color='r', linestyle='--', alpha=0.5, label='x = 0.25')

# Styling
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('График кусочной функции (разрыв в x=0.25)', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 0.5)

plt.tight_layout()
plt.show()