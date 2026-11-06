import numpy as np
import matplotlib.pyplot as plt

def least_squares_approximation():
    # Исходные данные
    x = np.array([1.0, 1.9, 2.8, 3.7, 4.6, 5.5])
    y = np.array([2.4142, 1.0818, 0.50953, 0.11836, -0.24008, -0.66818])
    n = len(x)

    print("--- Метод наименьших квадратов ---")
    
    #1. Линейная аппроксимация P1(x) = a0 + a1*x
    # Составляем матрицу системы
    A1 = np.array([
        [n, np.sum(x)],
        [np.sum(x), np.sum(x**2)]
    ])
    B1 = np.array([np.sum(y), np.sum(x * y)])
    
    # Решаем систему
    a = np.linalg.solve(A1, B1)
    P1 = lambda x_val: a[0] + a[1] * x_val
    
    # Считаем ошибку
    Phi1 = np.sum((y - P1(x))**2)
    
    print("\n Линейная аппроксимация")
    print(f"Уравнение: P1(x) = {a[0]:.4f} + {a[1]:.4f} * x")
    print(f"Сумма квадратов ошибок (Phi1): {Phi1:.6f}")

    # 2. Квадратичная аппроксимация P2(x) = b0 + b1*x + b2*x^2
    # Составляем матрицу системы
    A2 = np.array([
        [n, np.sum(x), np.sum(x**2)],
        [np.sum(x), np.sum(x**2), np.sum(x**3)],
        [np.sum(x**2), np.sum(x**3), np.sum(x**4)]
    ])
    B2 = np.array([np.sum(y), np.sum(x * y), np.sum(x**2 * y)])
    
    # Решаем систему
    b = np.linalg.solve(A2, B2)
    P2 = lambda x_val: b[0] + b[1] * x_val + b[2] * x_val**2
    
    # Считаем ошибку
    Phi2 = np.sum((y - P2(x))**2)
    
    print("\n Квадратичная аппроксимация")
    print(f"Уравнение: P2(x) = {b[0]:.4f} + {b[1]:.4f}*x + {b[2]:.4f}*x^2")
    print(f"Сумма квадратов ошибок Phi2: {Phi2:.6f}")
    
    if Phi2 < Phi1:
        print("\nВывод: Квадратичная аппроксимация точнее Phi2 < Phi1.")
    else:
        print("\nВывод: Линейная аппроксимация точнее.")

    # ГРАФИЧЕСКОЕ ИЗОБРАЖЕНИЕ
    x_plot = np.linspace(min(x) - 0.5, max(x) + 0.5, 100)
    y_plot_P1 = P1(x_plot)
    y_plot_P2 = P2(x_plot)

    plt.figure(figsize=(10, 6))
    
    # Исходные точки
    plt.plot(x, y, 'ko', markersize=4, label='Исходные данные y_i')
    
    # Аппроксимации
    plt.plot(x_plot, y_plot_P1, 'b--', label=f'Линейная: P_1(x)')
    plt.plot(x_plot, y_plot_P2, 'r-', label=f'Квадратичная: P_2(x)')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Аппроксимация табличной функции методом МНК')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

least_squares_approximation()