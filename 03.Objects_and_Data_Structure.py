# Printing a simple message
print("Hello world\n")

# ----------------------------------------------------------------

# Variables
var = "random"          # String variable
_var = 123              # Integer variable
var_a = var_b = var_c = 1  # Multiple variables initialized to the same value
# print(var_a)          # Uncomment to print var_a
# print(var_b)          # Uncomment to print var_b
# print(var_c)          # Uncomment to print var_c

var_1, var_2, var_3 = 1, 2, 3  # Multiple variables with different values
# print(var_1)         # Uncomment to print var_1
# print(var_2)         # Uncomment to print var_2
# print(var_3)         # Uncomment to print var_3

# ----------------------------------------------------------------

# Numbers
number = 123           # Integer
num = 100              # Another integer
age = 18               # Integer for age

# ----------------------------------------------------------------

# Strings
name = ' Mehdi '       # String with spaces
# print(f'"{name.strip()}"')  # Removes leading and trailing spaces
name_2 = "MehdiTaleghani"  # Concatenated name as string
_name3 = "Pahalvoon Ahmadi" # Another string variable

# ----------------------------------------------------------------

# Using del function
# print(_name3)         # Print the variable
# del _name3            # Delete the variable
# print(_name3)         # Causes an error because _name3 is deleted

# ----------------------------------------------------------------

# Int and Float Data Types
num = 3                # Integer
num_p = 3.14           # Float
# print(type(num))      # Print type of num
# print(type(num_p))    # Print type of num_p
num_float = float(num) # Convert int to float
# print(num_float)      # Print converted float value
num_p_int = int(num_p) # Convert float to int
# print(num_p_int)      # Print converted int value

# ----------------------------------------------------------------

# Math Operators
num_1 = 12
num_2 = 3
# print(num_1 + num_2)  # Addition
# print(num_1 - num_2)  # Subtraction
# print(num_1 * num_2)  # Multiplication
# print(num_1 / num_2)  # Division
# print(num_1 % num_2)  # Modulus
# print(num_1 ** num_2) # Exponentiation
# print(num_1 // num_2) # Floor division

# ----------------------------------------------------------------

# Relational Operators
num_1 = 12
num_2 = 3
# print(num_1 == num_2)  # Equal to
# print(num_1 != num_2)  # Not equal to
# print(num_1 >= num_2)  # Greater than or equal to
# print(num_1 <= num_2)  # Less than or equal to

# ----------------------------------------------------------------

# Assignment Variables
num_1 = 12
num_2 = 3
# num_3 = num_1 + num_2 # Assigning addition result to num_3
# Or we can do this:
# num_2 += num_1       # Increment num_2 by num_1
# print(num_2)         # Uncomment to see the updated value
# The same pattern works for all math operations:
# num_2 -= num_1
# num_2 *= num_1
# num_2 /= num_1

# ----------------------------------------------------------------

# Logical Operators (or & and)
math_score = 18
full_score = 17
# if math_score >= 18 and full_score >= 17:
#     print("Good Job")  # Both conditions are true

# if math_score >= 19 and full_score >= 17:
#     print("Good Job")
# else:
#     print("Stupid Kid")  # Executes if at least one condition is false

# if math_score >= 14 or full_score >= 17:
#     print("Good Job")  # At least one condition is true
# else:
#     print("Stupid Kid")

# ----------------------------------------------------------------

# Identity Operators
num_1 = 12
num_2 = 3
name = 'Mehdi'
# print(num_1 is num_2)       # False, different objects
# print(num_1 is not num_2)   # True, objects are not the same
# print('m' in name)          # False, lowercase 'm' not in 'Mehdi'
# print('M' in name)          # True, uppercase 'M' is in 'Mehdi'
# print('Meh' in name)        # True, substring matches
# print('mehdi' in name)      # False, case-sensitive
# print('M' not in name)      # False, 'M' is present
# print('m' not in name)       # True, 'm' is not in 'Mehdi' (case-sensitive)
# print('madsdfaufa' not in name)  # True, string not found in 'Mehdi'

# print('m' not in name)       # True, 'm' is not in 'Mehdi' (case-sensitive)
# print('madsdfaufa' not in name)  # True, string not found in 'Mehdi'

# ----------------------------------------------------------------

# Using id() function
num_1_id = id(num_1)  # Get the memory ID of num_1
num_2_id = id(num_2)  # Get the memory ID of num_2
# print(num_1_id is num_2_id)  # False, different memory IDs
# print(num_1_id is num_1_id)  # True, same memory ID

# ----------------------------------------------------------------

# Checking elements in a list
mylist = [1, 2, 3, 4]
# print(1 in mylist)   # True, 1 is in mylist
# print(3 in mylist)   # True, 3 is in mylist
# print(7 in mylist)   # False, 7 is not in mylist

# ----------------------------------------------------------------

# Strings Data Type
name = 'Mehdi'
last_name = 'Taleghani'
big_string = '''
my name is Mehdi and
my lastname is 
Taleghani
and i like body building
'''
# print(big_string)  # Print multiline string

# String slicing
# print(name)          # Print entire string
# print(name[:])       # Print entire string using slice
# print(name[0:3])     # 'Meh'
# print(name[0:4])     # 'Mehd'
# print(name[0:5])     # 'Mehdi'
# print(name[1:5])     # 'ehdi'
# print(name[2:5])     # 'hdi'
# print(name[-1])      # 'i', last character
# print(name[-5])      # 'M', first character (reverse index)

# ----------------------------------------------------------------

# Concatenation and Repetition
name = 'Mehdi '
last_name = 'Taleghani'
# print(name + last_name)  # Concatenation: 'Mehdi Taleghani'
# print(name * 3)          # Repetition: 'Mehdi Mehdi Mehdi '

# ----------------------------------------------------------------

# Raw String and Escape Character
address = r'C:\users\nazanin\teacher\files'  # Raw string avoids escape processing
# print(f'address is {address}')
address = 'C:\\users\\nazanin\\teacher\\files'  # Explicit escape characters
# print(f'address is {address}')

# ----------------------------------------------------------------

# f-Strings
name = 'Mehdi'
lname = ' Taleghani'
# print(f'Hello my name is {name} and my lastname is{lname}')
# print(f'I gonna do some math ... 42 times 13 : {42*13}')
# print(
#     f'we can use fstrings in mutltilines\n'
#     f'this is how we do it\n'
#     f'it may be useful'
# )

# ----------------------------------------------------------------

# String Methods
name = 'mehdiii taleghani DSII'
# print(name.capitalize())    # Capitalize first letter
# print(name.count('i'))      # Count occurrences of 'i'

# print(name.isalnum())       # False, not all characters are alphanumeric
# print(name.isalpha())       # False, contains spaces
# print(name.isnumeric())     # False, contains letters

# print(name.isupper())       # False, not all letters are uppercase
# print(name.upper())         # Convert to uppercase

# print(name.islower())       # False, some letters are uppercase
# print(name.lower())         # Convert to lowercase

# print(name.isspace())       # False, contains non-space characters
# print(len(name))            # Length of the string

# Splitting a string
# print(name.split())         # Split by spaces
# print(name.split('i'))      # Split by 'i'
# print(name.split('e'))      # Split by 'e'

# Finding substrings
# print(name.find('mehdi'))   # Find starting index of 'mehdi'
# print(name.find('i'))       # Find first occurrence of 'i'
# print(name.find('T'))       # Find first occurrence of 'T'
# print(name.find('t'))       # Returns -1 if not found

# Replacing substrings
# print(name.replace('mehdi', 'x'))      # Replace 'mehdi' with 'x'
# print(name.replace('taleghani', ''))  # Remove 'taleghani'

# ----------------------------------------------------------------

# Using help() for string methods
# print(help(name.isupper))
# print(help(name.upper))
# print(help(name.replace))

# ----------------------------------------------------------------

# Lists
mylist = ['Mehdi', 'RezaMozafari', 1385, 1390, 'a', 16.2]
mylist_2 = [1997, 1846, 1921]
# print(mylist)           # Print the list
# print(len(mylist))      # Length of the list
mylist[2] = 1380         # Update an element
# print(mylist[2])       # Print updated element
# List Operations
mylist[2] = 1385  # Updating an element in the list
# print(mylist)
# print(mylist + mylist_2)  # Concatenation of two lists
# print(mylist * 3)         # Repetition of a list
# print('mehdi' in mylist)  # Case-sensitive check for element existence
# print('mehdi' in mylist or 'Mehdi' in mylist)  # Check for either case

# ----------------------------------------------------------------

# Slicing and Indexing Lists
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# fruits2 = fruits[:fruits.index("cherry")]  # Elements up to "cherry"
# print(fruits2)
# print(fruits[:fruits.index('orange')])  # Elements up to "orange"

# ----------------------------------------------------------------

# List Methods
a = ['apple', 'banana', 'orange', 'MOZ']
b = [313, 414, 22, 21, 8293, 8294]
# print(len(a))                   # Length of list
# print(max(a, key=len))          # Longest string in list
# print(max(b))                   # Maximum number in list
# print(min(b))                   # Minimum number in list
b.append(85)                      # Append element to list
# print(b)
a.append(75)                      # Append non-string element
# print(a)
# print(a.count('Apple'))         # Count occurrences (case-sensitive)
# print(a.count('apple'))

# ----------------------------------------------------------------

# Converting Tuples to Lists
tuple = ('banana', 'apple', 'orange', 'dodol')
convert_tuple_to_list = list(tuple)  # Convert tuple to list
# print(convert_tuple_to_list)

# ----------------------------------------------------------------

# Using range to Create Lists
c = list(range(5))  # List from 0 to 4
# print(c)
a.append(c)          # Append list as a single element
# print(a)
b.extend(c)          # Extend list by another list
# print(b)
c.insert(3, 7)       # Insert value at index
# print(c)
poped = a.pop()      # Remove and return last element
# print(poped)
removed = a.remove('apple')  # Remove specific element
# print(a)
a.reverse()          # Reverse list
# print(a)
b.sort()             # Sort list
# print(b)
b.sort(reverse=True) # Sort in descending order
# print(b)

# ----------------------------------------------------------------

# Joining Lists into Strings
g = ['apple', 'banana', 'orange', 'MOZ']
new_g = ' - '.join(g)  # Join elements with separator
# print(new_g)

# ----------------------------------------------------------------

# Tuples
tuple = ('apple', 123, 'banana', 75)
# print(type(tuple))  # Tuple data type

tuple1 = (1, 2, 3)
tuple2 = (4,)
# print(type(tuple2))  # Tuple with single element (requires trailing comma)
tuple3 = tuple1 + tuple2  # Concatenation
# print(tuple3)

# ----------------------------------------------------------------

# Dictionaries (JSON-like structures in Python)
mydict = {'name': 'mehdi', 'age': 18, 'Job': 'ITman'}
mydict['name'] = 'Mehdi'  # Updating value
# print(mydict['name'])
mydict['newObject'] = 'a new object'  # Adding a key-value pair
# print(mydict)
del mydict['newObject']  # Deleting a key-value pair
# print(mydict)
mydict.clear()           # Clearing dictionary
# print(mydict)

# Dictionary Methods and Nested Dictionaries
mydict = {'dict-1': {'name-1': 'Mehdi', 'name-2': 'Mamad'},
          'dict-2': {'lastname-1': 'taleghani', 'lastname-2': 'mamoshian zade'}}
# print(mydict['dict-1']['name-1'] + ' ' + mydict['dict-2']['lastname-1'])

mydict['dict3'] = {}
mydict['dict3']['job1'] = 'ITman'
mydict['dict3']['job2'] = 'Pstar'
# print(mydict)

# ----------------------------------------------------------------

# Sets and Set Operations
myset = {1, 2, 3, 4}
myset.add('Hello')  # Add a single element
# print(myset)
myset.add(('tuple', 123))  # Add an immutable tuple
# print(myset)
myset.update([227000, 'new update V2'])  # Add multiple elements
# print(myset)
myset.discard(227000)  # Remove an element (no error if not present)
# print(myset)
myset.add(25)
myset.remove(25)  # Remove element (error if not present)
# print(myset)

# Set Unions, Intersections, and Differences
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# print(set1 | set2)  # Union
# print(set1 & set2)  # Intersection
# print(set1 - set2)  # Difference (elements in set1 not in set2)
# print(set2 - set1)  # Difference (elements in set2 not in set1)
# print(set1 ^ set2)  # Symmetric difference (elements in either, not both)

