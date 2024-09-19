#  Modele e implemente um método recursivo que calcule o somatório de um número n (passado como parâmetro) até 0.

def somatorio_recursivo(n):
    if n == 0:
        return n
    else:
        return n + somatorio_recursivo(n-1)

print(somatorio_recursivo(1))
print(somatorio_recursivo(2))
print(somatorio_recursivo(3))
print(somatorio_recursivo(4))
print(somatorio_recursivo(5))
print(somatorio_recursivo(6))
print(somatorio_recursivo(7))
print(somatorio_recursivo(8))
print(somatorio_recursivo(9))
print(somatorio_recursivo(10))