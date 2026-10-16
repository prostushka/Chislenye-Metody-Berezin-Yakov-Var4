import math
import numpy as np
import matplotlib.pyplot as plt


# Определяем функции
def f(x):
    """Исходная функция f(x) = x^3 + x^2 - x - 0.5"""
    return x**3 + x**2 - x - 0.5

def df(x):
    """Производная f'(x) = 3x^2 + 2x - 1 """
    return 3*x**2 + 2*x - 1

def phi(x):
    """Итерационная функция phi(x) = кубический корень из (-x^2 + x + 0.5)
    Получена из исходного уравнения: x^3 = -x^2 + x + 0.5"""
    return (-x**2 + x + 0.5)**(1/3)

def simple_iteration(x0, eps=0.0001, max_iter=100):
    print("\n--- Метод простой итерации ---")
    print(f"{'k':<5} | {'x_k':<12} | {'x_{k+1}':<12} | {'|x_{k+1} - x_k|':<15}")
    
    x = x0
    for k in range(max_iter):
        x_new = phi(x)
        diff = abs(x_new - x)
        print(f"{k+1:<5} | {x:<12.6f} | {x_new:<12.6f} | {diff:<15.6f}")
        
        if diff < eps:
            print("-" * 55)
            print(f"Сошлось за {k+1} итераций.")
            return x_new
        x = x_new
        
    print("Достигнуто максимальное количество итераций.")
    return x

def newton_method(x0, eps=0.0001, max_iter=100):
    print("\n--- Метод Ньютона (касательных) ---")
    print(f"{'k':<5} | {'x_k':<12} | {'f(x_k)':<12} | {'x_{k+1}':<12} | {'|x_{k+1} - x_k|':<15}")
    print("-" * 75)
    
    x = x0
    for k in range(max_iter):
        x_new = x - f(x) / df(x)
        diff = abs(x_new - x)
        print(f"{k+1:<5} | {x:<12.6f} | {f(x):<12.6f} | {x_new:<12.6f} | {diff:<15.6f}")
        
        if diff < eps:
            print("-" * 75)
            print(f"Сошлось за {k+1} итераций.")
            return x_new
        x = x_new
        
    print("Достигнуто максимальное количество итераций.")
    return x

if __name__ == "__main__":
    # Начальное приближение и точность
    x0 = 0.85
    eps = 0.0001
    
    print(f"Решение уравнения: x^3 + x^2 - x - 0.5 = 0")
    print(f"Начальное приближение: x0 = {x0}")
    print(f"Заданная точность: eps = {eps}")
    
    # Запуск методов
    root_si = simple_iteration(x0, eps)
    root_newton = newton_method(x0, eps)
    
    print("\n=== ИТОГОВЫЕ РЕЗУЛЬТАТЫ ===")
    print(f"Корень (Метод простой итерации): x = {root_si:.6f}")
    print(f"Корень (Метод Ньютона):          x = {root_newton:.6f}")
    print(f"Проверка f(x) для метода Ньютона: {f(root_newton):.8f}")

#Графическое изображение
x = np.linspace(0, 1, 10000)
y1 = x**3
y2 = -x**2 + x + 0.5

plt.plot(x, y1)
plt.plot(x, y2)

plt.show()