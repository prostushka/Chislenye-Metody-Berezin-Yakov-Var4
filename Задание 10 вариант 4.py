import numpy as np
import math as m


def f(x):
    return np.sin(x) - 1 + m.exp(-np.sin(x))


def f1(x, y):
    return -y * np.cos(x) + 0.5 * np.sin(2 * x)


def method_elera(x0, x1, h):
    print(f"\n--- Метод Эйлера ---")
    print(f"{'k':<3} | {'x':<5} | {'y':<10} | {'delta_y':<10} | {'y_ист':<10} | {'e':<10}")
    y0 = 0
    x = x0
    k = 0
    while x < x1 - 1e-9:
        y1 = y0 + h * f1(x, y0)  
        
        
        y_exact_next = f(x + h)
        error = y_exact_next - y1
        
        print(f"{k:<3} | {x:<5.2f} | {y1:<10.6f} | {y1-y0:<10.6f} | {y_exact_next:<10.6f} | {error:<10.6f}")
        
        k += 1
        y0 = y1
        x += h


def method_improved_elera(x0, x1, h):
    print(f"\n--- Улучшенный метод Эйлера ---")
    print(f"{'k':<3} | {'x':<5} | {'y':<10} | {'delta_y':<10} | {'y_ист':<10} | {'e':<10}")
    y0 = 0
    x = x0
    k = 0
    while x < x1 - 1e-9:
        
        y_pred = y0 + h * f1(x, y0)
        
        y1 = y0 + (h / 2) * (f1(x, y0) + f1(x + h, y_pred))
        
        y_exact_next = f(x + h)
        error = y_exact_next - y1
        
        print(f"{k:<3} | {x:<5.2f} | {y1:<10.6f} | {y1-y0:<10.6f} | {y_exact_next:<10.6f} | {error:<10.6f}")
        
        k += 1
        y0 = y1
        x += h

def method_runge_kutta(x0, x1, h):
    print(f"\n--- Метод Рунге-Кутты 4-го порядка ---")
    print(f"{'k':<3} | {'x':<5} | {'y':<10} | {'delta_y':<10} | {'y_ист':<10} | {'e':<10}")
    y0 = 0
    x = x0
    k = 0
    while x < x1 - 1e-9:
        k1 = f1(x, y0)
        k2 = f1(x + h/2, y0 + (h/2) * k1)
        k3 = f1(x + h/2, y0 + (h/2) * k2)
        k4 = f1(x + h, y0 + h * k3)
        
        y1 = y0 + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        
        y_exact_next = f(x + h)
        error = y_exact_next - y1
        
        print(f"{k:<3} | {x:<5.2f} | {y1:<10.6f} | {y1-y0:<10.6f} | {y_exact_next:<10.6f} | {error:<10.6f}")
        
        k += 1
        y0 = y1
        x += h


method_elera(0, 1, 0.1)
method_improved_elera(0, 1, 0.1)
method_runge_kutta(0, 1, 0.1)