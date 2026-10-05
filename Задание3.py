x1 = 0.0
x2 = 0.0
x3 = 0.0
x4 = 0.0

epsilon = 0.01

error = 1.0
k = 0

while error > epsilon:
    x1_old, x2_old, x3_old, x4_old = x1, x2, x3, x4
    
    x1 = (20 + 9*x2 + 8*x3 - 8*x4) / 26.0
    x2 = (164 + 9*x1 - 2*x3 + 8*x4) / 21.0
    x3 = (-140 - 3*x1 + 2*x2 + 8*x4) / 18.0
    x4 = (-81 - x1 + 6*x2 + x3) / 11.0
    
    error = max(abs(x1 - x1_old), abs(x2 - x2_old), 
                abs(x3 - x3_old), abs(x4 - x4_old))
    
    k += 1
    print(f"Итерация {k}: x = [{x1:.5f}, {x2:.5f}, {x3:.5f}, {x4:.5f}], погрешность = {error:.5f}")

print(f"Сошлось за {k} итераций с точностью {epsilon}.\n")
print("Ответ:")
print(f"x1 = {x1:.5f}")
print(f"x2 = {x2:.5f}")
print(f"x3 = {x3:.5f}")
print(f"x4 = {x4:.5f}")