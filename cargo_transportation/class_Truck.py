# Грузовик (производный от Машина)
# имеет
#   емкость кузова, скорость движения, расход топлива за час поездки
# может
#   стоят под погрузкой/разгрузкой
#   ехать со скоростью

from class_Car import Car
from termcolor import cprint

class Truck(Car):

    def __init__(self, model,body_space=1000):#объем кузова по умолчанию тонна
        super().__init__(model=model)# здесь еще стоит пересмотреть, зачем нам именно брать модель из Car
        self.body_space=body_space
        self.speed=100#да он гонщик нереальный
        self.cargo = 0#по умолчанию он идет пустой
        self.expenditure=10# по умолчанию он тратит 10 литров на 100 км
        self.place= None# где мы находимся чтобы если что знать
        self.distance_to_target=0# расстояние до цели

    def __str__(self):
        res=super().__str__()#типа чтоб возвращало из базового класса что есть
        return res+ f'Я еду со скоростью {self.speed}, мой груз {self.cargo}, моя вместимость {self.body_space}, расход {self.expenditure}'
    
    def go_to(self,road):
        self.place=road
        self.distance_to_target=road.distanse#типа осталась вся дистанция
        cprint(f'{self.model} выехал, едет по дороге {self.place}',color='yellow')

    def ride(self):
        if (self.distance_to_target>self.speed):
            self.distance_to_target-=self.speed
        cprint(f'{self.model} едет расстояние {self.distance_to_target}', color='light_yellow')
    
    def act(self):
        if (self.fuel <= 10):
            self.refill()
        elif isinstance(self.place,Road):#типа если место является дорогой, то я еду
            self.ride()
        