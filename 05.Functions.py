#functions
def MyFunc():
    print('Hello world')
# MyFunc()

# ----------------------------------------------------------------

# num1 = int(input('Enter number 1 : '))
# num2 = int(input('Enter number 2 : '))
# def Calculator():
#     print(num1 + num2)
# Calculator()

def MyFunc_2():
    return 'Hello MehdiTaleghani'
MyFunc_2() # this is not working
# print(MyFunc_2())
# so what return is doing is showing raw data is output , it's returning the value to the place that function is executed

def NewFunc(name):
    print(f'Hello dear {name} welcome to your application')
# NewFunc() # this will show error
# NewFunc('Mehdi')
# so here we send the value Mehdi to name it's like "name = ?" and when we call NewFunc we can assign a value to "name" variable in NewFunc

def DocString():
    '''
    #######################################################
    # this is my "doc string", it's essential to use them #
    #######################################################
    '''
# print(DocString.__doc__)

# ----------------------------------------------------------------

#global variables
a = 5
def NewFunc_2():
    a = 10
    print(a)
# NewFunc_2()
# print(a)

a = 5
def NewFunc_3():
    a = a + 10
    print(a)
# NewFunc_3() # it says "i can't use a because a is not local"

a = 5
def NewFunc_4():
    global a
    a += 10 # a is 5 and 5 + 10 is 15 so output of NewFunc_4() is 15
    print(a)
# NewFunc_4()

name = ''
def ChangeName(UserName):
    global name
    name = UserName
    print(f'Hello dear {name}')
# print(name + ' ?')
# ChangeName('Mehdi')
# print(name + ' ?')

a = 100
b = 'Mehdi'
c = 650
# print(globals())

def LocalVars():
    a = 60
    b = 'Taleghani'
    c = 28
    print(locals())
# LocalVars()

# ----------------------------------------------------------------
#Different argumants 

# def greeting(greet, name):
#     return f'"{greet}" dear "{name} welcome"'
# print(greeting('Hello', 'Mehdi')) # these are normal argumetns

# def greeting_2(greet, name):
#     return f'"{greet}" dear "{name} welcome"'
# print(greeting_2(greet = 'Hello', name = 'Mehdi')) # these are key word arguments

# def greeting_3(greet = 'Say Hello or سلام or onichan ...', name = 'Say your name here'): # default values
#     return f'"{greet}" dear "{name} welcome"'
# print(greeting_3(greet='Hello')) # we forget to assign name argument

# ----------------------------------------------------------------
# what are *args and *kwargs

# args = (3, 'Hello', 75)
# kwargs = {'name' : 'Hello', 'age' : 18}
# def greeting_4(*args, **kwargs):
#     print(args)
#     print(kwargs)
# greeting_4('hello',
# 'goodbye', 123123, name = 'mehdi', age = 18)

# myargs = (123, 'Mehdi', 321, 'Idhem')
# mykwargs = {'name' : 'Mehdi', 'lastname' : 'Taleghani'}
# def greeting_5(*args, **kwargs):
#     print(*args)
#     print(**kwargs)
# greeting_5(myargs, mykwargs)

# factorial - calculate factorial of 5
# def calculator(number):
#     main = 1
#     for i in range(1, number+1):
#         main = main * i
#     print(main)
# calculator(5)

# ----------------------------------------------------------------
# lambda functions

morabae_number = lambda num : num ** 2
# print(morabae_number(4))

IsEvenOrNot = lambda number : number % 2 == 0
# print(IsEvenOrNot(7))

first = lambda word : word[0]
# print(first('Mehdi'))

AddNumber = lambda x,y : x + y
# print(AddNumber(80, 20))





