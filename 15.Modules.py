'''
So first let's discuss what are modules, we call other .py files a module
when i say import random, import os, import time, import my_module_1, all do same thing
they import everything from the imported file, this let us to use all variables,
functions, methods and etc from imported file
module name should be sneak case seprated with "_"
that's all for now
'''

# ----------------------------------------------------------------

import my_module_1
# now if i run the code every thing from my_module_1 will run in this code for example 
# the print('Module imported !') will be execute

# i can even print "var" from my_module_1
print(my_module_1.var)

# i have access to functions, methods and etc.
print(my_module_1.add(4,5))

# when you write print(my_module_1.) you can wait and check what things you have access
# for example here i have access to var and add function 
#print(my_module_1.))

# in this step "print(my_module_1.add())" can see docstring of add function
# print(my_module_1.add())

# we also can use dir function
import my_module_1
print(dir(my_module_1)) # You can see add and var ...

# sometimes modules are heavy adn big and make our code slow, but we just need a small
# part of that module, that's how we handle this problem :
from my_module_1 import add
from my_module_1 import var
from my_module_1 import var, add
from os import listdir

# sometimes module names are too long or we don't like them, we can handle it in this way :
import my_module_1 as mm
print(mm.var)

# ----------------------------------------------------------------

'''
You may ask how Python find modules
    current directory (we seen this right now)
    print(os.getcwd)
    
    Python PATH (here we have buildin modules)
    we can make a few modules and put them in a specefic directory and add it to
    Python PATH, but remember that script won't work for other people
        
    Python installed path (here we have modules installed with pip)
'''

'''
remember we can't enter absolute path of modules , some are buildin of python
the ones that we make our self should be in the exact path with our pain file
for example my main file is in "/home/user/Documents/xProject/script.py"
modules that im gonna use should be in this path "/home/user/Documents/xProject/my_module_1.py"
that's all
'''

# ----------------------------------------------------------------
# sometimes our packages are really big and heavy that's how we handle them :
import bigmodule # for example this package is so big

'''
There are 2 reasons that i can import a folder 

first one is that bigmodule folder is alongside of 15.Modules.py, so Python know have
access to it

second one is that bigmodules have a file named __init__.py , this file let python 
to know it as a module not a simple folder

if you check all folders of bigmodule you see there are 3 folders that all of them
have __init__.py inside their self, this let python to know all of these folders as
module and sub-modules or package and sub-packages
'''

# in this way we can make out file lighter and faster :
import bigmodule.folder1.file1

# this one is much more lighter :
from bigmodule.folder2 import file2

from bigmodule.folder3.file3 import where_we_are
print(where_we_are())

import bigmodule.folder1.file1 as bff1
print(bff1.where_we_are())

# ----------------------------------------------------------------

'''
Now let's learn a concept about __name__ , you may see this alot :

if __name__ == __main__:
    main()
    
let's discuss it :
'''

print(__name__) # output is "__main__"
#this means we run this code in a nomral way

# but let's write "print(__name__)" in file "my_module_2.py" and import it!
print()
print(f'Module name is : {__name__}')
import my_module_2
# wait what? it was __main__ when we executed it from my_module_2.py but when we
# imported it module name from __main__ changed to "my_module_2"

# well yea that's how it exavtly works :
if __name__ == '__main__':
    print('I have been executed directly')
else:
    print('I have been imported')

# developers use it in this way :
def main():
    print('These are some cods and stuff')
    
if __name__ == '__main__':
    main()

# and sometimes they don't write else: in this no one can't import this file as a module

# ----------------------------------------------------------------
# Now let's learn about pip , pip is a package or module manager for python, it let us
# to search, install, upgrade, unistall and etc of our python modules
# install it via "sudo apt install python3-pip"
# run "pip help" and take a look at it and for practice install and unistall a package
# btw there are some useful pip commands
'''
pip help
pip help "operaion" -> pip help install
pip install "module_name"
pip unistall "module_name"
pip list -> shows all installed modules and their version
pip list -o -> shows all out dated modules
pip install -U "module_name" -> update the module you want
pip install -r file.txt -> install all modules that their name is in file.txt
'''











