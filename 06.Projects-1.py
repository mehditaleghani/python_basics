# question 1
# name = input('Enter your name : ')
# lastname = input('Enter your last name : ')

# print(lastname + ' ' + name)

# ----------------------------------------------------------------

# question 2
# word = input('Enter a word please : ')
# print(word.upper())
# print(word.lower())

# ----------------------------------------------------------------

# question 3
# number1 = int(input('Enter number 1 : '))
# number2 = int(input('Enter number 2 : '))
# number3 = int(input('Enter number 3 : '))
# mylist = [number1, number2, number3]
# mylist.sort()
# print(mylist)

#-----------------------------------------------------------------

# question 4
#Twinkle, twinkle, little star,
#    How I wonder what you are!
#        Up above the world so high,
#        Like a diamond in the sky.
#Twinkle, twinkle,
#    little star, How I wonder what you are!

# print(f'Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!')

# ----------------------------------------------------------------

# quesion 5
# number = int(input('Enter a number : '))
# if number % 2 == 0:
#     print(f'{number} is an even number!')
# else:
#     print(f'{number} is not even!')

# ----------------------------------------------------------------

# question 6
# word = input('Enter a word : ')
# print(word[0:4].lower() + word[4:])

# ----------------------------------------------------------------

# question 7
# Word = input('Enter a word : ')

# def myfunc(aWord):
#     return(aWord)

# ListWord = list(Word)

# start = ListWord[0]
# poped = ListWord.pop(-1)
# ListWord.append(start)
# ListWord.remove(ListWord[0])
# ListWord.insert(0, poped)

# myword = ''
# for i in ListWord:
#     myword = myword + i

# print(myfunc(myword))

# teacher method for previous question :
# def TechWord(str1):
#     return str1[-1:] + str1[1:-1] + str1[:1]
# print(TechWord('MistD'))

# ----------------------------------------------------------------

# question 8
# HtmlTag = input('Enter your html tag : ')
# UserWord = input('What you wanna put in tags ? ')

# def HtmlConstructor(Tag, Word):
#     print(f'<{Tag}>{Word}</{Tag}>')
#     # ContinueOrNot = input('Continue or not ? (y/n)')
#     # if ContinueOrNot == 'y':
#     #     HtmlConstructor(HtmlTag, UserWord)
#     # elif ContinueOrNot == 'n':
#     #     print('Bye Bye')

# HtmlConstructor(HtmlTag, UserWord)

# ----------------------------------------------------------------

# question 9
# def TripleSum(n1, n2, n3):
#     MySum = n1 + n2 + n3
#     if n1 == n2:
#         MySum = 0
#         print(MySum)
#     elif n1 == n3:
#         MySum = 0
#         print(MySum)
#     elif n2 == n3:
#         MySum = 0
#         print(MySum)
#     else:
#         print(MySum)
# TripleSum(32, 3, 33)

# ----------------------------------------------------------------

# quesion 10
# UserInput = 'the quick brown fox jumps over the lazy brown fox' 
# Sentence = UserInput
# SplitedSentence = Sentence.split(' ')
# MyDict = {}

# def RepeatCounterFunc(Sentence):
#     for i in SplitedSentence:
#         MyDict[i] = SplitedSentence.count(i)
#     return MyDict

# print(RepeatCounterFunc(UserInput))

# ----------------------------------------------------------------

# question 11
# UserInput = input('Enter a word or name : ')
# SlicedUserInput = UserInput[0:4]
# UpperCounter = 0

# def UpperCaser(UserInput):
#     global UpperCounter
#     for i in SlicedUserInput:
#         if i == i.upper():
#             UpperCounter += 1
#             if UpperCounter >= 2:
#                 UserInput = UserInput.upper()
#     return UserInput

# print(UpperCaser(UserInput))

# ----------------------------------------------------------------

# question 12
# MyTuple = ('M', 'e', 'h', 'd', 'i', 'T', 'a', 'l', 'e', 'g', 'h', 'a', 'n', 'i')
# str1 = ''
# for i in MyTuple:
#     str1 += i
# print(str1)

# ----------------------------------------------------------------

# question 13
# MyTuple = ('M', 'e', 'h', 'd', 'i')
# ListedMyTuple = list(MyTuple)
# ListedMyTuple.append('New Item')
# MyTuple= tuple(ListedMyTuple)
# print(MyTuple)

# ----------------------------------------------------------------

# question 14
# MyTuple = ('M', 'e', 'h', 'd', 'i')
# ListedMyTuple = list(MyTuple)
# ListedMyTuple.remove('M')
# MyTuple = tuple(ListedMyTuple)
# print(MyTuple)

# ----------------------------------------------------------------

# question 15
# MyTuple = ('M', 'e', 'h', 'd', 'i')
# Letter = 'M'
# print(Letter in MyTuple)

# ----------------------------------------------------------------

# question 16
# MyTuple = ('Mehdi')
# ListedMyTuple = list(MyTuple)
# print(len(ListedMyTuple))

# print(len(MyTuple))

# ----------------------------------------------------------------

# question 17
# MyTuple = ('Mehdi', 'Talegh', 'Mehdi', 214, 214, 1, 5, 12, 17, 6, 5, 213, 214)
# MyList = []

# for i in MyTuple:
#     MyList.append(MyTuple.count(i))
    
# MyList.sort()
# print(MyList[-1])

# ----------------------------------------------------------------

# question 18
# UserInput = 'MehD TaleghHani'
# FirstChar = UserInput[3]
# SecondChar = UserInput[-4]
# print(FirstChar + ' ' + SecondChar)

# ----------------------------------------------------------------

# question 19
# MyTuple = ('MehdiTaleghani')
# ListedyTuple = list(MyTuple)
# ListedyTuple.reverse()
# MyTuple = tuple(ListedyTuple)
# print(MyTuple)

# ----------------------------------------------------------------

# question 20
# UserInput = 'Key1'
# MyDict = {'Key1' : 1, 'Key2' : 2, 'Key3' : 3, 'Key4' : 4}

# def KeyChecker(UserInput):
#     if UserInput in MyDict.keys():
#         return f'{UserInput} exists in {MyDict}'
#     else:
#         return f'{UserInput} does not exists in {MyDict}'

# print(KeyChecker(UserInput))

# ----------------------------------------------------------------

# question 21
# UserInput = 'Key1'
# MyDict = {'Key1' : 1, 'Key2' : 2, 'Key3' : 3, 'Key4' : 4}

# def KeyChecker(UserInput):
#     if UserInput in MyDict.keys():
#         print(MyDict)
#         print('\nDeleting ... Done \n')
#         del MyDict[UserInput]
#         print(MyDict)
#     else:
#         pass

# KeyChecker(UserInput)

# ----------------------------------------------------------------

# question 22
# MyDict = {'Key1' : 1, 'Key2' : 2, 'Key3' : 3, 'Key4' : 4}

# def DictBeatify():
#     for i in MyDict.keys():
#         print(f'{i} ==> {MyDict[i]}')

# DictBeatify()
# # Teacher method :
# for DictKey, DictValue in MyDict.items():
#     print(DictKey, '==>', DictValue)

# ----------------------------------------------------------------

# question 23
# MyDict1 = {'Key1' : 1, 'Key2' : 2, 'Key3' : 3, 'Key4' : 4, '44' : 400}
# MyDict2 = {'Key1' : 100, 'Key2' : 200, '3' : 300, '4' : 400}
# MyDict1.update(MyDict2)
# print(MyDict1)

# ----------------------------------------------------------------

# question 24
# MyDict = {'Item1':100, 'Item2':-57, 'Item3':295}
# Sum = 0
# for i in MyDict.values():
#     Sum += i
# print(Sum)

# Teacher method :
# print(sum(MyDict.values()))

# ----------------------------------------------------------------

# question 25
# UserInput = input('Enter numbers : ')
# ListedUserInput = UserInput.split(',')
# print('List : ', ListedUserInput)
# TupledUserInput = tuple(ListedUserInput)
# print('Tuple : ', TupledUserInput)

# ----------------------------------------------------------------

# question 26
# MyList = ['Red', 'Yellow', 'Green', 'Blue', 'White', 'Pink']
# print(MyList[0])
# print(MyList[-1])

# ----------------------------------------------------------------

# question 27
# List1 = ['1', '2', '3', '4']
# List2 = ['1', '2']
# Differenc = []
# TargetList = ''
# NotTargetList = ''

# if len(List1) > len(List2):
#     TargetList = List1
#     NotTargetList = List2
# else:
#     TargetList = List2
#     NotTargetList = List1

# for i in TargetList:
#     if i not in NotTargetList:
#         Differenc += i

# print(Differenc)

# ----------------------------------------------------------------

# question 28
# MyList = ['M', 'e', 'h', 'd', 'i']
# for i in MyList:
#     print(i, end='')

# Teacher method :
# str1 = ''.join(MyList)
# print('\n'+str1)

# ----------------------------------------------------------------

# question 29
# List1 = [1, 2, 3]
# List2 = [4, 5]
# List3 = ['Mehdi', 'Taleghani']
# print(List1 + List2 + List3)

# ----------------------------------------------------------------

# question 30
# MySet2 = {'Mehdi', 'Taleghani', 'x', 'y', 2, 6, 1, 3, 6}
# MySet1 = {1, 2, 3, 4}

# ListedMySet1 = list(MySet1)
# ListedMySet2 = list(MySet2)

# print(set(ListedMySet2) - set(ListedMySet1))

# Teacher method : 
# x = set(ListedMySet2)
# print(x.difference(set(ListedMySet1)))

# ----------------------------------------------------------------

# question 31
# import random
# MyList = ['1', '2', '3', '4', '5']
# random.shuffle(MyList)
# print(MyList)

# ----------------------------------------------------------------

# question 32
# import random
# MyList = ['10', '20', '30', '40', '50']
# RandomFromMyList = MyList[random.randrange(5)]
# print(RandomFromMyList)

# ----------------------------------------------------------------

# question 33
# MyList = [3, 1, 6, 2, 4, 9, 7, 5, 8, 10]
# MyList.sort()
# NewList = []

# def SecBigNum():
#     global MyList
#     global NewList
    
#     for x in MyList:
#         for y in MyList:
#             if x == y:
#                 pass
#             if x < y:
#                 NewList.append(x)
#             else:
#                 pass

#     MyDict = {}
#     for i in NewList:
#         MyDict.update({i:0})

#     BiggestNumInMyList = set(MyList) - set(NewList)
#     BiggestNumInMyListNewV = list(BiggestNumInMyList)[0]

#     SmallestNumInMyList = next(iter(MyDict))
#     del MyDict[next(iter(MyDict))]
#     SecondSmallestNumInMyList = next(iter(MyDict))

#     return f'Smallest number after {SmallestNumInMyList} is : {SecondSmallestNumInMyList}\nalso Biggest number in this list is {BiggestNumInMyListNewV}'

# print(SecBigNum())

# ChatGBT idea to remove duplicate items : 
# UniqueList = list(set(MyList))  # Remove duplicates
# UniqueList.sort()

# ----------------------------------------------------------------

# question 34
# MyList = [2, 3, 6, 7, 1, 4, 10, 11, 2, 5, 4, 3, 0, 0]
# MyListNewV = list(set(MyList))
# BiggestOrSmallest = input('Biggest number or smallest ? (b/s)')
# if BiggestOrSmallest == 'b':
#     print(f'Biggest number of MyList is : {MyListNewV[-1]}')
# elif BiggestOrSmallest == 's':
#     print(f'Biggest number of MyList is : {MyListNewV[0]}')

# ----------------------------------------------------------------

# question 35
# method 1
MyList = [1, 2, 3, 4, 4, 5, 6, 6, 7, 2, 2, 7, 8, 9, 1]
# MyList = list(set(MyList))
# print(MyList)

# method 2
# MyDict = {}
# for i in MyList:
#     MyDict.update({i:0})

# NewList = []
# for i in MyDict.keys():
#     NewList.append(i)

# print(NewList)

# ----------------------------------------------------------------

# question 36
# MySet = {7, 12, 19, 11, 15, 20, 5, 3, 6}
# Sum = 0
# for i in MySet:
#     Sum += i

# Sumx = Sum / len(MySet)
# RoundedSumX = round(Sumx, 2)

# print(RoundedSumX)

# ----------------------------------------------------------------

# question 37
# Sum1 = 0
# Sum2 = 1
# # print(Sum1)
# while Sum1 <= 50:
#     Sum1 , Sum2 = Sum1 + Sum2 , Sum1
#     print(Sum1)

# ----------------------------------------------------------------

# question 38
# for i in range(7):
#     if i == 3 or i == 6:
#         continue
#     else:
#         print(i)

# ----------------------------------------------------------------

# question 39
# import random
# RandomNumber = random.choice(range(9))
# # print(RandomNumber)

# UserInput = int(input('Enter a number : '))

# while UserInput != RandomNumber:
#     UserInput = int(input('Enter a number : '))
#     if UserInput == RandomNumber:
#         print(f'Yay UserInput:{UserInput} was same as RandomNumber:{RandomNumber}')

# ----------------------------------------------------------------

# question 40
# def Calculator(Operation):
#     if Operation == '+':
#         def Sum(Number1, Number2):
#             SumAllNums = Number1 + Number2
#             return f'Sum of {Num1} and {Num2} is : {SumAllNums}'
#         Num1 = int(input('Enter number 1 : '))
#         Num2 = int(input('Enter number 2 : '))
#         print(Sum(Num1, Num2))
#         ContinueOrNot = input('Do you want continue or no ? enter Y for YES and enter N for No ? ')
#         if ContinueOrNot == 'Y':
#             WhatOperation = input('What operation you wanna do ? + - * / ? ')
#             Calculator(WhatOperation)
#         else:
#             pass
#     elif Operation == '-':
#         def Minus(Number1, Number2):
#             MinusNums = Number1 - Number2
#             return f'{Num1} Minus {Num2} : {MinusNums}'
#         Num1 = int(input('Enter number 1 : '))
#         Num2 = int(input('Enter number 2 : '))
#         print(Minus(Num1, Num2))
#         ContinueOrNot = input('Do you want continue or no ? enter Y for YES and enter N for No ? ')
#         if ContinueOrNot == 'Y':
#             WhatOperation = input('What operation you wanna do ? + - * / ? ')
#             Calculator(WhatOperation)
#         else:
#             pass
#     elif Operation == '*':
#         def Times(Number1, Number2):
#             TimesNums = Number1 * Number2
#             return f'{Num1} Times {Num2} : {TimesNums}'
#         Num1 = int(input('Enter number 1 : '))
#         Num2 = int(input('Enter number 2 : '))
#         print(Times(Num1, Num2))
#         ContinueOrNot = input('Do you want continue or no ? enter Y for YES and enter N for No ? ')
#         if ContinueOrNot == 'Y':
#             WhatOperation = input('What operation you wanna do ? + - * / ? ')
#             Calculator(WhatOperation)
#         else:
#             pass
#     elif Operation == '//':
#         def Devide(Number1, Number2):
#             DevideNums = Number1 / Number2
#             return f'{Num1} Devide at {Num2} : {DevideNums}'
#         Num1 = int(input('Enter number 1 : '))
#         Num2 = int(input('Enter number 2 : '))
#         print(Devide(Num1, Num2))
#         ContinueOrNot = input('Do you want continue or no ? enter Y for YES and enter N for No ? ')
#         if ContinueOrNot == 'Y':
#             WhatOperation = input('What operation you wanna do ? + - * / ? ')
#             Calculator(WhatOperation)
#         else:
#             pass

# WhatOperation = input('What operation you wanna do ? + - * / ? ')
# Calculator(WhatOperation)

# ----------------------------------------------------------------

# question 41
import random
CharactarsList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQWRSTUVWXYZ0123456789!@#$%^&*()_+'
MyList = []

PasswordLength = int(input('Enter the passwords length password length ? '))
HowManyPasswords = int(input('How many passwords you want ? '))

def PasswordGenerator():
    global MyList
    
    for i in CharactarsList:
        if i not in MyList:
            RandomCharacter = random.choice(CharactarsList)
            MyList.append(RandomCharacter)
    
    for i in MyList[:PasswordLength]:
        print(i, end='')
    print('')
    MyList = []
        
for i in range(HowManyPasswords):
    PasswordGenerator()

