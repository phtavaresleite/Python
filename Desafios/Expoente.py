def expoente(a,b):
    r = a ** b
    return r

a = int(input('Digite a base: '))
b = int(input('Digite o expoente: '))

if a >= 0 and b >= 0:
    print(expoente(a,b))
