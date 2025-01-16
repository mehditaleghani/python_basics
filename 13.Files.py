# Let's learn about reading in files

path_to_file = '/home/mehdi/Documents/Python/README.txt'

try:
    file = open(path_to_file)
    '''
    open(path_to_file) read file
    open(path_to_file, 'r') again read the file
    open(path_to_file, 'w') write in file
    open(path_to_file, 'a') append things to file
    '''
    # some command here
    # if a == b :
finally:
    file.close() # and finally we close the file to save memory

# or we can use the new method :
with open(path_to_file, 'r') as f:
    print(f) # f stands for file
    print(f.name)
    print(f.mode)
    '''print(f.read()) # we use read method for small files like 1000 lines, it's better to use readlines(), imagine 100000 lines enter memory in 1 second :D'''
    '''print(f.readlines()) # this load the lines 1 by one and it's a little slower but it don't swap memory'''
    '''print(f.readline()) # this one read only 1 line but it's even better than read lines, we can read all lines with a for loop :'''
    # for i in f:
    #     print(i, end='')
    
# and when we are out of indent f(our file) is closed automatically so we save our memory
# so th proper way for showing a file is this :
# with open(path_to_file) as myfile:
#     for i in myfile:
#         print(i, end='')

with open(path_to_file) as myfile:
    text = myfile.read(10) # this reads the first 10 character, also we can use print(text, end='')
    print(text)
    text = myfile.read(10) # this reads the next 10 character, also we can use print(text, end='')
    print(text)
    text = myfile.read(1) # this reads the first 1 character, also we can use print(text, end='')
    print(text)

print()
with open(path_to_file) as myfile:
    text = myfile.read(10)
    print(text)
    
    myfile.seek(17)
    # seek control the cursor position , we can change the cursor position to change what are next characters that will be print
    text = myfile.read(6)
    print(text)
    
    myfile.seek(0) # i move cursor to character 0 and print the first 4 character : 
    text = myfile.read(4)
    print(text) 

# ----------------------------------------------------------------
# Now let's learn about writing in files
path_to_file = '/home/mehdi/Documents/Python/WRITEME.txt'

with open(path_to_file, 'w') as file:
    file.write('This file made with "w" method in python open function!')
    file.write('The line will be append to previous line')
    # write() can make file in the path if it does not exists, if it exist it rewrite the file content
    # we also can use seek() to stoping the full rewrite 

with open(path_to_file, 'a') as file: # and this is append method
    file.write('Some new text will be append to WRITEME.txt')
    
with open(path_to_file, 'w', encoding='utf-8') as file: # for writing persian we use 'utf-8' encoding
    file.write('This file made with "w" method in python open function!')

path_to_file1 = '/home/mehdi/Documents/Python/README.txt'
path_to_file2 = '/home/mehdi/Documents/Python/WRITEME.txt'
# we gonna put content of file1 in file2 : 
with open(path_to_file1, 'r') as file1:
    with open(path_to_file2, 'w') as file2:
        for line in file1:
            file2.write(line)

# to delete a file : 
import os
os.remove("/home/mehdi/Documents/Python/WRITEME.txt") 

# check of exists, after it delete : 
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 

# ----------------------------------------------------------------

print(os.getcwd()) # current working directory
os.chdir('/home/mehdi/Documents/Python/') # we indicate the new working directory
print(os.getcwd()) # as you see new we are in '/home/mehdi/Documents/'

os.mkdir('NewDir') # this one make a new directory named NewDir
os.rmdir('NewDir') # and now we deleted NewDir

# os.remove('WRITEME.txt') # we delete WRITEME.txt :D, if you want it comment this line and run the code and 'w' method will write it .

print(os.listdir()) # this one works like ls -la
os.chdir('/home/mehdi')
print(os.listdir())
print(os.chdir('/home/mehdi/Documents/Python/'))

# os.rename('x.txt', 'newname.txt') # this one change x.txt to newname.txt

# print(os.stat('13.Files.py').st_ctime)

user_directory = '/home/mehdi'
print(os.path.join(user_directory, 'Desktop'))




















