import numpy as np

def natural_cubic_spline(x, y, x_val):
    n = len(x) - 1
    h = np.diff(x)
    
    # Матрица для системы уравнений (размерность n-1)
    # Так как h одинаковый, коэффициенты 1, 4, 1
    A = np.zeros((n-1, n-1))
    b = np.zeros(n-1)
    
    # Заполняем правую часть и матрицу (внутренние узлы 1..n-1)
    for i in range(1, n):
        b[i-1] = 3 * ( (y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1] )
        A[i-1, i-1] = 2 * (h[i-1] + h[i])
        if i > 1:
            A[i-1, i-2] = h[i-1]
        if i < n-1:
            A[i-1, i] = h[i]
            
    # Решаем систему (находим c1, c2, ..., cn-1)
    c_internal = np.linalg.solve(A, b)
    c = np.zeros(n+1) # c0 = 0, cn = 0
    c[1:n] = c_internal
    
    # Находим интервал, в который попадает x_val
    interval = 0
    for i in range(n):
        if x[i] <= x_val <= x[i+1]:
            interval = i
            break
            
    # Вычисляем коэффициенты для найденного интервала
    a = y[interval]
    d = (c[interval+1] - c[interval]) / (3 * h[interval])
    b_coef = (y[interval+1] - y[interval]) / h[interval] - (h[interval] * (2 * c[interval] + c[interval+1])) / 3
    
    # Значение сплайна
    dx = x_val - x[interval]
    result = a + b_coef * dx + c[interval] * dx**2 + d * dx**3
    
    print(f"Интервал: [{x[interval]}, {x[interval+1]}]")
    print(f"Коэффициенты c: {c}")
    print(f"Уравнение на интервале: S(x) = {a:.5f} + {b_coef:.6f}*(x-{x[interval]}) + {c[interval]:.6f}*(x-{x[interval]})^2 + {d:.6f}*(x-{x[interval]})^3")
    print(f"Значение в точке X*={x_val}: {result:.6f}")

x_data = np.array([1.0, 1.9, 2.8, 3.7, 4.6])
y_data = np.array([2.4142, 1.0818, 0.50953, 0.11836, -0.24008])
X_star = 2.66666667

natural_cubic_spline(x_data, y_data, X_star)