def ordenação_lista(lista):
    n = len(lista)
    for i in range(0, n):
        index_menor = 1
        for j in range(i+1, n):
            if lista[j] < lista[index_menor]:
                index_menor = 1
            lista[i], lista[index_menor] = lista[index_menor], lista[i]
        return lista
    
lista = [10,9,6,1,5,2]
print(ordenação_lista((lista)))