# Initializing Objects
# __init__
# What is an initializer?
# the first parameter __init is self

# class Employee:
#     def __init__(self, ID = None, salary = 0, department = None):
#         self.ID = ID
#         self.salary = salary
#         self.department = department


# Steve = Employee(123453, 2500, 'IT')
# Mark = Employee()
# print('ID = ', Steve.ID)
# print('Department:', Steve.department)
# print('Salary: ', Steve.salary)
# print('--------------')
# print('ID = ', Mark.ID)
# print('Department:', Mark.department)
# print('Salary: ', Mark.salary)

# define class variables and instance variables
# class Player:
#     teamName = 'Liverpool'
     
#     def __init__(self, name):
#         self.name = name
# p1 = Player('Mark')
# p2 = Player('Steve')

# print('Name:', p1.name)
# print('Team name', p1.teamName)

# print('Name:', p2.name)
# print('Team name', p1.teamName)

# class Player:
#     teamName = 'Manchester United'
#     teamMembers = []

#     def __init__(self, name):
#         self.name = name
#         self.formerTeam = []
#         self.teamMembers.append(self.name)

# p1 = Player('Steve')
# p2 = Player('Mark')

# print('Name: ', p1.name)
# print('Team Members: ')
# print(p1.teamMembers)
# print('----------')
# print('Name: ', p2.name)
# print('Team Members: ')
# print(p2.teamMembers)