peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite a sua altura: ")) / 100

imc = peso / altura ** 2


if peso != '' and altura != '':
    if imc < 18.5:
        print(f'Seu IMC é de {imc}')
        print('Abaixo do peso')

    elif imc > 18.6 and imc < 24.9:
        print(f'Seu IMC é de {imc}')
        print('Peso ideal (parabéns)')

    elif imc > 25.0 and imc < 29.9:
        print(f'Seu IMC é de {imc}')
        print('Levemente acima do peso')

    elif imc > 30.0 and imc < 34.9:
        print(f'Seu IMC é de {imc}')
        print('Obesidade grau I')

    elif imc > 35.0 and imc < 39.9:
        print(f'Seu IMC é de {imc}')
        print('Obesidade grau II (Severa)')

    elif imc > 40.0:
        print(f'Seu IMC é de {imc}')
        print('Obesidade grau III')
else:
    print('Digite os dados corretamente.')