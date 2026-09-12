# and (e) or (ou) not (não)

entrada = input("[E]ntrar ou [S]air: ")
senha = input("Digite a senha: ")

senha_correta = "123456"

if entrada == "E"  and senha == senha_correta:
    print("Você entrou no sistema.")
elif entrada == "S":
    print("Você saiu do sistema.")
