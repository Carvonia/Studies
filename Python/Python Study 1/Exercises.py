NumList = []

for i in range(0, 4):
    NumList.append(float(input('Insira um número: ')))    
NumList.sort(reverse = True)
for x in NumList:
    print(x)
