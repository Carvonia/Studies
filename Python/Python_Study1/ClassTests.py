import locale
locale.setlocale( locale.LC_ALL, '' )

class Multiply():
    @classmethod
    def operate(self, Val1, Val2):
        x = Val1 * Val2
        return x

Employees = []

def format_currency(i):
    return locale.currency(float(i), grouping=True)

print(format_currency(10))