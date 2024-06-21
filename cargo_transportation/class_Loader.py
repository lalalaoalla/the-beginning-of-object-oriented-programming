# Погрузчик (производный от Машина)
# имеет
#   скорость погрузки, расход топлива в час при работе
# может
#   загружать/разгружать грузовик
#   ждать грузовик
from class_Car import Car
from class_Truck import Truck

class Loader(Car):
    def __init__(self,model, warehouse=None, possible_load=100, role='Losder'):# также модель, склад, возможная нагрузка(за один раз сколько поднимает) загружатель\разгружатель
        super().__init__(model=model)
        self.warehouse=warehouse
        self.possible_load=possible_load
        self.role=role
        self.load_speed=1000#в час он может перенести вес в 1000 кг
        self.consumption=1# в час он тратит 1л топлива
        self.truck = None #текущий загружаемый грузовик
    def __str__(self):
        res=super().__str__()
        return res + f'мой склад - {self.warehouse}, максимальная загрузка за раз - {self.possible_load}, моя скорость {self.load_speed}, трачу топлива - {self.consumption}, сейчас за гружаю этот грузовик {self.truck}'
    
    def load(self):
        count_load=self.truck.body_space - self.truck.cargo
        if count_load <= self.possible_load:
            self.warehouse.content-=self.possible_load#берем из содержимого склада
            self.truck.cargo+=self.possible_load
        else:
            #ну типа берем сколько осталось и докладываем в грузовик да
            self.warehouse.content-=count_load
            self.truck.cargo+=count_load
    def unload(self):
        if self.truck.cargo >= self.possible_load:
            self.warehouse.content+=self.possible_load#кладем на склад
            self.truck.cargo-=self.possible_load
        else:
            #ну типа берем сколько осталось и докладываем на склад да
            self.truck.cargo-=self.truck.cargo
            self.warehouse.content+=self.truck.cargo
    
    def act(self):
        if (self.fuel <=5):
            self.refill()
        elif(self.role=='Loader'):
            self.load()
        elif(self.truck is None):
            self.truck=self.warehouse.get_the_next_truck()# функция из класса Склад
        elif(self.role='Unloader'):
            self.unload()
        
        