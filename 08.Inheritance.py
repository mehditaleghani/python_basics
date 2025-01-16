# we have this class named employe:

class Employee:
    hardwork = True
    salaryplus = 0.1
    
    def __init__(self, fname, lname, salary, rate):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.rate = rate

    def employee_data(self):
        return f'name : {self.fname} | last name : {self.lname} | salary : {self.salary} | hard work : {self.hardwork}'
    
    def salary_raise(self):
        self.salary += int(self.salary * self.salaryplus)
        
    def full_name(self):
        return f'{self.fname} {self.lname}'


emp1 = Employee('Armin', 'Bizhani', 200, 8.1)
emp2 = Employee('Mehdi', 'Taleghani', 300, 9.4)

# print(emp1.employee_data())

# print(f'{emp1.fname} get this salary : {emp1.salary}')
# emp1.salary_raise()
# print(f'{emp1.fname} get a salary raise : {emp1.salary}')


# now we wanna make another class that have all of these attributes "with some new stuff"
# we are going to let new class inheritance from employee class

class Developer(Employee):
    # developer class attrbutes
    salaryplus = 0.2 # we assign a new seprated value to salaryplus for developer class

    def __init__(self, fname, lname, salary, language): # we also add a new attribute for developer instances
        super().__init__(fname, lname, salary) # we do these do send values of developer instances to employee __init__
        self.language = language # but we don't send this new attribute to employee __init__ 

    def employee_data(self):
        return super().employee_data() + f'| programming language : {self.language}'

# so we made a subclass of employee, let's check help :
# print(help(Developer)) # read this stuff to understand how subclass works
    
dev1 = Developer('Mehdi', 'Taleghani', 200, 'Python')
dev2 = Developer('Hossein', 'AliNezhad', 200, 'Python')
dev3 = Developer('sajjad', 'shahroyi', 200, 'Python')

# print(dev1.employee_data())

# print(f'{dev1.fname} get this salary : {dev1.salary}')
# dev1.salary_raise()
# print(f'{dev1.fname} get a salary raise : {dev1.salary}') # as you see we had 0.2 salary raise not 0.1


class Manager(Employee):
    """Managers control employees, each manager control 5 employee"""
    
    def __init__(self, fname, lname, salary, emps = None):
        super().__init__(fname, lname, salary)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps

    def add_emp(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)
    
    def reomve_emp(self, emp):
        if emp in self.emps:
            self.emps.remove(emp)
    
    def show_all_emp(self):
        for emp in self.emps:
            print('--->', emp.full_name())

mngr1 = Manager('Shahin', 'Khabaz', 350, [dev1])

# mngr1.add_emp(dev2)
# print(mngr1.show_all_emp())

# ----------------------------------------------------------------

class Animal:
    def __init__(self):
        print('An instance of class Animal created')
    
    def animal_say(self):
        print('ANIMAL')


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('An instance of class Dog created')
    
    def animal_say(self):
        print('DOG')
    
    def dog_say(self):
        print('Hap Hap ...')

   
# dog = Dog()

# dog.animal_say()
# let's comment animal_say() in Dog ... and now run this code --->
# dog.animal_say()

# dog.dog_say() # Animal don't have this method but Dog have animal methods because of inheritance

# print(isinstance(dog, Dog))
# print(isinstance(dog, Animal)) # so dog is also instance of Animal too 

# print(issubclass(Dog, Animal))
# print(issubclass(Animal, Dog))

# ----------------------------------------------------------------

class A:
    def __init__(self):
        print('Class A')


class B:
    def __init__(self):
        print('Class B')


class C:
    def __init__(self):
        print('Class C')


# instance = C()




class A:
    def __init__(self):
        print('Class A')


class B:
    def __init__(self):
        print('Class B')


class C(A, B): # class C(B, A):
    def __init__(self):
        super().__init__()
        print('Class C')

        # A.__init__(self)
        # print('Class C')
        
        # B.__init__(self)
        # print('Class C')

instance = C()













