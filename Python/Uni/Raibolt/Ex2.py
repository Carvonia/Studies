# Por: Matheus Cunha Nogueira - 06004493
import random

MaxNum = 0
for i in range(100):
    RandNum = random.randint(1, 1000)
    if RandNum > MaxNum:
        MaxNum = RandNum

print("O maior valor entre os números que foram sorteados é:", MaxNum)