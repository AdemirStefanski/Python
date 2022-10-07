
class Calc:
    def __init__(self, num1, num2):
        self.valora = num1
        self.valorb = num2
    def soma(self):
        return self.valora + self.valorb
    def sub(self):
        return self.valora - self.valorb
    def mult(self):
        return self.valora * self.valorb
    def div(self):
        return self.valora / self.valorb


calc = Calc(10, 2)
print('Soma: {}' .format(calc.soma()))
print('Subtração: {}' .format(calc.sub()))
print(calc.mult())
print(calc.div())



