#if state ments in python
x = 50
a = 100
# if a > x:
#     print(f'{a} is bigger than {x}')

b = 20
# if b > x:
    # print(f'{b} is bigger than {x}')
# else:
    # print(f'{b} is smaller than {x}')

# ----------------------------------------------------------------

#nested if and else if
num1 = 2
num2 = 3
main_num = 12
# if main_num % num1 == 0 and main_num % num2 == 0:
#     print(f'{main_num} is divisible to {num1} and {num2}')
# elif main_num % num2 == 0:
#     print(f'{main_num} is divisible to {num2}')
# elif main_num % num1 == 0:
#     print(f'{main_num} is divisible to {num1}')
# else:
#     print(f'{main_num} is not divisible to {num1} or {num2}')

# if main_num % num1 == 0:
    # if main_num & num2 == 0:
        # print(f'{main_num} is divisible to {num1} and {num2}')
    # else:
        # print(f'{main_num} is divisible to {num1}')
# else:
    # if main_num % num2 == 0:
        # print(f'{main_num} is divisible to {num2}')
    # else:
        # print(f'{main_num} is a single number')

# ----------------------------------------------------------------
#for loops   

mlist = [5, 4, 6, 3, 7, 6, 8]
x = 0
# for i in mlist:
#     # print(i)
#     x += i
#     print(x)

dota_players_list = ['Topson', 'Miracle', 'w33ha']
# for i in range(len(dota_players_list)):
#     print(f'Game play of "{dota_players_list[i]}" is great')

# for i in range(len(dota_players_list)):
#     print(f'Game play of "{dota_players_list[i]}" is great')
# else:
#     print('I don\'t know any other great player.')

# ----------------------------------------------------------------

#break continue pass
mylist = [3, 5, 7 ,9, 10, 31, 50]
# for i in mylist:
#     if i % 2 == 0:
#         break
#     print(i)

# for i in 'string':
#     if i == 'i':
#         break
#     print(i)

# print('\n')
# for i in 'string':
#     if i == 'i':
#         break
#     print(i, end='')

# print('\n')
# for i in 'string':
#     if i == 'i':
#         break
#     print(i, end=' ')

# for i in 'string':
#     if i == 'i':
#         continue #ignor the contion i think
    # print(i)

# for i in 'string':
#     if i == 'i':
#         pass #we pass errors with "pass"
#     print(i)

# ----------------------------------------------------------------
    
# for i in range(1,11):
#     print(f'zarb adad {i}')
#     for j in range(1,11):
#         k = i*j
#         print(f'hasel zarb {i} dar {j} mishe {k}')

# ----------------------------------------------------------------

#for loops in lists AKA list comperhension
list1 = []
# for i in 'Meh':
#     list1.append(i)
# print(list1)

list2 = [i for i in 'Mehdi']
# print(list2)

list3 = [i for i in range(11)]
# print(list3)

list4 = [i for i in range(11) if i % 2 == 0]
# print(list4)

list5 = [i for i in range(11) if i % 2 == 0 if i % 3 == 0]
# print(list5)

list6 = [i for i in range(100) if i % 2 == 0 if i % 5 == 0]
# print(list6)

list7 = ['Even' if i % 2 == 0 else 'Odd' for i in range(11)]
# print(list7)

# user_input = int(input('say : '))
# list8 = [i for i in range(user_input+1) if i % 2 == 0]
# print(f'there is {len(list8)} even numbers from 0 to {user_input}')
# print(f'they are {list8}')

# ----------------------------------------------------------------

#while loops in python
number = 5
# while number < 10:
    # print(f'{number} is smaller than 10')

# user_number = int(input('Enter your number : '))
# while user_number < 10:
    # print(f'{number} is smaller than 10')
# else:
    # print(f'{user_number} is bigger than 10')

target_number = 10
sum_of_numbers = 0
i = 1
# print(i)
# while i < target_number:
#     sum_of_numbers = sum_of_numbers + i
#     i = i + 1
#     print(i)
# print(f'\n{sum_of_numbers}')