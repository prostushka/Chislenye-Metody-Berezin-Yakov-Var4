import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / math.tan(x)

def lagrange_method(x_nodes, y_nodes, x_val):
    n = len(x_nodes)
    result = 0.0
    for i in range(n):
        term = y_nodes[i]
        for j in range(n):
            if i != j:
                term *= (x_val - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result

def newton_method(x_nodes, y_nodes, x_val):
    n = len(x_nodes)
    # Создаем таблицу разделенных разностей
    coef = np.zeros([n, n])
    coef[:, 0] = y_nodes
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x_nodes[i+j] - x_nodes[i])
            
    # Вычисляем значение многочлена
    result = coef[0, 0]
    x_term = 1.0
    for j in range(1, n):
        x_term *= (x_val - x_nodes[j-1])
        result += coef[0, j] * x_term
        
    return result


# Точка интерполяции
X_star = math.pi / 3
    
# Узлы для Лагранжа (столбец а)
x_nodes_a = [math.pi/8, 2*math.pi/8, 3*math.pi/8, 4*math.pi/8]
y_nodes_a = [f(x) for x in x_nodes_a]
    
# Узлы для Ньютона (столбец б)
x_nodes_b = [math.pi/8, 5*math.pi/16, 3*math.pi/8, math.pi/2]
y_nodes_b = [f(x) for x in x_nodes_b]
    
print(f"Функция: y = ctg(x)")
print(f"Точка интерполяции X* = pi/3 ≈ {X_star:.6f}")
    
# Истинное значение
exact_val = f(X_star)
print(f"Точное значение функции в X*: {exact_val:.6f}\n")
    
# Метод Лагранжа (вариант а)
print("Интерполяция Лагранжа (вариант а)")
print("Узлы x_i:", [round(x, 5) for x in x_nodes_a])
val_lagrange = lagrange_method(x_nodes_a, y_nodes_a, X_star)
error_lagrange = abs(exact_val - val_lagrange)
print(f"Приближенное значение: {val_lagrange:.6f}")
print(f"Абсолютная погрешность: {error_lagrange:.6f}\n")
    
# Метод Ньютона (вариант б)
print("Интерполяция Ньютона (вариант б)")
print("Узлы x_i:", [round(x, 5) for x in x_nodes_b])
val_newton = newton_method(x_nodes_b, y_nodes_b, X_star)
error_newton = abs(exact_val - val_newton)
print(f"Приближенное значение: {val_newton:.6f}")
print(f"Абсолютная погрешность: {error_newton:.6f}\n")
    
print("ИТОГОВЫЕ РЕЗУЛЬТАТЫ")
print(f"Погрешность Лагранжа (а): {error_lagrange:.6f}")
print(f"Погрешность Ньютона (б):  {error_newton:.6f}")