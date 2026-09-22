numero = (input('Digite um número: '))

if numero.is_integer():
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')

else:
    print('Isso não é um número inteiro!')