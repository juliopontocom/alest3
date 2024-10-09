# Problema do Troco
# Suponha que tenhamos disponíveis moedas com certos valores (por exemplo, de 100, 25, 10, 5 e 1). 
# O problema do troco consiste criar um algoritmo que para conseguir obter um determinado valor com o menor número de moedas ´ possível. Por exemplo, para “dar um troco” de R$2,89, a melhor solução, isto é, o menor número de moedas possível para obter o valor consiste em 10 moedas: 2 de valor 100, 3 de valor 25, 1 de valor 10 e 4 de valor 1.

# Objetivo: contrua um algorítmo que recebe a lista das moedas disponíveis e um valor, e retorna uma lista com a menor quantidade de moedas para este troco;
# Defina uma assinatura adequada para este método;
# Utiliza uma abordagem gulosa (se puder);
# Contabilize e exiba o número de iterações para cada caso de teste;
# O exercício pode ser feito em grupos de um, dois ou três elementos.



lista_de_moedas = [100,25,10,5,1]


def troco(lista_de_moedas, valor):
    troco = {}
    lista_de_moedas = sorted(lista_de_moedas)
    lista_de_moedas.reverse()
    for moeda in lista_de_moedas:
        while valor >= moeda:
            if troco.get(moeda) is None:
                troco[moeda] = 0
            troco[moeda] += 1
            valor -= moeda
            
    for moeda in troco:
        print("\n", troco[moeda], "moeda(s) de", moeda)
    
            
troco(lista_de_moedas, 289)
    
    
    
