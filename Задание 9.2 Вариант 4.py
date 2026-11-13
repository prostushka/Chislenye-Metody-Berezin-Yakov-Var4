def y_c(a, b):
    c = (a+b)/2

    return (3*c + 4)/(2*c + 7)

def y(a):

    return (3*a + 4)/(2*a + 7)

def method_pryamougol(h, x_i):
    sum = 0
    while x_i != 2:
        x_i1 = x_i + h
        sum += y_c(x_i, x_i1)
        x_i = x_i1
    return  sum*h

def method_trapez(h, x_i):
    sum = 0
    while x_i != 2:
        x_i1 = x_i + h
        sum += y(x_i) + y(x_i1)
        x_i = x_i1
    return h*sum/2

def method_simpsona(h, x_i):
    sum = 0
    while x_i != 2:
        x_i1 = x_i + h
        x_i2 = x_i1 + h
        sum += y(x_i) + 4*y(x_i1) + y(x_i2)
        x_i = x_i2
    return h*sum/3

print(f"Решение методом прямоугольников с шагом 1: {method_pryamougol(1, -2)} с шагом 0,5: {method_pryamougol(0.5, -2)}")
print(f"Решение методом трапеций с шагом 1: {method_trapez(1, -2)} с шагом 0,5: {method_trapez(0.5, -2)}")
print(f"Решение методом Симпсона с шагом 1: {method_simpsona(1, -2)} с шагом 0,5: {method_simpsona(0.5, -2)}")

print("\n Уточнение по Рунге-Ромберга")

#Для метода прямоугольников
R1 = method_pryamougol(1, -2)
R2 = method_pryamougol(0.5, -2)
R_ref = R2 + (R2 - R1) / 3
print(f"Метод прямоугольников (уточненный): {R_ref:.6f}")

#Для метода трапеций
T1 = method_trapez(1, -2)
T2 = method_trapez(0.5, -2)
T_ref = T2 + (T2 - T1) / 3
print(f"Метод трапеций (уточненный): {T_ref:.6f}")

#Для метода Симпсона
S1 = method_simpsona(1, -2)
S2 = method_simpsona(0.5, -2)
S_ref = S2 + (S2 - S1) / 15
print(f"Метод Симпсона (уточненный): {S_ref:.6f}")