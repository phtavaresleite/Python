def soma (a,b):
    return a + b

def subtração (a,b):
    return a - b

def multiplicação (a,b):
    return a * b

def divisão (a,b):
    return a / b

print('Qual será a operação?')
print('Digite [1] para soma')
print('Digite [2] para subtração')
print('Digite [3] para multiplicação')
print('Digite [4] para divisão')

escolha = int(input('Digite o valor da opção: '))

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input ('Digite o segundo valor: '))
resultado = int(0)

if escolha == 1:
    print(soma(num1,num2))
    resultado = soma(num1,num2)
elif escolha == 2:
    print(subtração(num1,num2))
    resultado = subtração(num1,num2)
elif escolha == 3:
    print(multiplicação(num1, num2))
    resultado = multiplicação(num1,num2)
elif escolha == 4:
    print(divisão(num1,num2))
    resultado = divisão(num1,num2)