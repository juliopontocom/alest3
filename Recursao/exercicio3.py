# Modele e implemente um método recursivo que calcule o n-ésimo número da sequência de fibonacci.

def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursivo(n-1)+ fibonacci_recursivo(n-2)

print(fibonacci_recursivo(1))
print(fibonacci_recursivo(2))
print(fibonacci_recursivo(3))
print(fibonacci_recursivo(4))
print(fibonacci_recursivo(5))
print(fibonacci_recursivo(6))
print(fibonacci_recursivo(7))
print(fibonacci_recursivo(8))
print(fibonacci_recursivo(9))
print(fibonacci_recursivo(10))
print(fibonacci_recursivo(11))
print(fibonacci_recursivo(12))