#атрибуты человека - сытость, количество денег, количество еды, усталость
#методы - играть, есть, работать, ходить в магазин
# В общем - у них теперь общий бюджет и еда, поэтому из объектов класса убралось количество еды и денег
# Пока что я еще не знаю можно ли сделать это как-то лучще..
from termcolor import cprint

class Human:
    
    def __init__(self, name):
        self.fullness=0# сытость
        self.name=name
        self.fatique=0#усталость
        self.house = None
    
    def __str__(self):
        return f"Я {self.name}, я на столько сыт {self.fullness}, а устал {self.fatique}"
    
    def work(self):
        if (self.house.has_money == 0):
            self.house.has_money+=100
            self.fatique+=10
            self.fullness-=20
            cprint(f"Я - {self.name}, я заработал вот столько денег - {self.house.has_money}, а также устал - {self.fatique}, проголодался - {self.fullness}", color='yellow')
    
    def play(self):
        if(self.fatique > 10):
            self.fatique-=10
            cprint(f'Я - {self.name}, я отдохнул - {self.fatique}',color='cyan')    

    def shopping(self):
        if(self.house.has_money>1):
            while(self.house.has_money != 0):
                self.house.has_food+=1
                self.house.has_money-=10
            cprint(f'Я {self.name}, я купил еду - {self.house.has_food}, у меня осталось столько денег - {self.house.has_money}', color='light_blue')    
    
    def eat(self):
        if (self.fullness == 0):
            if(self.house.has_food !=0):
                self.house.has_food-=1
                self.fullness+=1
                cprint(f"{self.name} поел",color='light_red')
    
    def go_into_the_house(self, house):
        self.house=house
        cprint(f'Я {self.name} заехал в этот дом!!!!!!! {self.house}', color='blue')

    def act(self):
        self.eat()
        self.work()
        self.shopping()
        self.play()

class House:
    def __init__(self, addres):
        self.has_food=10
        self.has_money=500
        self.addres=addres
    def __str__(self):
        return f'В доме осталось столько еды - {self.has_food}, столько денег - {self.has_money}, а вот мой адрес - {self.addres}'


Andrey = Human('Andrey')
Olga=Human('Olga')
house=House('Советская 123')
Andrey.go_into_the_house(house=house)
Olga.go_into_the_house(house=house)
for day in range (1,8):
    cprint(f"================day {day}==========================",color='red')
    Andrey.act()
    Olga.act()
    print(Andrey,Olga)
    print(house)
#print(Andrey.go_into_the_house('Советская 123'))
