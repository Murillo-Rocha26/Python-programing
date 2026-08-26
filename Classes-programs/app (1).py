print("--------- LOGIN DO SISTEMA ----------")
print("Escolha uma opção desejada")
opcao = input("[S]aida /// [E]ntrada\n")

senha = int(input("Digite a senha: "))

senha_correta = 26122007

# Condição AND todas precisam ser verdadeira

if opcao == "E" or "e": # Pode se fazer if (opcao == E or e) and senha == senha_correta está certo também
    print("Entrando no sistema")
    if senha == senha_correta:
        print("Senha correta!")
        print("------ SISTEMA DE LOGIN ------")
    else:
        print("Senha errada.")
        print("Saindo do sistema...")


