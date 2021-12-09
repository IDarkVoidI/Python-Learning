# Automization
# Reusability
# A function is a reusable set of operation
# def findMin(val1, val2):
#     if isinstance(val1, str) and isinstance(val2, str) == 'str':
#         if len(val1) > len(val2):
#             return val2
#         else:
#             return val1
#     elif isinstance(val1, int) and isinstance(val2, int):
#         if val1 > val2:
#             return val2
#         else:
#             return val1


# answer = findMin('Spiderman', 'Batman')
# answer2 = findMin(1, 5)
# print(answer)

# random_string = 'This is a string'
# print(random_string.find('is'))

# len() is a function
# .find() is a method because it comes after a dot


# lambda parameter: expression

# triple = lambda num: num * 3 # assigned a lambda to a variable triple
# print(triple(10))

# concat_strings = lambda a, b, c: a[0] + b[0] + c[0]

# print(concat_strings('World', 'Wide', 'Wibe'))

# my_func = lambda num: 'High' if num > 50 else 'Low'

# print(my_func(60))

# def add(n1, n2):
#     return n1 + n2


# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2


# def calculator(operation, n1, n2):
#     return operation(n1, n2)  # Using the 'operation' argument as a function


# result = calculator(multiply, 10, 20)
# print(result)
# print(calculator(add, 10, 20))

# def calculator(operation, n1, n2):
#    return operation(n1, n2)  # Using the 'operation' argument as a function

# result = calculator(lambda n1, n2: n1*n2, 10, 30) 
# print(result)

# num_list = [1, 3, 55, 66, 77]

# double_list = map(lambda n: n*2, num_list)
# greater_than_10 = list(filter(lambda n: n > 10, num_list))
# print(greater_than_10)
# print(list(double_list))