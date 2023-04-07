class Multiply():
    @classmethod
    def operate(self, Val1, Val2):
        x = Val1 * Val2
        return x

Numbers = []
for i in range(0, 2):
    while True:
        try:
            Numbers.append(int(input('Type a number please: ')))
            break
        except ValueError:
            print('Only numbers are allowed! \n')
        

operation = Multiply.operate(Numbers[0], Numbers[1])
print(f'\nThe result of the operation is: {operation}')