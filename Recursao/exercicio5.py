# Modele e implemente um método recursivo que recebe um String em retorna true se este String for um palíndrome, false caso contrário.


def palindrome(palavra):
    tamanho = len(palavra)
    if tamanho == 1 or tamanho == 0:
        return "é palindrome"
    elif palavra[0] == palavra[tamanho-1]:
        nova_palavra = palavra[1:tamanho-2]
        return palindrome(nova_palavra)
    else:
        return "não é um palindrome"
    
print("palavra: julio " + palindrome("julio"))
print("palavra: ovo " + palindrome("ovo"))
print("palavra: kayak " + palindrome("kayak"))


