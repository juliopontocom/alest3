eventos = [
    {'inicio': 4, 'fim': 8},
    {'inicio': 6, 'fim': 7},
    {'inicio': 13, 'fim': 14},
    {'inicio': 4, 'fim': 5},
    {'inicio': 2, 'fim': 4},
    {'inicio': 6, 'fim': 9},
    {'inicio': 7, 'fim': 10},
    {'inicio': 9, 'fim': 11},
    {'inicio': 1, 'fim': 6},
    {'inicio': 3, 'fim': 13},
    {'inicio': 9, 'fim': 12} 
]


def escalonamento(eventos):
    eventos = ordena_eventos(eventos)
    horarios = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    eventos_selecionados= []from django.utils.translation import ugettext_lazy as _
    
    for evento in eventos:
        if verifica_disponibilidade(evento, horarios):
    print(eventos)
    return 1


escalonamento(eventos)


def ordena_eventos(eventos):
    for evento in eventos:
        evento['tamanho'] = evento['fim'] - evento['inicio']     
    eventos = sorted(eventos, key=lambda d: d['tamanho'])
    return eventos

def verifica_disponibilidade(evento, horarios):
    inicio = evento['inicio']
    fim = evento['fim']
    
    while inicio < fim:
        if horarios[inicio] == 0:
            continue
        else:
            return false
        inicio += 1
    
    return true

def preenche_horarios(inicio, fim, horarios):
    while inicio < fim:
        horarios[inicio] = 1
        inicio +=1
        
    return horarios
        
    