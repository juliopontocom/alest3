# Modele e implemente um método recursivo que calcule o fatorial de um número n passado como parâmetro.

def fatorial_recursivo(n):
    if n == 1 or n == 0:
        return n
    else:
        return n * fatorial_recursivo(n-1)

print(fatorial_recursivo(1))
print(fatorial_recursivo(2))
print(fatorial_recursivo(3))
print(fatorial_recursivo(4))
print(fatorial_recursivo(5))
print(fatorial_recursivo(6))
print(fatorial_recursivo(7))