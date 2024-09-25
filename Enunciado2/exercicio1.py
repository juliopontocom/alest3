 # Vamos começar com um algorítmo já estudado e conhecido (em AEDI). O Merge Sort é um algorítmo de ordenação baseado nos seguintes passos:

    # * recursivamente ordene a metade esquerda do vetor
    # * recursivamente ordene a metade direita do vetor
    # * mescle (faça o merge) das duas metades para ter o vetor ordenado. 
    
def merge_sort_recursivo(vetor):
   if len(vetor) <= 1:
      return vetor
   
   meio = len(vetor)//2
   esquerda = merge_sort_recursivo(vetor[:meio])
   direita = merge_sort_recursivo(vetor[meio:])
   
   return merge(esquerda, direita)

def merge(esquerda, direita):
   resultado = []
   i = 0
   j = 0
   
   while i < len(esquerda) and j < len(direita):
      if esquerda[i] <= direita[j]:
         resultado.append(esquerda[i])
         i += 1
      else:
         resultado.append(direita[j])
         j += 1
   
   resultado.extend(esquerda[i:])
   resultado.extend(direita[j:])
   return resultado

array = [12, 13, 9, 12, 12, 18, 24, 17, 32, 5, 3]
array_ordenada = merge_sort_recursivo(array)
print(array_ordenada)