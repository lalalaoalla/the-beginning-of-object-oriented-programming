# Базовый класс - Машина,
# имеет
#   кол-во топлива
# может
#   заправляться
class Car:
    def __init__(self,model):
        self.model=model# пускай есть какая-то
        self.fuel=0#по умолчанию количество нашего топлива такое
    def __str__(self):
        return f'{self.model}, количество топлива - {self.fuel}'
    def refill(self):
        ''' Функция заправления '''
        self.fuel+=1000
# car=Car('Nissan Terrano')
# print(car)