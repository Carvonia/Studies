
class Multiply():
    def __init__(self, Val1, Val2):
        self.Val1 = Val1
        self.Val2 = Val2

    @classmethod
    def ChangeShop(cls, ShopName):
        cls.ShopName = ShopName

    def operate(self):
        print(self.Val1 * self.Val2)

Numbers = []
for i in range(0, 2):
    Numbers.append(int(input('Type a number please: ')))

operation = Multiply(Numbers[0], Numbers[1])
operation.operate()