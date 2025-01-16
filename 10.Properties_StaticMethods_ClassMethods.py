'''
in this section we are gonna learn somethings that proffesional python programmers use them
we are gonna use something called decorator, it let us define functions with same name that works differently
we also can call those functions without ()
another point is we define different functions with same name
'''

class Person:
    def __init__(self, name):
        self.__name = name
        
    # this is our getter, so we use @property
    @property
    def name(self):
        return f'The name is {self.__name}'

    # this is our setter so we use @name.setter
    @name.setter
    def name(self,new_name):
        self.__name = new_name
        print('Changing name ... please wait ...')
        return f'The name changed to {new_name}'

    # and this is our deleter so we use @name.deleter
    @name.deleter
    def name(self):
        del self.__name

person1 = Person('Mehdi')

print(person1.name)

person1.name = 'Mamad'
print(person1.name)

del person1.name # print(person1.name) # and here we get error because we deleted person 1 before.

# another instance of using decorator :

class Gamer:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return f'Gamer nickname is {self.__name}'

    @name.setter
    def name(self, new_name):
        self.__name = new_name
        print(f'Nickanme changed to {self.__name}')


gamer1 = Gamer('AliIllidan')

print(gamer1.name)
gamer1.name = 'GreenHorn'
print(gamer1.name)

# ----------------------------------------------------------------

class my_math:
    
    @staticmethod
    def sum_sum(x, y):
        return x + y

print(my_math.sum_sum(5, 7))

class Noslash:
    
    @staticmethod
    def replacer(date):
        list(date)
        new_date = ''
        for i in date:
            if i == '/':
                i = '-'
            new_date += i
        
        return new_date

# another static method :

print(Noslash.replacer('1403/9/24'))

# teacher method :

class Date:
    
    @staticmethod
    def DoDashDate(user_date):
        user_date.replace('/', '-')
        return user_date

print(Date.DoDashDate('1403/9/24'))

# ----------------------------------------------------------------
# now we gonna learn about class methods :
class SayAge:
    age = 18
    
    @classmethod
    def say_age(cls):    # classname.age
        return f'The age is {cls.age}'

print(SayAge.say_age())

# ----------------------------------------------------------------
# A random practice :
import datetime

class Person:
    what_is_date = datetime.datetime.now()

    def __init__(self, name, age):
        self.__name = name
        if age > 100:
            self.age = Person.what_is_date.year - age
        else:
            self.age = age
    
    @property    
    def name(self):
        print(f'The name is {self.__name} and have {self.age} years old')
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        print(f'The name changed to {new_name}')
    
    @name.deleter
    def name(self):
        del self.__name


person1 = Person('Mehdi', 18)
person2 = Person('Payam', 2003)


person1.name
person1.name = 'milad'
person1.name
del person1.name
print(person1.__dict__)
person2.name









