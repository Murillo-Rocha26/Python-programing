# Cerquilha, jogo da velha, hashtag -> Usado para fazer comentário de uma linha


print("Boa noite Pessoal!")

"""As três aspas significam DOCSTRING -> Utilizada para deixar comentários multi linha ( mais de uma linha )"""

print("AAAAAAAAAAAAAAA")

#print -> Função de saída de dados
#Dentro () ficam os argumentos

print(3, 68) #o 3 e o 68 são argumentos não nomeados

print(21, "vinte e um") # Por padrão a cada argumento tem uma vírgula que é o caractere vazio
# Argumentos nomeados



#sep -> Substituir o espaço que a "," faz 
print(19, 18, 18, 18, 18, sep="\n") # O "sep=" é um comando para substituir a vírgula - sep é um argumento 



#end -> Substitui a quebra de linha no final de cada print 
print("67, 69, 61, Frango", end=" V ")


#Tipos de dados/variável
#Tipagem dinâmica / FORTE -> Porque ele verifica automaticamente


#str (String) -> Text type
#String sempre é usada nas aspas duplas ou simples "" ''


print(1, "MURILLÂO da MASSA")


print('MURILLÃO da "MASSA"') #Tanto a barra invertida ou as aspas duplas dentro das aspas simples é usada para deixar a palavra com aspas duplas
print("MURILLÂO  da \"MASSA\"")


#\n Escape/Pula linha --> Faz a quebra de linha
print("Essa é a primeira linha \n Essa é a segunda linha")


# O \t --> Faz a tabulação horizontal (Alinhamento)
print("Professor \t\tTime")
print("Victor \tVila Nova")
print("Nelson \tPalmeiras")
print("Lucio \tSantos")
print("Emilton \t\tCorinthians")

#int -> Números inteiros
#EX. 10, 5, 94384534, 548365654, 5290543584353, -3921482395935, -1 ,667676767676767, 67

#float -> Números decimais 
#EX. 3.423453, 4.42534535, 67.342487, -32149235.6435, -5239.43 -- Sempre usando o .

#input -> Entrada de dados
#Nome de Variáveis
#Não pode: 1num - 2num
#Pode: num1, num_1, notaNum 
#Quando o nome é composto coloca sempre a primeira letra do segundo nome maiuscula 

Nome = input("Digite seu nome: ")

print(f"Seu nome é {Nome}")
