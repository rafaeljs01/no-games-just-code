frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. Python foi criado por Guido van Rossum, e lançado em 1991. '\
    'É mantido pela Python Software Foundation. É uma linguagem de programação '\
    'multiparadigma.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_quer_apareceu_mais_vezes = ''


while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_quer_apareceu_mais_vezes = letra_atual
    i += 1
print(letra_quer_apareceu_mais_vezes, qtd_apareceu_mais_vezes)

