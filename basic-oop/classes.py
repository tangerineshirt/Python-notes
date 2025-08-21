class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    #this str function inside a class is used so that we can print the class only without 
    #referencing any properties. it needs a return value
    
    def myFunc(self):
        print("Hello world")

per = Person("John", 36)
per.myFunc()

class Student(Person): #this is inheritance. the student class has all the properties of Person
    def __init__(self, name, age, year):
        super().__init__(name, age) # this makes the child class have its own constructor wihtout overriding the parent
        self.graduation_year = year # you can add more properties. dont forget to add it to the init parameters
    def __str__(self):
       return f"My name is {self.name}. I am {self.age} years old. I will graduate in {self.graduation_year}"

x = Student("Gerni", 20, 2022)
print(x)
        