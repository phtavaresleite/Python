valor_produto = float(200)

codigo_promocional = input("Digite o seu código promocional:" )

if codigo_promocional == "VBFMZB":
    valor_desconto = valor_produto-valor_produto*0.25
    print(valor_desconto)
elif codigo_promocional == "HT2Y8E" :
    valor_desconto = valor_produto-valor_produto*0.25
    print(valor_desconto)
else:
   print(valor_produto)