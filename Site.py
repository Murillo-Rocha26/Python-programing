import random

number = random.randint(0, 100)

print(number)

guess = int(input("Selecione um número de 0 á 100: "))

guess = int

if guess == number:
    print("Parabéns você acertou!")

else:
    print(f"Tente novamente. O número era: {number}.")