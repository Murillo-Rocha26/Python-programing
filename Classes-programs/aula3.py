"""print("------------- RECIBO DE COMPRA -------------")

nome = input("Digite o nome do cliente: ")
produto = input("Digite o nome do produto: ")

valOrig = float(input("Digite o valor do produto: "))

valDesc = float(input("Desconto aplicado: "))

valTotal = valOrig * valDesc 

print(f"Total: \t{valTotal}")

print("----------------------------------------------")"""
""""
num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
#Ex de operações
adicao = num1 + num2
subtracao = num1 - num2 
divisao = num1 / num2 
multiplicacao = num1 * num2
potenciacao = num1 ** num2
#Saida dos dados
print(f"Valor da adição: {adicao}")
print(f"Valor da subtração: {subtracao}")
print(f"Valor da divisão: {divisao: .2f}")
print(f"Valor da multiplicação: {multiplicacao}")
print(f"Valor da potência: {potenciacao}")"""

## Outros tipos de operações
# Módulo % -->> Calcula o resto da divisão
# // -->> Calcula o inteiro da divisão
"""
modulo = num1 % num2 
inteiro = num1 // num2

print(f"Valor do módulo: {modulo}")
print(f"Valor do inteiro: {inteiro}")"""

"""
nota_1 = float(input(f"Digite a nota 1: "))
nota_2 =float(input(f"Digite a nota 2: "))
nota_3 = float(input(f"Digite a nota 3: "))

soma_nota = nota_1 + nota_2 + nota_3
media = soma_nota / 3
print(f"Soma da nota: {soma_nota}")
print(f"Valor da média: {media: .1f}")"""

nota_1 = float(input(f"Digite a nota 1: "))
nota_2 =float(input(f"Digite a nota 2: "))
nota_3 = float(input(f"Digite a nota 3: "))
exercicio = 0.15
teste = 0.25
prova = 0.6

exerci_sala = nota_1 * exercicio

teste_desem = nota_2 * teste

prova = nota_3 * prova

med_final = exerci_sala + teste_desem + prova

nota_final = med_final / 3

print(f"Média final: {med_final}")
print(f"Nota final: {nota_final}")

