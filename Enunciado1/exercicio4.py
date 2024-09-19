# Modele e implemente um método recursivo que calcule o somatório dos números inteiros entre os números k e j, passados como parâmetro.
# enunciado

def somatorio_intervalo_recursivo(k, j):
    if k > j:
        somatorio_intervalo_recursivo(j, k)
    elif k+1 == j-1:
        return k+1
    elif k == j:
        return 0
    else:
        return j-k + somatorio_intervalo_recursivo(k, j-1)
        

print(somatorio_intervalo_recursivo(1, 2))
print(somatorio_intervalo_recursivo(1, 3))
print(somatorio_intervalo_recursivo(1, 4))
print(somatorio_intervalo_recursivo(1, 5))
print(somatorio_intervalo_recursivo(1, 6))
print(somatorio_intervalo_recursivo(1, 7))
print(somatorio_intervalo_recursivo(1, 8))
print(somatorio_intervalo_recursivo(1, 9))
print(somatorio_intervalo_recursivo(1, 10))