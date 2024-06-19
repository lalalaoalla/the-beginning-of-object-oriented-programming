#атрибуты человека - сытость, количество денег, количество еды, усталость
#методы - играть, есть, работать, ходить в магазин
#если сытость объекта < 0, то объект умирает
#челоыеку надо прожить 365 дней
from termcolor import cprint

class Human:
    
    def __init__(self, name):
        self.money = 0#количество денег
        self.count_food=10#количество еды, которую я могу поесть
        self.fullness=0# сытость
        self.name=name
        self.fatique=0#усталость
        self.house = None
    
    def __str__(self):
        return f"Я {self.name}, у меня осталось еды - {self.count_food}, денег - {self.money} и я на столько сыт {self.fullness}, а устал {self.fatique}"
    
    def work(self):
        if (self.money == 0):
            self.money+=100
            self.fatique+=10
            self.fullness-=20
            cprint(f"Я - {self.name}, я заработал вот столько денег - {self.money}, а также устал - {self.fatique}, проголодался - {self.fullness}", color='yellow')
    
    def play(self):
        if(self.fatique > 10):
            self.fatique-=10
            cprint(f'Я - {self.name}, я отдохнул - {self.fatique}',color='cyan')    

    def shopping(self):
        if(self.money>1):
            while(self.money != 0):
                self.count_food+=1
                self.money-=10
            cprint(f'Я {self.name}, я купил еду - {self.count_food}, у меня осталось столько денег - {self.money}', color='light_blue')    
    
    def eat(self):
        if (self.fullness == 0):
            if(self.count_food !=0):
                self.count_food-=1
                self.fullness+=1
                cprint(f"{self.name} поел",color='light_red')
    
    def go_into_the_house(self, house):
        self.house=house
        cprint(f'Я заехал в этот дом!!!!!!! {self.house}', color='blue')

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


Andrey = Human('Andrey')
Olga=Human('Olga')
house=House('Советская 123')
#for day in range (1,8):
 #   cprint(f"================day {day}==========================",color='red')
  #  Andrey.act()
   # Olga.act()
    #print(Andrey,Olga)
print(Andrey.go_into_the_house('Советская 123'))
