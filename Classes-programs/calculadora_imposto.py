salario = float(input("Insira o valor do seu salário atual: "))
sal_imposto = float()
sal_novo = float()

sal_novo = salario - (salario*sal_imposto)

if salario < 1903.98:
    print("Insento de imposto")
elif  1903.99 > salario == 2826.65:
    print("Alíquota de 7.5%")
    sal_imposto = salario * 0.075
elif 2826.66 > salario == 3751.05:
    print("Alíquota de 15%")
    sal_imposto = salario * 0.15
elif 2826.65 > salario == 3751.05:
    print("Alíquota de 22.5%")
    sal_imposto = salario * 0.225
else:
    sal_imposto = salario * 0.275

sal_novo = salario - sal_imposto

print(f"Salário: {sal_novo}")