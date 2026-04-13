import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
import matplotlib.patches as mpatches

# ─── Настройка фигуры ───────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 9))
ax.set_aspect('equal')
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)
ax.axis('off')
ax.set_title('Вращающаяся чёрная дыра (Керра) | Экваториальное сечение', 
             fontsize=13, pad=20)

# ─── Физические параметры (в геометрических единицах G=c=1) ─
M = 1.0   # Масса
a = 0.85  # Параметр вращения (0 ≤ a ≤ M, здесь a=0.85M)

# Границы по метрике Керра
r_plus = M + np.sqrt(M**2 - a**2)           # Внешний горизонт событий
r_static_eq = 2 * M                         # Статический предел на экваторе
ring_radius = a                             # Радиус кольцевой сингулярности

# Масштабирование для наглядности
scale = 2.5
R_horizon = r_plus * scale
R_static_limit = r_static_eq * scale
R_ring = ring_radius * scale

# ─── 1. ЭРГОСФЕРА (фиолетовая область) ──────────────────────
# Касается горизонта на полюсах, выпирает на экваторе
ergo = Ellipse((0, 0), R_static_limit*2, R_horizon*1.8, 
               fill=True, color='purple', alpha=0.15, zorder=1)
ax.add_patch(ergo)
ergo_edge = Ellipse((0, 0), R_static_limit*2, R_horizon*1.8, 
                    fill=False, color='magenta', linestyle='--', linewidth=2, zorder=4)
ax.add_patch(ergo_edge)

# ─── 2. ГОРИЗОНТ СОБЫТИЙ ───────────────────────────────────
horizon = Circle((0, 0), R_horizon, color='black', zorder=5, 
                 edgecolor='white', linewidth=2)
ax.add_patch(horizon)

# ─── 3. КОЛЬЦЕВАЯ СИНГУЛЯРНОСТЬ ───────────────────────────
ring = Circle((0, 0), R_ring, fill=False, color='red', linewidth=2.5, zorder=6)
ax.add_patch(ring)

# ─── 4. АККРЕЦИОННЫЙ ДИСК ─────────────────────────────────
theta = np.linspace(0, 2*np.pi, 100)
for r in np.linspace(R_static_limit*0.9, 6.2, 18):
    alpha = 0.7 * (1 - (r - R_static_limit*0.9) / (6.2 - R_static_limit*0.9))
    color = (1, 0.4 + 0.6*alpha, 0)
    x = r * np.cos(theta)
    y = r * 0.22 * np.sin(theta)  # Сильно сплюснут из-за вращения
    ax.fill(x, y, color=color, alpha=alpha*0.4, edgecolor='none', zorder=2)

# ─── 5. УВЛЕЧЕНИЕ ПРОСТРАНСТВА-ВРЕМЕНИ (стрелки) ─────────
# Спиральные линии показывают, как пространство "закручивается"
for angle in [30, 120, 210, 300]:
    rad = np.radians(angle)
    t = np.linspace(0, np.pi/3, 15)
    r_arrow = 2.8
    x_spiral = r_arrow * np.cos(rad + t)
    y_spiral = r_arrow * 0.35 * np.sin(rad + t)
    ax.plot(x_spiral, y_spiral, color='cyan', linewidth=2, alpha=0.8, zorder=3)
    ax.arrow(x_spiral[-2], y_spiral[-2], 
             x_spiral[-1]-x_spiral[-2], y_spiral[-1]-y_spiral[-2],
             head_width=0.15, head_length=0.12, fc='cyan', ec='cyan', zorder=3)

# ─── Подписи ───────────────────────────────────────────────
ax.text(0, 0, 'КОЛЬЦЕВАЯ\nСИНГУЛЯРНОСТЬ', color='red', ha='center', va='center', 
        fontsize=8, fontweight='bold', zorder=7)
ax.text(R_horizon + 0.15, 0.2, 'ГОРИЗОНТ\nСОБЫТИЙ', color='white', ha='left', 
        fontsize=9, fontweight='bold', zorder=6)
ax.text(0, R_horizon*0.85, 'ЭРГОСФЕРА', color='magenta', ha='center', 
        fontsize=10, fontweight='bold', zorder=5)
ax.text(0, R_horizon*1.15, 'УВЛЕЧЕНИЕ\nИНЕРЦИАЛЬНЫХ\nСИСТЕМ ОТСЧЁТА', 
        color='cyan', ha='center', fontsize=9, fontweight='bold', zorder=4)

# ─── Легенда ───────────────────────────────────────────────
legend_elements = [
    mpatches.Patch(facecolor='purple', alpha=0.3, label='Эргосфера (можно извлечь энергию)'),
    plt.Line2D([0], [0], color='black', lw=3, label='Горизонт событий'),
    plt.Line2D([0], [0], color='red', lw=2, label='Кольцевая сингулярность'),
    plt.Line2D([0], [0], color='cyan', lw=2, label='Frame-dragging (закрутка пространства)')
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=9, framealpha=0.8)

plt.tight_layout()
plt.show()

# ─── Формулы Керра ─────────────────────────────────────────
print("🌀 ПАРАМЕТРЫ ВРАЩАЮЩЕЙСЯ ЧД (a = 0.85M)")
print("="*50)
print(f"Внешний горизонт:   r₊ = M + √(M² - a²) = {r_plus:.3f}M")
print(f"Статический предел: r_SL = 2M (на экваторе)")
print(f"Кольцевая сингулярность: радиус a = {a}M")
print()
print("⚡ ЭФФЕКТЫ:")
print("• В эргосфере невозможно оставаться неподвижным")
print("• Процесс Пенроуза: извлечение энергии вращения ЧД")
print("• Прецессия Ланзе-Тирринга: орбиты прецессируют")
print("="*50)