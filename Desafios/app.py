valor_produto = float(200)
codigo_promocional = input("Digite o seu código promocional:" )

Cupons = ["VBFMZB","HT2Y8E"]

if codigo_promocional.upper() in Cupons:
    valor_desconto = valor_produto-valor_produto*0.25
    print(valor_desconto)
else:
   print(valor_produto)