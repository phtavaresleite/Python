import random

numero_aleatorio = random.randint(1,10)
ganhou = False

while ganhou != True:
    n = int(input("Digite um valor de 1 a 10: "))
    if n > numero_aleatorio:
        print("Chutou alto")
    elif n < numero_aleatorio:
        print("Chutou baixo")
    else:
        print("Acertou")
        ganhou = True