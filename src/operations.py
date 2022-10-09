from math import log

# Calcula el total de operaciones por hora que puede realizar una computadora
# dependiendo de la complejidad del algoritmo

total_operations_xhour = float(3.6*10**13)

def square_root(total_operations):
    largest_input = pow(total_operations,(1/2))
    return largest_input

def cube_root(total_operations):
    largest_input = pow(total_operations,(1/3))
    return largest_input

def ahundred_sqrt_root(total_operations):
    largest_input = pow((total_operations/100),(1/2))
    return largest_input

def two_pow2(total_operations):
    largest_input = (log(total_operations))/(log(2))
    return largest_input

def two_pow_two_n(total_operations):
    # Algoritmo con complejidad 2^(2^n)
    largest_input = log((log(total_operations))/(log(2)))/(log(2))
    return largest_input

print("n^2: ", square_root(total_operations_xhour))
print("n^3: ", cube_root(total_operations_xhour))
print("100n^2: ", ahundred_sqrt_root(total_operations_xhour))
print("2^n: ", two_pow2(total_operations_xhour))
print("2^(2^n): ",two_pow_two_n(total_operations_xhour))
