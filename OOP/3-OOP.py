# class Student:
#     school_name = 'James Madison'
#     def __init__(self, age, name, grade):
#         self.age = age
#         self.name = name
#         self.grade = grade
#     def grad_time(self):
#         return(17 - self.age)
# John = Student(15, 'John', 10)
# print(John.grad_time())

# Class methods
# @classmethod
# cls is used to refer to the class just like self
# class Myclass:
#     classVariable = 'test'

#     @classmethod
#     def demo(cls):
#         return cls.classVariable

# class Player:
#     teamName = 'Liverpool'

#     def __init__(self, name):
#         self.name = name
    
#     @classmethod
#     def getTeamName(cls):
#         return cls.teamName
# print(Player.getTeamName())

# Static method
# Limited to class only and not objects
# Can be accessed using class name or object
# class Myclass:
#     @staticmethod
#     def demo():
#         print('I am a static method')

# class Player:
#     teamName = 'Liverpool'
#     def __init__(self, name):
#         self.name = name
#     @staticmethod
#     def demo():
#         print('I am a static method')

# p1 = Player('lol')
# p1.demo()
# Player.demo()

# To produce a useful result
# class BodyInfo:
#     @staticmethod
#     def bmi(weight, height):
#         return weight / (height ** 2)

# weight = 90
# height = 1.86
# print(BodyInfo.bmi(weight, height))

# Public attributes
# Can be accessed from everywhere (inside and outside of class)
# class Employee:
#     def __init__(self, ID, salary):
#         # all properties are public
#         self.ID  = ID
#         self.salary = salary
#     def displayID(self):
#         print('ID', self.ID)

# Steve = Employee(2345, 2500)
# Steve.displayID()


# Private attributes
# Cannot be accessed directly from outside of class
# Can be accessed from inside of a class
# class Employee:
#     def __init__(self, ID, salary):
#         self.ID  = ID
#         self.__salary = salary # salary is a private property
    
#     def tax(self): #accesed from inside a class
#         return self.__salary * 0.2

# Steve = Employee(2345, 2500)
# # print(Steve.__salary)
# print(Steve.tax)
