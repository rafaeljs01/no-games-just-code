# and (e) or (ou) not (não)

entrada = input("[E]ntrar ou [S]air: ")
senha = input("Digite a senha: ")

senha_correta = "123456"

if entrada == "E" or entrada == "e" and senha == senha_correta:
    print("Você entrou no sistema.")
elif entrada == "S" or entrada == "s":
    print("Você saiu do sistema.")
