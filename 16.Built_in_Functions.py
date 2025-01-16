# Let's start with map function :

'''
make a function that make cantigrad to farenhate
'''

def cantofaren(temp):
    return (temp * 9/5) + 32

print(cantofaren(0))
print(cantofaren(28))
print(cantofaren(11))

# now solve it with map function :

my_temps = [0, 28, 11]
map_output = map(cantofaren, my_temps)

print(list(map_output))

# ----------------------------------------------------------------

list1 = range(10)

def zoj_check(num):
    if num % 2 == 0:
        return True
    else:
        return False

# using filter function :
print(list(filter(zoj_check, list1)))































































