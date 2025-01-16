
import sqlite3

# now we gonna make a connection to our database
# my variable for connecting to db :
conn = sqlite3.connect('database_name.db')
# variable conn will connect to database named 'database_name.db' 
# tip : if database_name.db is not created yet, connect method first make the database and after it do the connection procces

# sometimes we are testing our application and we don't want put database on hard disk, we can use this method :
conn = sqlite3.connect(':memory:')
# this will create the database and connect to it but all of these will happen in memory not in hard disk

# ----------------------------------------------------------------

# now we are gonna make a database and learn how to make tables :
conn = sqlite3.connect('database_name.db')

# for intracting with database we need to use a cursor, this is how we make a cursor :
cursor = conn.cursor()

# now we are gonna make a table :
#cursor.execute('SMALL SQL QUERY')

#cursor.execute('''BIG
#                  SQL
#                  QUERY
#                  ''')


#                                      TABLE NAME HERE # table name should be lowercase
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                  name text,
                  lastname text,
                  salary integer,
                  rate real
                  )''')

'''
employees is table name
name, lastname, salary and rate these are our columns
text, integer and real are our data types, and these are all sqlite3 datatypes :
NULL, INTEGER, REAL, TEXT, BLOB | for more details : https://www.sqlite.org/datatype3.html
'''

# after adding some changes to database we need to save those changes :
conn.commit() # we can't use cursor because this is not a SQL query

# we can add some more changes 
# change 2
# conn.commit()
# change 3
# conn.commit()

# and finaly we close the database
# conn.close() # i comment this because :
# after closing database we can't intract with it, so always close it when everything is done.

'''
as you see now we have daabase_name.db as a database in $(pwd)
about 'CREATE TABLE IF NOT EXISTS' we can write 'CREAT TABLE tablename', but if we
run code for a second time we get error that this table is exists , so for handling
it we use 'CREATE TABLE IF NOT EXISTS'
'''

# ----------------------------------------------------------------

# okay now let's insert some data into database_name.db :
#cursor.execute('INSERT INTO employees VALUES("Mehdi", "Taleghani", "200", "8.7")')
# after we run this code for first time we comment it, because each time we run it
# it will insert those data to a new line of our table
#conn.commit() 

cursor.execute('SELECT * FROM employees') # but this is not recommanded because this method use lot's of memory
# print(cursor.fetchall())

cursor.execute('SELECT * FROM employees WHERE name="Mehdi"')
# print(cursor.fetchmany(1)) # none=1 | we can say 2, 3 or more and it will return more lines
# print(cursor.fetchone())

# now we wanna use a class to creat some object and insert those objects and their properties to our database
from databases_class import Employee
# if we use import databases_class we need to use it in this way : databases_class.Employee
# so for making it shorter and easier to use we exactly import Employee from databases_class

emp1 = Employee('Armin', 'Bizhani', 200, 8.3)
emp2 = Employee('Mehdi', 'Taleghani', 300, 9.4)
emp3 = Employee('Zeinab', 'Bavali', 300, 9.1)

# this method is a good and strong method but syntax is a bit hard
# cursor.execute('INSERT INTO employees VALUES (:first, :lastname, :salary, :rate)' , {'first' : emp1.name, 'lastname' : emp1.lastname, 'salary' : emp1.salary, 'rate' : emp1.rate})

# this one is simple in syntax but it's hard for debbug
# cursor.execute('INSERT INTO employees VALUES (?, ?, ?, ?)' , (emp2.name, emp2.lastname, emp2.salary, emp2.rate))

cursor.execute('SELECT * FROM employees')
# print(cursor.fetchall())

# ----------------------------------------------------------------

# now let's make the code better :
def insert_emp(emp):
    cursor.execute('INSERT INTO employees VALUES (:name, :lastname, :salary, :rate)' , {'name':emp.name, 'lastname':emp.lastname, 'salary':emp.salary, 'rate':emp.rate})
    print(f'{emp.name} {emp.lastname} added to employees table.')
    conn.commit()

def whois(emp):
    cursor.execute('SELECT * FROM employees WHERE name=:name' , {'name':emp.name})
    print(cursor.fetchone())

# get_emp_by_name(emp1)

def show_all_emps():
    cursor.execute('SELECT * FROM employees')
    return(cursor.fetchall())

def delete_emp(emp):
    cursor.execute('DELETE FROM employees WHERE name=:name AND lastname=:lastname' , {'name':emp.name, 'lastname':emp.lastname})
    print(f'{emp.name} {emp.lastname} was deleted from employees succefully.')
    conn.commit()
    
def update_salary(emp, salary):
    print(f'old salary of {emp.name} was {emp.salary}')
    cursor.execute('UPDATE employees SET salary=:salary WHERE name=:name AND lastname=:lastname' , {'salary':salary, 'name':emp.name , 'lastname':emp.lastname})
    print(f'new salary for {emp.name} is {salary}')
    conn.commit()

def update_rate(emp, rate):
    print(f'old rate of {emp.name} {emp.lastname} was {emp.rate}')
    cursor.execute('UPDATE employees SET rate=:rate WHERE name=:name AND lastname=:lastname' , {'rate':rate, 'name':emp.name, 'lastname':emp.lastname})
    print(f'new rate for {emp.name} {emp.lastname} is {rate}')


whois(emp1)
whois(emp2)
whois(emp3)

'''
so what we did here ? we made a database and a table, after it we made all queries into
python functions, so now we don't need database knowledge anymore, we can insert, delete
select, update and etc to this database with python functions because we made functions 
for all SQlite3 quieries.
''' 

# ----------------------------------------------------------------

# now let's make the output that we have in terminal, a bit more human readable :
# pip install tabulate
from tabulate import tabulate # print(tabulate(emps))
# or 
import tabulate # print(tabulate.tabulate(emps))

# and we can make our output more human readable in this way :
emps = show_all_emps()
print(tabulate.tabulate(emps))




