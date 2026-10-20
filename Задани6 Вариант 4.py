import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, cos, log, lambdify

x1, x2 = symbols("x1 x2")


df1x1 = diff(x1 - cos(x2) - 1, x1)
df1x2 = diff(x1 - cos(x2) - 1, x2)
df2x1 = diff(x2 - log(x1 + 1, 10) - 1, x1) 
df2x2 = diff(x2 - log(x1 + 1, 10) - 1, x2)

def f1(x1, x2):
    return x1 - math.cos(x2) - 1

def f2(x1, x2):
    return x2 - math.log10(x1 + 1) - 1


df1_dx1 = lambdify((x1, x2), df1x1, modules='math')
df1_dx2 = lambdify((x1, x2), df1x2, modules='math')
df2_dx1 = lambdify((x1, x2), df2x1, modules='math')
df2_dx2 = lambdify((x1, x2), df2x2, modules='math')


#метод Ньютона
def newton_method(x10, x20, eps=0.0001):
    print("\n--- Метод Ньютона ---")
    print(f"{'k':<5} | {'x1_k':<12} | {'x2_k':<12} | {'f1(x_k)':<12} | {'f2(x_k)':<12} | {'x1_{k+1}':<12} | {'x2_{k+1}':<12}")
    print("-" * 90)

    x1_val = x10
    x2_val = x20
    
    for k in range(-1, 100): 
        
    
        A1 = np.array([
            [f1(x1_val, x2_val), df1_dx2(x1_val, x2_val)],
            [f2(x1_val, x2_val), df2_dx2(x1_val, x2_val)]
        ])
        A2 = np.array([
            [df1_dx1(x1_val, x2_val), f1(x1_val, x2_val)],
            [df2_dx1(x1_val, x2_val), f2(x1_val, x2_val)]
        ])
        J = np.array([
            [df1_dx1(x1_val, x2_val), df1_dx2(x1_val, x2_val)],
            [df2_dx1(x1_val, x2_val), df2_dx2(x1_val, x2_val)]
        ])
        
        det_J = np.linalg.det(J)
        x1_new = x1_val - np.linalg.det(A1) / det_J
        x2_new = x2_val - np.linalg.det(A2) / det_J
        
        print(f"{k+1:<5} | {x1_val:<12.6f} | {x2_val:<12.6f} | {f1(x1_val, x2_val):<12.6f} | {f2(x1_val, x2_val):<12.6f} | {x1_new:<12.6f} | {x2_new:<12.6f}")
        
        if abs(x1_new - x1_val) < eps and abs(x2_new - x2_val) < eps:
            print("-" * 90)
            print(f"Сошлось за {k+1} итераций.")
            return x1_new, x2_new
            
        x1_val = x1_new
        x2_val = x2_new
        
    print("Достигнуто максимальное количество итераций.")
    return x1_val, x2_val

x10 = 1.2
x20 = 1.4
eps = 0.0001
    
print(f"Решение системы уравнений:")
print(f"x1 - cos(x2) - 1 = 0")
print(f"x2 - lg(x1 + 1) - 1 = 0")
print(f"Начальное приближение: x10 = {x10}, x20 = {x20}")
print(f"Заданная точность: eps = {eps}")
    
# Запуск методов
root_newton = newton_method(x10, x20, eps)
    
print("\n=== ИТОГОВЫЕ РЕЗУЛЬТАТЫ ===")

print(f"x1 = {root_newton[0]:.6f}")
print(f"x2 = {root_newton[1]:.6f}")