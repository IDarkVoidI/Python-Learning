# Task 1
# class Point:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def sqSum(self):
#         x = self.x ** 2
#         y = self.y ** 2
#         z = self.z ** 2
#         return x + y + z
# p1 = Point(1, 3, 5)
# print(p1.sqSum())

# Task 2-3
# Implement a method – totalObtained – in the Student class that calculates total marks of a student.
# name = Mark
# phy  = 80
# chem = 90 
# bio  = 40
# Percentage = (marks obtained / total marks) x 100
# class Student:
#     def __init__(self, phy, chem, bio):
#         self.phy = phy
#         self.chem = chem
#         self.bio = bio
#     def totalObtained(self):
#         total = self.phy + self.chem + self.bio
#         return total
#     def percentage(self):
#         answer = (self.totalObtained()/300) * 100
#         return answer
# marks = Student(80, 90, 40)
# print(marks.percentage())


# Task 1

# Write a Python class called Calculator by completing the tasks below:

# Task 1: Create an initializer: properties: num1 and num2

# task 2:  Methods: add(), sub(), mult(), divide()

# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#     def add(self):
#         addition = self.num1 + self.num2
#         return addition
#     def sub(self):
#         subtraction = self.num1 - self.num2
#         return subtraction
#     def mult(self):
#         multiplication = self.num1 * self.num2
#         return multiplication
#     def divide(self):
#         division = self.num1 / self.num2
#         return division
# answer = Calculator(12, 2)
# print(answer.add())