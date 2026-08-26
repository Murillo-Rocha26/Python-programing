nome = input("Digite seu nome: ")
saldo = float(input("Digite o valor a ser utilizado: "))

def exibir_opcoes():
    print("Opção 1: Ver saldo\n")
    print("Opção 2: Saque\n")
    print("Opção 3: Depósito\n")
    print("Opção 4: Sair\n")

def ver_saldo():
    print(f"Seu saldo é de: {saldo}")

def sacar_saldo():
    print(f"Saque de: {saldo}")

def depositar_saldo():
    print(f"Depositar valor de: {saldo}")

def encerrar_programa():
    voltar_menu_principal()

def voltar_menu_principal():
    return exibir_opcoes()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Digite uma opção: "))
    
        if opcao_escolhida == 1:
            ver_saldo()
        elif opcao_escolhida == 2:
            sacar_saldo()
        elif opcao_escolhida == 3:
            depositar_saldo()
        else:
            encerrar_programa()
    except ValueError:
        print("Opção inválida!")
    return True


def main():
    while True:
        exibir_opcoes()

        continuar = escolher_opcoes()

        if not continuar:
            break

if __name__ == '__main__':
    main()