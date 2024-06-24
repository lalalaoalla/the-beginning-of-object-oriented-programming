from datetime import date
from termcolor import cprint

class Person:
    list = []

    def __init__(self, firstname, name, otchestvo, sex, height, date_of_birth):
        self.firstname = firstname
        self.name = name
        self.otchestvo = otchestvo
        self.__sex = sex
        self.height = height
        self.date_of_birth = date_of_birth
        self.age = 1  

    def counting_age(self, date_of_birth):
        '''Функция для получения возраста по дате рождения'''
        today = date.today()
        self.age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        return self.age

    def append_list(self):
        '''Функция добавления данных в список'''
        Person.list.append({'firstname': self.firstname, 'name': self.name,
                            'otchestvo': self.otchestvo, 'sex': self.__sex,
                            'height': self.height, 'date_of_birth': self.date_of_birth,
                            'age': self.age})
        return Person.list  

    def sort(self, flag=0):
        '''Функция сортировки'''
        if flag == 2:
            sorted_list = sorted(Person.list, key=lambda item: item['firstname'])
            for i in sorted_list:
                cprint(f"{i['firstname']} {i['name']} {i['otchestvo']} пол - {i['sex']}, рост - {i['height']}, возраст - {i['age']}", color='green') 

        if flag == 3:
            sorted_list = sorted(Person.list, key=lambda item: item['firstname'], reverse=True)
            for i in sorted_list:
                cprint(f"{i['firstname']} {i['name']} {i['otchestvo']} пол - {i['sex']}, рост - {i['height']}, возраст - {i['age']}", color='green')

    def act(self, date_of_birth):
        self.counting_age(date_of_birth)
        self.append_list()
