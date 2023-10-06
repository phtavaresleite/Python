#como criar uma busca linear
def busca_linear(lista, item):
  for elemento in range(len(lista)):
    if item == elemento:
      return item
  return "não encontrado"

valor_procurado = int(input("digite o valor procurado:"))
testelista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
posição = testelista.index(valor_procurado)
print(busca_linear(testelista, valor_procurado))
print(posição)