import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

# 1. Определяем функцию №3
def f3(x):
    # Инициализируем массив NaN
    result = np.full_like(x, np.nan)
    
    # Условие 1: 0 <= x <= 1
    # f(x) = cos(x) * e^(-x^2)
    cond1 = (x >= 0) & (x <= 1)
    result[cond1] = np.cos(x[cond1]) * np.exp(-x[cond1]**2)
    
    # Условие 2: 1 < x <= 2
    # f(x) = ln(x+1) - sqrt(4-x^2)
    cond2 = (x > 1) & (x <= 2)
    result[cond2] = np.log(x[cond2] + 1) - np.sqrt(4 - x[cond2]**2)
    
    return result

# 2. Генерируем данные
# 500 точек от 0 до 2
x_values = np.linspace(0, 2, 500)
y_values = f3(x_values)

# 3.график Plotly
fig = go.Figure()

# Добавляем линию графика
fig.add_trace(go.Scatter(
    x=x_values, 
    y=y_values, 
    mode='lines', 
    name='График функции 3',
    line=dict(color='#0000FF', width=3) # Синяя линия
))

# 4.внешний вид
fig.update_layout(
    title={
        'text': "Интерактивный график функции №3",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title="x",
    yaxis_title="f(x)",
    hovermode="x unified", # Показывает координаты при наведении
    template="plotly_white",
    font=dict(family="Arial", size=14)
)

pio.write_html(fig, file='function_3_graph.html', auto_open=True, include_plotlyjs='cdn')