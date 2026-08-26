nome = input(f"Digite o seu nome: ")
print("Escolha entre os dois tipos de avaliação\n")
opcao = input("[D]isciplina [P]rojeto: ")


if opcao == "P" or opcao == "p":
        print("Método de avaliação projeto")
        exercicio = float(input("Digite a nota de seus exercícios 0 - 1.5 : "))
        teste_desem = float(input("Digite a nota de seus testes de desempenho 0 - 2.5 : "))
        prova = float(input("Digite a nota da sua prova 0 - 6 : "))

        total = exercicio + teste_desem + prova

        if total >= 6:
            print(f"{nome} está aprovado!")
        else:
            print(f"{nome} está reprovado.")


# Sempre fique de olho no or, porque precisa especificar por ex: elif opcao == "D" or "d"
# Não funciona, precisa especificar utilizando elif opcao == "D" OR == "d"
elif opcao == "D" or opcao == "d":

    print("Método de avaliação disciplina")  
    sprint1 = float(input("Digite a nota do seu sprint 0 - 1: "))
    sprint2 = float(input("Digite a nota do seu sprint 0 - 2: "))
    sprint3 = float(input("Digite a nota do seu sprint 0 - 7: "))
        
    soma = sprint1 + sprint2 + sprint3

    if soma >= 6:
        print(f"{nome} está aprovado!")
            
    else:
        print(f"{nome} está de recuperação")

print("Opção inválida!")