# Itera realiza o calculo das sequencias da loteria.
def itera(iterable,cel):
# Transforma a lista em uma tupla.
    info = tuple(iterable)
# Informa o tamanho total da lista.
    n = len(info)
# Se o número de células forem maior que o tamanho total da lista, return 0.
    if cel > n:
        return
# Cria um indice de 1 á número total da celula    .
    indices = list(range(cel))
# Armazena posição, para dar continuidade.
    yield tuple(info[i] for i in indices)
# Entra no laço
    while True:
    # Verifica se o valor final da lista é igual o valor atual a ser informado.
        for i in reversed(range(cel)):
            if indices[i] != i + n - cel:
                break# Se for igual, fecha o While.
        else:#Se não, return 0(Else do for).
            return
        # Icrementa "+1" ao valor final da célula.
        indices[i] += 1
        # Realiza o icremento nos outros indices da célula.
        for j in range(i+1,cel):
            indices[j]=indices[j-1]+1
        yield tuple(info[i] for i in indices)

        
# Função que descobre o valor total de sequencias.        
def calculo(lista,cel):
    fat, fat2 = 1
    
    for i in reversed(range(cel)):
        apoio = (i + n) - (cel + 1)
        fat = apoio*fat
        fat2 = (i + 1) * fat2
        result = fat / fat2
        return result