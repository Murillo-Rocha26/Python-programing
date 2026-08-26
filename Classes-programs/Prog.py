total = int
desconto = float
total_pago = float

print("----- RECIBO DE COMPRA -----")

input("Insira o nome do cliente: ")
produto = input(f"Insira o nome do produto: ")
print("Valor original R$25.00")
desconto = float(input("Valor do desconto: "))

total_pago = total * desconto

print("Valor total: ")