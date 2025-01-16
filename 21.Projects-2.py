# question 1
import calendar
import time

def show_calender():
    print('Hello , this is a program that asks you a year and a month, and show you calender of that month in that year :D')
    time.sleep(2)
    print('Enter a year for example : 1983')
    year = int(input('Year : '))
    print('Enter a month for example : 2 , or you can enter month name : april')
    month = int(input('month : '))
    print()
    return calendar.month(year,month)

# print(show_calender())

# ----------------------------------------------------------------
# question 2
from datetime import datetime, date

first_date = str(date(2025,1,2))
second_date = str(date(2025,1,11))
def say_difference():
    list1 = first_date.split('-')
    list2 = second_date.split('-')

    int_list1 = int(list1[2])
    int_list2 = int(list2[2])

    return int_list2 - int_list1

# print(say_difference())

# ----------------------------------------------------------------
# question 3
import os
# print(os.system('ls -la'))

# Teacher method :
import subprocess
# print(subprocess.call(['ls', '-la']))


# ----------------------------------------------------------------
# question 4
import os
# print(os.system('whoami'))
# print(os.system('id'))

# teacher method :
import getpass
# print(getpass.getuser())

# ----------------------------------------------------------------
# question 5
import os
# print(os.system('ping -c 1 localhost | grep "localhost"'))

# teacher method :
import socket
# print(socket.gethostbyname('localhost')) # or we can do this :
# print(socket.gethostbyname(socket.gethostname()))

# ----------------------------------------------------------------
# question 6
def get_number():
    try:
        number = int(input('Enter a number : '))
        print(f'Your entered "{number}"')
    except ValueError :
        print(f'please only enter numbers between 0-9 - don\'t enter strings or etc...')
        print()
        get_number()
    
# get_number()

# ----------------------------------------------------------------
# question 7
def is_valid():
        
    try:
        ip = input('Enter a valid IP : ')

        ip_subs = ip.split('.')

        int_ip_subs = []

        for i in ip_subs:
            int_ip_subs.append(int(i))

        if int_ip_subs[0] < 0 or int_ip_subs[1] < 0 or int_ip_subs[2] < 0 or int_ip_subs[3] < 0:
            print('This is not a valid ip address')
        elif int_ip_subs[0] > 255 or int_ip_subs[1] > 255 or int_ip_subs[2] > 255 or int_ip_subs[3] > 255:
            print('This is not a valid ip address')
        else:
            print('This is a valid IP')
    except ValueError:
        print('''Enter a valid IP
A valid IP is made of 4 numbers that are seprated with "."
This is an example : 192.168.120.168
Min number should be 0 and max number should be 255''')

# is_valid()

# Teacher method :
import socket

ipaddress = '127.0.0.1'

# try:
#     socket.inet_aton(ipaddress) # this make our ip address into a string and check is it valid or not ...
#     print('Valid ip address')
# except socket.error:
#     print('invalid ip address')

# ----------------------------------------------------------------
# question 8
# Teacher advice : go to 06.Projects-1.py , and solve all of that questions with OOP
class calculator():
    def __init__(self, r, p=3.14):
        self.r = r
        self.a2 = r*2
        self.p = p

    def calc_enviroment(self):
        env = self.a2 * self.p
        return env
    
    def calc_area(self):
        area = self.r * self.r * self.p
        return area
    
circle1 = calculator(3)
circle2 = calculator(5, 3)

print(circle1.calc_enviroment())
print(circle1.calc_area())

print(circle2.calc_enviroment())
print(circle2.calc_area())

# ----------------------------------------------------------------
# question 9
from random import randint
from os import system
from time import sleep

def script():
    while True:
        websites = ['google.com', 'duckduckgo.com', 'guthib.com', 'varzesh3.ir']
        random_website = websites[randint(0,3)]
        system(f'python3 -m webbrowser -t https://{random_website}')
        sleep(3)

# script()

# or we can do this :
import webbrowser

def swap_script():
    while True:
        websites = ['google.com', 'duckduckgo.com', 'guthib.com', 'varzesh3.ir']
        random_website = websites[randint(0,3)]
        webbrowser.open_new_tab(f'https://{random_website}')
        sleep(3)

swap_script()

# ----------------------------------------------------------------
# question 10
# make a script that works like mahak mobile app for managing money spent.

# ----------------------------------------------------------------
