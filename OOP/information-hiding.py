# information hiding is a consent of hiding inner workings of a class
# providing the interface which the outside world can interact with the class 

# Components of data hiding
# 1. Encapsulation
# 2. Abstraction


# Encapsulation
# get and set
# A getter method allows reading the property's value
# A setter method allows modifying a property's value
# getProps() => value
# setProps(value)


# class User:
#     def __init__(self, username=None):
#         self.__username = username
#     def setUsername(self, x):
#         self.__username = x
#     def getUsername(self):
#         return (self.__username)
# Steve = User('Steve1')
# print(f'Before setting: {Steve.getUsername()}')
# Steve.setUsername('Steve2')
# print(f'After setting: {Steve.getUsername()}')


# Login app
# userName
# password
# login()


# Very bad example!!!
class User:
    def __init__(self, userName=None, password=None):
        self.userName = userName
        self.password = password

    def login(self, userName, password):
        if ((self.userName.lower() == userName.lower()) and (self.password == password)):
            print('Access Granted! :D')
        else:
            print('Access Denied! D:')
Steve = User('Steve', '12345')
# Steve.login('steve', '12345')
# Steve.login('steve', '123')
Steve.password = '6789' # made a new password and hacked 
Steve.login('steve', '6789')

