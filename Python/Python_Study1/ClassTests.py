import locale
locale.setlocale( locale.LC_ALL, '' )

class Multiply():
    @classmethod
    def operate(self, Val1, Val2):
        x = Val1 * Val2
        return x

#text_model = 'The {} is {}!\n'
#def form(*args, **kwargs):
#    sum = 0
#    for key,value in kwargs.items():
#        print(text_model.format(key,value))
#    for i in args:
#        sum += i
#    return sum
        
#print(form(1, 2, 3, 4, Cat='Cute', Dog='Happy', Parrot='Singing'))

Employees = []

def format_currency(i):
    return locale.currency(float(i), grouping=True)

print(format_currency(10))