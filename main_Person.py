from class_Person import Person
from datetime import date
from termcolor import cprint


cprint('Выберите, что хотите сделать', color='green')
cprint('Чтобы добавить пользователя, введите - 1', color='red')
cprint('Чтобы отсортировать пользователей по возрастсанию введите - 2', color='yellow')
cprint('Чтобы отсортировать пользователей по убыванию введите - 3', color='blue')
cprint('Чтобы закончить работу, введите - 0', color='light_red')
flag=int(input())

if ((flag<0) or (flag>3)):
    cprint('Пожалуйста, введите число от одного до трех')
    cprint('Выберите, что хотите сделать', color='green')
    cprint('Чтобы добавить пользователя, введите - 1', color='red')
    cprint('Чтобы отсортировать пользователей по возрастсанию введите - 2', color='yellow')
    cprint('Чтобы отсортировать пользователей по убыванию введите - 3', color='blue')
    cprint('Чтобы закончить работу, введите - 0', color='light_red')
    flag=int(input())

if (flag==0):
    cprint('Возвращайтесь к нам еще',color='green')
    exit()

if (flag==1):
    while(flag==1):
        cprint('Пожалуйста, введите фамилию', color='yellow')
        firstname=str(input())
        cprint('Введите имя', color='yellow')
        name=str(input())
        cprint('Введите отчество', color='yellow')
        otchestvo=str(input())
        cprint('Введите пол', color = 'yellow')
        sex=str(input())
        cprint('Введите рост в сантиметрах',color='yellow')
        height=int(input())
        cprint('Введите год рождения', color='yellow')
        year=int(input())
        cprint('Введите mесяц рождения', color='yellow')
        month=int(input())
        cprint('Введите день рождения', color='yellow')
        day=int(input())

        date_of_birth=date(year, month, day)
        person=Person(firstname,name, otchestvo, sex, height, date_of_birth)
        person.act(date_of_birth)

        cprint('Выберите, что хотите сделать', color='green')
        cprint('Чтобы добавить пользователя, введите - 1', color='red')
        cprint('Чтобы отсортировать пользователей по возрастсанию введите - 2', color='yellow')
        cprint('Чтобы отсортировать пользователей по убыванию введите - 3', color='blue')
        cprint('Чтобы закончить работу, введите - 0', color='light_red')
        flag=int(input())
if (flag==2):
    person.sort(flag)
    cprint('Выберите, что хотите сделать', color='green')
    cprint('Чтобы добавить пользователя, введите - 1', color='red')
    cprint('Чтобы отсортировать пользователей по возрастсанию введите - 2', color='yellow')
    cprint('Чтобы отсортировать пользователей по убыванию введите - 3', color='blue')
    cprint('Чтобы закончить работу, введите - 0', color='light_red')
    flag=int(input())
if (flag==3):
    person.sort(flag)
    cprint('Выберите, что хотите сделать', color='green')
    cprint('Чтобы добавить пользователя, введите - 1', color='red')
    cprint('Чтобы отсортировать пользователей по возрастсанию введите - 2', color='yellow')
    cprint('Чтобы отсортировать пользователей по убыванию введите - 3', color='blue')
    cprint('Чтобы закончить работу, введите - 0', color='light_red')
    flag=int(input())
    
