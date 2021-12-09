from stack import *

def rev_str(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    reverse = ''
    while not stack.is_empty():
        reverse += stack.pop()
    return reverse

stack = Stack()
input_string = 'World'
print(rev_str(stack, input_string))