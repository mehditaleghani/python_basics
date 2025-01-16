# we are gonna learn encapsulation in this section , first we need to learn a new concept, look at this class
'''
we are going to make variables privet and limited to the class we wanna stop users to
assign new values to variables from old school "var.attr = x" way
'''

class Car:
    def __init__(self, model, speed, color):
        self.model = model
        self.speed = speed
        self.color = color

# we need 2 methods named getter and setter for showing values and setting new values for attributes
    def get_speed(self): # we also can use getter_speed
        return self.speed
    
    def set_speed(self, new_speed): # we also can use setter_speed
        self.speed = new_speed

dodge = Car('Dodge challenger', '240', 'Black')

# print(dodge.speed) # this method is not good, we should do it in this way :
print(dodge.get_speed())

# dodge.speed = 255 # this is not the right way of assigning a new value to an attribute, this is how we should do it :
dodge.set_speed(265)
print(dodge.speed)

# ----------------------------------------------------------------

'''
so for now we learned how is the proper way of assigning a new value to an attribute and 
how should we show value of a attribute, now let's learn how encapsulation works and how
to do it
'''

class Test:
    def __init__(self, name):
        self.a = name
        self._b = name # this is  a privet variable
        self.__c = name # this is  a super privet variable and only Test class can see it's value ot change it.

something1 = Test('Random name 1')
something2 = Test('Random name 2')
something3 = Test('Random name 3')

print(something1.a)
print(something2._b)
# print(something3.__c)


'''
as you see we could print random name 1 and random name 2, but what happend to random name3 ?
well we made random name 3 privet :D (we puted it in a capsule we encapsulated something3 so
now only 1 thing can access it "just the Test calss it self")
'''

# ----------------------------------------------------------------

'''
so now we are gonna do the same thing to car calss, we don't want other programmers to use 
car.speed = 255 method we wanna force them to use our methods like set_speed(265)
'''

class Newcar:
    def __init__(self, model, speed, color):
        self.model = model
# we can't make this     ↓  and ↑ this speed into a privet variable because we are getting their value from user and as we know only class can change the values of a privet variable
        self.__speed = speed 
# so we make this ↑ speed into a privet variable speed → __speed and it becomes super privet and only class can change the value
# so know for changing the values we need to change them only via setter and getter methods
        self.color = color

    def get_speed(self):
        return self.__speed
    
    def set_speed(self, new_speed):
        self.__speed = new_speed

camaro = Newcar('Camaro 2016', '310', 'Black')

# print(camaro.speed) # yeap it says "AttributeError: 'Newcar' object has no attribute 'speed'"
# print(camaro.__speed) # and also this one says "AttributeError: 'Newcar' object has no attribute '__speed'. Did you mean: 'get_speed'?"

# Let's try this : 
print(camaro.get_speed()) # yeap it's working (:, we encapsulated a variable 

# ----------------------------------------------------------------

'''
you may ask what is point of making a variable privet when user can use the method and change
values ? That's right Now let's see a realstic example :
'''
print()
class Sellthings:
    public_discount_code = '123123'
    discount_amount = '33%'
    
    
    def __init__(self, price):
        self.__price = price
        
    
    def __print_discount(self): # this is a encapsulated method 
        print(f'congratulation you got {Sellthings.discount_amount} price discount!')
    
    def set_thing(self):
        dicount_code = input('Do you have dicount code ? (y/n)')
        
        if dicount_code == 'y' or dicount_code == 'Y' :
            what_is_discount_code = input('enter it please : ')
            
            if what_is_discount_code == Sellthings.public_discount_code:
                self.__price -= 10
                self.__print_discount()
                print(f'dvd price 30 → {self.__price}')
                    
            elif what_is_discount_code != '123123':
                print(f'wrong discount code ... dvd price → {self.__price}')
                
        elif dicount_code == 'n' or dicount_code == 'N' :
            print(f'dvd price → {self.__price}')
    
    def get_thing(self):
        return self.__price


dvd = Sellthings(30)
print(dvd.get_thing())
dvd.set_thing()



