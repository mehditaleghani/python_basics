'''
Table of Contents

    Built-in Exceptions
        Exception context
            __context__
            __cause__
            __suppress_context__
        Inheriting from built-in exceptions
        Base classes
            BaseException
                args
                with_traceback()
                __traceback__
                add_note()
                __notes__
            Exception
            ArithmeticError
            BufferError
            LookupError
        Concrete exceptions
            AssertionError
            AttributeError
            EOFError
            FloatingPointError
            GeneratorExit
            ImportError
                name
                path
            ModuleNotFoundError
            IndexError
            KeyError
            KeyboardInterrupt
            MemoryError
            NameError
            NotImplementedError
            OSError
                errno
                winerror
                strerror
                filename
                filename2
            OverflowError
            PythonFinalizationError
            RecursionError
            ReferenceError
            RuntimeError
            StopIteration
                value
            StopAsyncIteration
            SyntaxError
                filename
                lineno
                offset
                text
                end_lineno
                end_offset
            IndentationError
            TabError
            SystemError
            SystemExit
                code
            TypeError
            UnboundLocalError
            UnicodeError
                encoding
                reason
                object
                start
                end
            UnicodeEncodeError
            UnicodeDecodeError
            UnicodeTranslateError
            ValueError
            ZeroDivisionError
            EnvironmentError
            IOError
            WindowsError
            OS exceptions
                BlockingIOError
                    characters_written
                ChildProcessError
                ConnectionError
                BrokenPipeError
                ConnectionAbortedError
                ConnectionRefusedError
                ConnectionResetError
                FileExistsError
                FileNotFoundError
                InterruptedError
                IsADirectoryError
                NotADirectoryError
                PermissionError
                ProcessLookupError
                TimeoutError
        Warnings
            Warning
            UserWarning
            DeprecationWarning
            PendingDeprecationWarning
            SyntaxWarning
            RuntimeWarning
            FutureWarning
            ImportWarning
            UnicodeWarning
            EncodingWarning
            BytesWarning
            ResourceWarning
        Exception groups
            ExceptionGroup
            BaseExceptionGroup
                message
                exceptions
                subgroup()
                split()
                derive()
        Exception hierarchy
'''
# there are a complete list of python built in errors above in start of 2025

'''
try : Let us to execute a block of code
except : Let us to handle error of the "try block code"
else : here we say what should be execute if there was no error
finally : here is for the code that it must be executed in any way
'''

# ----------------------------------------------------------------
# let's handle some error :
try:
    with open('file.txt') as f:
        print(f.read())
        # as you see , this shows an error : "FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'"
        # to handle it we put this block of code into a "try", so that's why we are in a try now :D

except FileNotFoundError: # except ErrorNameHere:
    print('Sorry we can\'t find this file!')
    # now instead of "FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'"
    # we see "Sorry we can\'t find this file!" :D

# another example :

# try: # uncomment these block
#     with open('file.txt') as f:
#         import asdasdasd

# except FileNotFoundError:
#     print('File Not Found Error!')
# except ModuleNotFoundError:
#     print('Module Not Found Error')

# # or we can do it in this way :
# except (FileNotFoundError, ModuleNotFoundError):
#     print('Error, please check spelling and be sure the file or module exists!')

# # i personally like this way :
# except ModuleNotFoundError as e:
#     print(e) # it prints a build in text to handle errors

# else: # and if try was True and there was no Error in try, else commands with execute
#     print(f.read())

# another example :
try:
    file = open('/home/mehdi/Documents/Python/000_Python_Basics/README.txt')

except FileNotFoundError as error:
    print(error)

else:
    print(file.readline())
    
finally:
    file.close()

# ----------------------------------------------------------------
# and now we learn how to call errors and how to make custom errors :
print('----------------------------------------------------------------')
print()
try:
    f = open('/home/mehdi/Documents/README.txt')
    if f.name == 'README.txt':
        raise ModuleNotFoundError
except FileNotFoundError as error:
    print(error)

# now let's make our own error :
# we wanna write this program without print()
def guess_number():
    user_input = int(input('Enter a number : '))
    if user_input>10:
        print('Value is big')
        guess_number()
    elif user_input<10:
        print('Value is small')
        guess_number()
    else:
        print('Nice Job')

guess_number()

import time
print('Good job now you are entering phase 2 of the game!')
time.sleep(2)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)

class Error(Exception):
    pass
class ValueIsSmall(Error):
    pass
class ValueISBig(Error):
    pass

number = 100
while True:
    try:
        u_number = int(input('Enter your number : '))
        
        if u_number<number:
            raise ValueIsSmall
        elif u_number>number:
            raise ValueISBig

        print('Nice job!')
        break

    except ValueIsSmall:
        print('Value Is Small, Try again!')
    except ValueISBig:
        print('Value Is Big, Try again!')
    except ValueError as error:
        print(error)



