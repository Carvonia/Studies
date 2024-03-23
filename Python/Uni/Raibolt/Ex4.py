# Por: Matheus Cunha Nogueira - 06004493
NumPpl = int(input("Serão quantas pessoas no grupo? "))
AllAges = 0
BiggestAge = -1
LowestAge = float('inf')
AdultCount = 0

for i in range(NumPpl):
    Age = int(input(f"Escreva a idade da pessoa {i + 1}: "))
    AllAges += Age
    
    if Age > BiggestAge:
        BiggestAge = Age
        
    if Age < LowestAge:
        LowestAge = Age
        
    if Age >= 18:
        AdultCount += 1

media_idades = AllAges / NumPpl

print(f"Média das idades: {media_idades:.2f}")
print(f"Maior idade: {BiggestAge}")
print(f"Menor idade: {LowestAge}")
print(f"Pessoas maiores de idade: {AdultCount}")