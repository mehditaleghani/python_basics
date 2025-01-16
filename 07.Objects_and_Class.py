# class Car: # car is a class
#     def __init__(self, name, model, color):
#         self.name = name # these are attrebiutes
#         self.model = model # these are attrebiutes
#         self.color = color # these are attrebiutes
#         self.quality = f'this car in year {self.model} have a great quality' # this is an instance attrebiute
        
# Dodge = Car('Challenger R/T', '1970', 'Black') # Dodge is an instace (instace of Car)

# print(Dodge.name)
# print(Dodge.model)
# print(Dodge.color)
# print(Dodge.quality)

# ----------------------------------------------------------------

# # another class that we used a function on it, when we use functions in classes we call them methods
# class NewCar:
#     def __init__(self, name, model, color):
#         self.name = name
#         self.model = model
#         self.color = color
        
#     def DescribeCar(self): # this is a method
#         return f'this car is a {self.name} , it\'s for {self.model} and the color is {self.color}'

# NewDodge = NewCar('Challenger R/T', '1970', 'Black')

# print(NewDodge.DescribeCar()) # thats how python methods made i think

# ----------------------------------------------------------------

# class Dog:
#     DoYouHaveDog = 'YES' # this is  a class attrebiute, it's different from instance attrebiute
#     def __init__(self, DogName, DogRace, DogColor, IsRabid, Price, Wool = True):
#         self.DogName = DogName
#         self.DogRace = DogRace
#         self.DogColor = DogColor
#         self.IsRabid = IsRabid
#         self.Price = Price
#         self.Wool = Wool

#     def ChatBot(self):
#         if self.DogRace == 'PresaCenario':
#             return f'''
# This Dogs are a really good race for guarding and these stuff their
# race is {self.DogRace} and they have the most power between Dogs.
# Name of this one is {self.DogName} and it's color is {self.DogColor}.
# It's Rabid test was "{self.IsRabid}" and the price is really good it's
# {self.Price} and totally worthy.
# '''
#         elif self.DogRace == 'GermanShepherd':
#             return f'''
# This Dogs are a really good race for guarding and these stuff their
# race is {self.DogRace} and they have the most power between Dogs.
# Name of this one is {self.DogName} and it's color is {self.DogColor}.
# It's Rabid test was "{self.IsRabid}" and the price is really good it's
# {self.Price} and totally worthy.
# '''
#         elif self.DogRace == 'ShortFeet'         :
#             return f'''
# Shitty and stupid dogs ... {self.DogRace}s ...
# Name of this one is {self.DogName}
# it's color is {self.DogColor}.
# It's Rabid test was "{self.IsRabid}" and about the price ...
# I don't buy these Fogs even for free bwt it's {self.Price} 
# '''         


# PresaCanario1 = Dog('Hector', 'PresaCenario', 'Brown and black', 'No', '460$')
# GermanShepher1 = Dog('Aldio', 'GermanShepherd', 'Gray', 'No', '520$')
# ShortFeet1 = Dog('Chiku', 'ShortFeet', 'Shite', 'No', '240$')

# print(Dog.DoYouHaveDog)
# print(PresaCanario1.DoYouHaveDog)
# print(PresaCanario1.Wool)

# ----------------------------------------------------------------

# class Pc:
#     RamUpgrade = 8
#     def __init__(self, Ram, Cpu, Gpu, Power, Mboard):
#         self.Ram = Ram
#         self.Cpu = Cpu
#         self.Gpu = Gpu
#         self.Power = Power
#         self.Mboard = Mboard

#     def RamUpgeadeCalc(self):
#         self.Ram += Pc.RamUpgrade

# Pc1 = Pc(8, 'Corei3 Gen 11', 'On board', '300w', 'MSI')
# Pc2 = Pc(4, 'Corei5 Gen 8', 'GTX 780', '450w', 'MSI')
# Pc3 = Pc(16, 'Corei5 Gen 9', 'RTX 1080', '600w', 'MSI')

# Pc1.RamUpgeadeCalc()
# print(Pc1.Ram)
        
# ----------------------------------------------------------------

# class Pc:
#     RamUpgrade = 8
#     def __init__(self, Ram, Cpu, Gpu, Power, Mboard):
#         self.Ram = Ram
#         self.Cpu = Cpu
#         self.Gpu = Gpu
#         self.Power = Power
#         self.Mboard = Mboard

#     def RamUpgeadeCalc(self):
#         self.Ram += Pc.RamUpgrade

# Pc1 = Pc(8, 'Corei3 Gen 11', 'On board', '300w', 'MSI')
# Pc2 = Pc(4, 'Corei5 Gen 8', 'GTX 780', '450w', 'MSI')
# Pc3 = Pc(16, 'Corei5 Gen 9', 'RTX 1080', '600w', 'MSI')

# print(Pc.__dict__)
# print('')
# print(Pc1.__dict__)
# print('')
# print(Pc2.__dict__)

# ----------------------------------------------------------------

# class Dog:
    
#     DoYouHaveDog = 'YES' # this is  a class attrebiute, it's different from instance attrebiute
#     DogsNumber = 0
    
#     def __init__(self, DogName, DogRace, DogColor, IsRabid, Price, Wool = True):
#         self.DogName = DogName
#         self.DogRace = DogRace
#         self.DogColor = DogColor
#         self.IsRabid = IsRabid
#         self.Price = Price
#         self.Wool = Wool
#         Dog.DogsNumber += 1

#     def ChatBot(self):
#         if self.DogRace == 'PresaCenario':
#             return f'''
# This Dogs are a really good race for guarding and these stuff their
# race is {self.DogRace} and they have the most power between Dogs.
# Name of this one is {self.DogName} and it's color is {self.DogColor}.
# It's Rabid test was "{self.IsRabid}" and the price is really good it's
# {self.Price} and totally worthy.
# '''
#         elif self.DogRace == 'GermanShepherd':
#             return f'''
# This Dogs are a really good race for guarding and these stuff their
# race is {self.DogRace} and they have the most power between Dogs.
# Name of this one is {self.DogName} and it's color is {self.DogColor}.
# It's Rabid test was "{self.IsRabid}" and the price is really good it's
# {self.Price} and totally worthy.
# '''
#         elif self.DogRace == 'ShortFeet'         :
#             return f'''
# Shitty and stupid dogs ... {self.DogRace}s ...
# Name of this one is {self.DogName}
# it's color is {self.DogColor}.
# It's Rabid test was "{self.IsRabid}" and about the price ...
# I don't buy these Fogs even for free bwt it's {self.Price} 
# '''         


# PresaCanario1 = Dog('Hector', 'PresaCenario', 'Brown and black', 'No', '460$')
# GermanShepher1 = Dog('Aldio', 'GermanShepherd', 'Gray', 'No', '520$')
# ShortFeet1 = Dog('Chiku', 'ShortFeet', 'Shite', 'No', '240$')

# print(PresaCanario1.DogsNumber)

# print(Dog.DoYouHaveDog) # it's YES because we are using the class attrebiute.
# print(PresaCanario1.DoYouHaveDog) # it's YES because instances have a property called inherit.
# print(PresaCanario1.__dict__) # as you see we don't have DoYouHaveDog because we are inheriting DoYouHaveDog from class Dog.
# PresaCanario1.DoYouHaveDog = 'NO' # But now we define this attrebout for instance it self
# print(PresaCanario1.__dict__) # as you see now we have DoYouHaveDog with value of NO
# print(Dog.DoYouHaveDog) # and DoYouHaveDog of class Dog is still YES

# ----------------------------------------------------------------

# class Dog:
    
#     DoYouHaveDog = 'YES' # this is  a class attrebiute, it's different from instance attrebiute
#     DogsNumber = 0
#     DogsNumber2 = 0
    
#     def __init__(self, DogName, DogRace, DogColor, IsRabid, Price, Wool = True):
#         self.DogName = DogName
#         self.DogRace = DogRace
#         self.DogColor = DogColor
#         self.IsRabid = IsRabid
#         self.Price = Price
#         self.Wool = Wool
#         self.DogsNumber2 += 1 # here instace can change this value go down and test
#         Dog.DogsNumber += 1 # here we use class name instead of instance name, in this way instace just can see value of DogsNumber and can't change the value
#         # print('Hello world')

#     def ChatBot(self):
#         if self.DogRace == 'PresaCenario':
#             return f'''
# This Dogs are a really good race for guarding and these stuff their
# race is {self.DogRace} and they have the most power between Dogs.
# Name of this one is {self.DogName} and it's color is {self.DogColor}.
# It's Rabid test was "{self.IsRabid}" and the price is really good it's
# {self.Price} and totally worthy.
# '''
#         elif self.DogRace == 'GermanShepherd':
#             return f'''
# This Dogs are a really good race for guarding and these stuff their
# race is {self.DogRace} and they have the most power between Dogs.
# Name of this one is {self.DogName} and it's color is {self.DogColor}.
# It's Rabid test was "{self.IsRabid}" and the price is really good it's
# {self.Price} and totally worthy.
# '''
#         elif self.DogRace == 'ShortFeet'         :
#             return f'''
# Shitty and stupid dogs ... {self.DogRace}s ...
# Name of this one is {self.DogName}
# it's color is {self.DogColor}.
# It's Rabid test was "{self.IsRabid}" and about the price ...
# I don't buy these Fogs even for free bwt it's {self.Price} 
# '''         


# PresaCanario1 = Dog('Hector', 'PresaCenario', 'Brown and black', 'No', '460$')
# GermanShepher1 = Dog('Aldio', 'GermanShepherd', 'Gray', 'No', '520$')
# ShortFeet1 = Dog('Chiku', 'ShortFeet', 'Shite', 'No', '240$')

# # each time we make an instace the __init__ will be execute, just uncomment the Hello world to see

# print(Dog.DogsNumber)
# print(PresaCanario1.DogsNumber)

# PresaCanario1.DogsNumber = 5

# print(Dog.DogsNumber)
# print(PresaCanario1.DogsNumber)
# # as you see now we have 2 DogsNumber 1 one Dogs with value of 3 and 1 for Presacanario1 with value of 5

# print(Dog.DogsNumber2) # value 0
# print(ShortFeet1.DogsNumber2) # value 1
# print(ShortFeet1.__dict__)
# print(Dog.DogsNumber2)
# # each one have it's own Dogs number ...

# ----------------------------------------------------------------

# Write a class `Book` with attributes `title`, `author`, `price`
# and a class attribute `discount` set to 0.1. Add a method
# `apply_discount()` that reduces the price by the discount
# percentage. Create two instances of the class with different
# titles and prices, and apply the discount to one of them.

class Book:
    discount = 0.1
    def __init__(self, title, author, price, special_discount = 0.1):
        self.title = title
        self.author = author
        self.price = price
        self.special_discount = special_discount
    
    def apply_discount(self):
        self.price = self.price - self.price*Book.discount

    def apply_special_discount(self):
        self.price = self.price - self.price*self.special_discount

Book1 = Book('Vampire assistant', 'Darren shan', 40)
Book2 = Book('A song og ice and fire', 'George RR Martin', 90)

print(f'Book price : {Book1.price}')
Book1.apply_discount()
print(f'Book price after discount : {int(Book1.price)}')

print(f'Book price : {Book2.price}')
Book2.apply_special_discount()
print(f'Book price after discount : {int(Book2.price)}')

