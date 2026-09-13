#Operadores in e not in
# Strings são iteráveis

# nome = "Rafael"
# print(nome[2])
# print(nome[-4])

# print("a" in nome)
# print("b" in nome)
# print(10 * '-')
# print("a" not in nome)
# print("b" not in nome)

nome = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"'{encontrar}' foi encontrado em '{nome}'")
else:
    print(f"'{encontrar}' não foi encontrado em '{nome}'")