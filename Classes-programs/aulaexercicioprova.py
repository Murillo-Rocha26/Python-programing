#Condicional simples (if)
#Condicional composta (if-else)
#Condicional encadeada (if-elif-else)
#Condicional alinhada (if dentro do if)

condicao1 = False
condicao2 = True
condicao3 = True
condicao4 = False
condicao5 = False
condicao6 = False

# Sempre verifica a verdadeira primeiro e depois da sequência nas outras
# Se a condição1 for verdadeira ele vai printar a primeira que é falsa
# Logo vai verificar a segunda para ver se é verdadeira
# E vai verificar a 3 se é verdadeira
# Logo vai ver a 4 e no final mostrar fora do bloco

if condicao1:
    print("Condição verdadeira")
    if condicao5:
        print("Condição verdadeira")
    else:
        print("Condição falsa")    
elif condicao2:
    print("Condição verdadeira")

elif condicao3:
    print("Condição verdadeira")

elif condicao4:
    print("Condição verdadeira")

else:
    ("Todas as outras são falsas")

print("Condições verdadeiras")