import locale

locale.setlocale(locale.LC_ALL, "")


class Multiply:
    @classmethod
    def operate(cls, Val1, Val2):
        x = Val1 * Val2
        return x
