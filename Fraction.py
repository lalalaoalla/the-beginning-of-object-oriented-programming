from termcolor import cprint

class Fraction:
    def __init__(self, a=0,b=1):
        self.a=a#числитель
        self.b=b#знаменатель
        self.number=self.a/self.b
        #self.int_num=0#если вдруг у нас это целое число все-таки
    def __str__(self):
        return f'Получил число {self.a}, а также число {self.b}, дробь выглядит так {self.a}/{self.b}, в виде десятичного - {self.number}'
    
    def error(self):
        if (self.b==0):
            cprint(f'Делить на 0 нельзя', color='red')
    
    def int_number(self):
        if(self.a%self.b == 0):
            cprint(f'{self.a}/{self.b} целое число - {self.a//self.b}', color='light_yellow')
        #return a//b

    def act(self):
        self.error()
        self.int_number()

    def __add__(self, other):
        if isinstance(other,Fraction):
            return (self.number + other.number).as_integer_ratio()
    def __sub__(self,other):
        if isinstance(other,Fraction):
            return (self.number - other.number).as_integer_ratio()
    def __mul__(self,other):
        if isinstance(other, Fraction):
            return (self.number*other.number).as_integer_ratio()
    def __truediv__(self,other):
        if isinstance(other,Fraction):
            if(other.number!=0):
                return (self.number/other.number).as_integer_ratio()
            else:
                cprint(f'На 0 делить нельзя',color='red')
    
    
class OperatonsOnFraction(Fraction):
    def __init__(self,a=0,b=1):
        super().__init__(a=a,b=b)
    def int_(self):
        return int(self.number)
    def float_(self):
        return float(self.number)


    


fraction1=OperatonsOnFraction(1,2)
fraction2=OperatonsOnFraction(11,2)
fraction1.act()
fraction2.act()

print(fraction1.float_())
print(fraction2.int_())

# number_add=fraction1.__add__(fraction2)
# number_sub=fraction1.__sub__(fraction2)
# number_mul=fraction1.__mul__(fraction2)
# number_div=fraction1.__truediv__(fraction2)

print(fraction1,fraction2)
# print(number_add)
# print(number_sub)
# print(number_mul)
# print(number_div)