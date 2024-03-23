# Por: Matheus Cunha Nogueira - 06004493
JobQuant = 0
JobVal = 0
HeirQuant = 0
HeirVal = 0
LuckQuant = 0
HeirVal = 0
TotalFortune = 0
BiggestFortune = 0

for i in range(3):
    FortuneValue = float(input("Informe o valor da fortuna: "))
    FortuneOrigin = input("Informe a origem da fortuna (trabalho, herança ou sorte): ").lower()

    if FortuneOrigin == "trabalho":
        JobQuant += 1
        JobVal += FortuneValue
    elif (FortuneOrigin == "herança") or (FortuneOrigin == "heranca") :
        HeirQuant += 1
        HeirVal += FortuneValue
    elif FortuneOrigin == "sorte":
        LuckQuant += 1
        HeirVal += FortuneValue

    TotalFortune += FortuneValue

    if FortuneValue > BiggestFortune:
        BiggestFortune = FortuneValue

print("\nFortunas adiquiridas por trabalho:", JobQuant)
print("Valor da Fortuna:", JobVal)
print("\nFortunas adiquiridas por herança:", HeirQuant)
print("Valor da Fortuna:", HeirVal)
print("\nFortunas adiquiridas por sorte:", LuckQuant)
print("Valor da Fortuna:", HeirVal)
print("\nValor da soma das 2000 fortunas:", TotalFortune)
print("\nA maior fortuna é de:", BiggestFortune)