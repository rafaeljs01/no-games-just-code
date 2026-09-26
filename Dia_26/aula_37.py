contador = 0

while contador < 100:
    contador += 1
    print('Contador: ', contador)

    if contador == 6:
        print('Não vou imprimir o 6')
        continue

    print('Contador: ', contador)

    if contador == 40:
        break


print('Acabou')    