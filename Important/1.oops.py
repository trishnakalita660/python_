# classes and object

class Person:

    amount = 0 #(Global, called as class variables) This belongs to the entire class
    # constructor
    def __init__(self, name, age) -> None:
        self.name = name
        self.age= age
        Person.amount += 1
    
    def __del__(self):
        Person.amount -= 1

    def __str__(self) -> str:
        return "Name : {}, Age: {}".format(self.name, self.age)



p1 = Person("Trishna", 22)
p2 = Person("Dhiman", 21)
print(p1)

print(Person.amount)
del p1
print(Person.amount)


# Inheritance

class Worker(Person):
    def __init__(self, name, age, salary) -> None:
        super().__init__(name, age)
        self.salary = salary
    
    def cal_LPA(self):
        return (self.salary * 12)

    #to overwrite base class 
    def __str__(self) -> str:
        text = super(Worker, self).__str__()
        text+= ", Salary {}".format(self.salary)
        return text

worker1 = Worker("A", 25, 1.5)

print(worker1)  #Name : A, Age: 25 <- Prints this as it is not overwritten

# # ~~~~~~~ operator overloading ~~~~~~~~~

# vector addition

class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __add__( self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__( self, other):
        return Vector( self.x - other.x, self.y-other.y)

    def __str__(self) -> str:
        return "X : {}, Y: {}".format(self.x, self.y)
v1 = Vector(1,2)
v2 = Vector(2,1)
v3 = v1.__add__(v2)
print(v3.x)