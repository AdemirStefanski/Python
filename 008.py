class Tv:
    def __init__(self):
        self.ligada = False
        self.canal = 2
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def canalup(self):
        self.canal += 1

    def canaldw(self):
        self.canal -= 1

tv = Tv()
print('Televisão ligada: {}' .format(tv.ligada))
tv.power()
print('Televisão ligada: {}' .format(tv.ligada))

print('\nCanal atual: {}' .format(tv.canal))
tv.canalup()
tv.canalup()
print('Canal atual: {}' .format(tv.canal))