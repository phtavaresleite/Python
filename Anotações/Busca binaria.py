def busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) -1

    while minimo <= maximo:
        
        meio = (minimo + maximo)//2
        if valor > lista[meio]:
            minimo = meio +1
        elif valor < lista[meio]:
            maximo = meio-1
        else:
            return True
        
    return False

testelista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(busca_binaria(testelista, 9))