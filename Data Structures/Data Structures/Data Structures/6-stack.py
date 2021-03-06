# # A
# # B
# # C
# # D
#
# # Stack data structure
#
 
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


myStack = Stack()
myStack.push('A')
myStack.push('B')
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())

#

# 1.  We iterate through the characters of the string
# 2.  if we get an opening bracket, push it onto the stack
# 3.  If we encounter a closing bracket, pop off an element from the stack and match it with the
# closing bracket. If it is an opening bracket and of the same type as the closing bracket,
# we conclude it is a successful match and move on. If it’s not,
# we will conclude that the set of brackets is not balanced.
# 4. Stack is empty => 1 || 0


# def is_match(p1, p2):
#     if p1 == "(" and p2 == ")":
#         return True
#     elif p1 == "{" and p2 == "}":
#         return True
#     elif p1 == "[" and p2 == "]":
#         return True
#     else:
#         return False


# def is_paren_balanced(paren_string):
#     s = Stack()
#     is_balanced = True
#     index = 0

#     while index < len(paren_string) and is_balanced:
#         paren = paren_string[index]
#         if paren in "([{":
#             s.push(paren)
#         else:
#             if s.is_empty():
#                 is_balanced = False
#                 break
#             else:
#                 top = s.pop()
#                 if not is_match(top, paren):
#                     is_balanced = False
#                     break
#         index += 1

#     if s.is_empty() and is_balanced:
#         return True
#     else:
#         return False


# print("String : (((({})))) Balanced or not?")
# print(is_paren_balanced("(((({}))))"))

# print("String : [][]]] Balanced or not?")
# print(is_paren_balanced("[][]]]"))

# print("String : [][] Balanced or not?")
# print(is_paren_balanced("]["))


# string_demo = 'Hello World'

# print(string_demo[::-1])
