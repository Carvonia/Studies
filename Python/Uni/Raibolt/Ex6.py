# Por: Matheus Cunha Nogueira - 06004493
ManAge = 0
WomanAge = 0
LessThanTwoYears = 0
TotalCouples = 2500

for _ in range(TotalCouples):
    AgeBoyfriend = int(input("Informe a idade do namorado: "))
    AgeGirlfriend = int(input("Informe a idade da namorada: "))
    RelationTime = int(input("Informe o tempo de namoro em anos: "))

    ManAge += AgeBoyfriend
    WomanAge += AgeGirlfriend

    if RelationTime < 2:
        LessThanTwoYears += 1


AverageMan = ManAge / TotalCouples
AverageWoman = WomanAge / TotalCouples

print("Média de idade entre os homens:", AverageMan)
print("Média de idade entre as mulheres:", AverageWoman)
print("Quantidade de casais com menos de 2 anos de namoro:", LessThanTwoYears)