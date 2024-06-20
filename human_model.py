#атрибуты человека - сытость, количество денег, количество еды, усталость
#методы - играть, есть, работать, ходить в магазин
# В общем - у них теперь общий бюджет и еда, поэтому из объектов класса убралось количество еды и денег
# Пока что я еще не знаю можно ли сделать это как-то лучще..
from termcolor import cprint
from random import choice

class Human:
    
    def __init__(self, name):
        self.fullness=0# сытость
        self.name=name
        self.fatique=0#усталость
        self.house = None
        self.cat = None
    
    def __str__(self):
        return f"Я {self.name}, я на столько сыт {self.fullness}, а устал {self.fatique}"
    
    def work(self):
        if (self.house.has_money == 0):
            self.house.has_money+=100
            self.fatique+=40
            self.fullness-=20
            cprint(f"Я - {self.name},денег - {self.house.has_money}, устал - {self.fatique}, проголодался - {self.fullness}", color='yellow')
    
    def play(self):
        if(self.fatique >= 10):
            self.fatique-=10
            cprint(f'Я - {self.name}, я поиграл - {self.fatique}',color='cyan')    

    def shopping(self):
        if(self.house.has_money>1):
            while(self.house.has_money != 0):
                self.house.has_food+=10
                self.house.has_money-=10
            cprint(f'Я {self.name}, я купил еду - {self.house.has_food}, у меня осталось столько денег - {self.house.has_money}', color='light_blue')    
    
    def eat(self):
            if(self.house.has_food !=0):
                self.house.has_food-=20
                self.fullness+=20
                cprint(f"{self.name} поел",color='light_red')
    
    def go_into_the_house(self, house):
        self.house=house
        cprint(f'Я {self.name} заехал в этот дом!!!!!!! {self.house}', color='blue')
        House.count_citizens+=1
    
    def take_a_cat(self, nickname):
        self.cat=nickname
        cprint(f'{self.name} взял кота {self.cat}', color='light_blue')
        House.count_cats+=1

    # def feed_the_cat(self):
    #     self.house.has_food-=50
    #     self.cat.cat_food+=50


    def act(self):
        if(self.fullness <=10):
            self.eat()
        self.work()
        if (self.house.has_food <=10):
            self.shopping()
        if (self.fatique>=10):
            self.play()
        # if(self.cat.cat_food <=10):
        #     self.feed_the_cat()

class House:
    count_citizens=0
    count_cats=0
    def __init__(self, addres):
        self.has_food=10
        self.has_money=500
        self.addres=addres
    def __str__(self):
        return f'В доме осталось столько еды - {self.has_food}, столько денег - {self.has_money}, а вот мой адрес - {self.addres}'

#Кошка у нас будет уметь есть, спать, уставать, а также бегать по дому
#
#
#
class Cats:
    
    def  __init__(self,nickname):
        self.nickname = nickname
        self.cat_fullness=10
        self.cat_fatique=0
        self.cat_fun=25
        self.cat_food=2000
    def __str__(self):
        return f'по имени {self.nickname}'

    def sleep(self):
        self.cat_fatique-=5
        self.cat_fullness-=3
        cprint(f'{self.nickname} поспала', color='green')

    def eat(self):
        self.cat_food-=10
        self.cat_fullness+=8
        cprint(f'{self.nickname}  поела ', color='yellow')

    def running_around_the_house(self):
        self.cat_fun+=5
        self.cat_fatique+=7
        self.cat_fullness-=4
        cprint(f'{self.nickname} побегала по дому', color='red')

    def act(self):
        self.running_around_the_house()
        if(self.cat_fullness<=15 and self.cat_food>=10):
            self.cat_fun-=10
            self.eat()
        elif(self.cat_fullness<=5 and self.cat_food <=10):
            self.cat_fun-=10
            cprint(f'{self.nickname} очень голодная, ей нечего есть', color='red')

        if(self.cat_fatique>=10):
            self.sleep()


citizens = [
    Human('Andrey'),
    Human('Olga')
]

cat=Cats(nickname='Бирка')

#print(bir.nickname, birka.cat_fun)

house=House('Советская 123')

for citizen in citizens:
    citizen.go_into_the_house(house=house)
    #House.count_citizens+=1


chosen_citizen = choice(citizens)
chosen_citizen.take_a_cat(nickname=cat)




for day in range (1,8):
    cprint(f"================day {day}==========================",color='red')
    for citizen in citizens:
        citizen.act()
        print(citizen)
    cat.act()
    print(house)
    print('-------------------------в конце дня---------------------------')
    cprint(f'количество еды у кошки - {cat.cat_food}',color='yellow')
    cprint(f'количество усталости у кошки - {cat.cat_fatique}',color='yellow')
    cprint(f'количество сытости у кошки - {cat.cat_fullness}',color='yellow')
    cprint(f'количество радости у кошки - {cat.cat_fun}',color='yellow')
    
cprint(f'Я - дом с адресом {house.addres}, мое количесвто жителей - {House.count_citizens}, количество котов - {House.count_cats}', color='green')
