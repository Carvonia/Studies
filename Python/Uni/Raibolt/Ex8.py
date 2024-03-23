# Por: Matheus Cunha Nogueira - 06004493
SellsType1 = 0
SellsType2 = 0
SellsType3 = 0
ValType1 = 0
ValType2 = 0
ValType3 = 0
TotalSold = 0
BiggestSold = 0
BiggestType = 0

for i in range(1000):
    ProdType = int(input("Digite o tipo do produto (1, 2 ou 3) para realizar a venda: "))
    SellValue = float(input(f"Informe o valor da venda do produto{ProdType}: "))

    if ProdType == 1:
        SellsType1 += 1
        ValType1 += SellValue
    elif ProdType == 2:
        SellsType2 += 1
        ValType2 += SellValue
    elif ProdType == 3:
        SellsType3 += 1
        ValType3 += SellValue

    TotalSold += SellValue

    if SellValue  > BiggestSold:
        BiggestSold = SellValue
        BiggestType = ProdType

print("Vendas do Produto 1:", SellsType1)
print("Vendas do Produto 2:", SellsType2)
print("Vendas do Produto 3:", SellsType3)
print("Valor total vendido do Produto 1:", ValType1)
print("Valor total vendido do Produto 2:", ValType2)
print("Valor total vendido do Produto 3:", ValType3)
print("Valor total vendido na loja:", TotalSold)
print(f"A maior venda foi de {BiggestSold} do produto {BiggestType}!")