# Por: Matheus Cunha Nogueira - 06004493
import random

RandNum = random.randint(1, 100)
Tries = 0

print("O objetivo deste jogo é adivinhar um número de 1 a 100 em apenas 10 tentativas!")
while Tries < 10:
    Guess = int(input(f"Tentativa atual: {Tries + 1}/10 \nDigite um número: "))

    Tries += 1
    
    if Tries == 10:
        print("Você perdeu! Acabaram as suas tentativas...")
        break
    
    if Guess == RandNum:
        print(f"Parabéns! Você adivinhou o número em {Tries + 1} tentativas.")
        break
    
    elif Guess < RandNum:
        print("Tente de novo, o número é maior.")
        
    else:
        print("Tente de novo, o número é menor.")


