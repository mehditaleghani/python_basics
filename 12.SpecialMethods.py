# Let's learn some special method 

class CustomClass1:
    def __init__(self):
        pass
'''the first one is __init__ , it help us to do OOP mush easier .'''

class CustomClass2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} : ("{self.name}" - "{self.age}")'
    
object1 = CustomClass2('Mehdi', '18')
print(object1.__dict__) # this one show all values of object1
print('--------------------------------------------------------------------')
print(object1)# "<__main__.CustomClass2 object at 0x7626b6846ff0>" , to solve this we use __str__
# as you see we solved it :D 
print()

# ----------------------------------------------------------------

import datetime
today = datetime.datetime.now()

print(str(today)) # we use str to show outputs to users.
print('--------------------------------------------------------------------')
print(repr(today)) # we use repr to see outputs our self, we use it for debug.
print()

# ----------------------------------------------------------------

class Book:
    def __init__(self, name, author, pages):
        print('Book has been created')
        self.name = name
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f'The book name is {self.name} and the writer is {self.author}, page have arounf {self.pages} pages and every one should read it at least 1 time'
    
    def __len__(self):
        return self.pages

book1 = Book('Vampire assistant', 'Darren shan', 270)

print(book1)
print(len(book1))








