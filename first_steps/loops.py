# structure of for loop:
# for iterator in sequency:
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(f'{i} is even')
#     else:
#         print(f'{i} is not even')

# Looping through a List/String
# float_list = [2.5, 15.3, 11.77, 8.4, 100.05]
# counter = 0
# for num in float_list:
#     if num > 10:
#         counter += 1
# print(counter)

# Nested loop
# num = 50
# num_list = [10, 4, 23, 6, 18, 27, 47]
# found = False
# for n1 in num_list:
#     for n2 in num_list:     # We have two iterators
#         if(n1 + n2 == num):
#             found = True    # set found to be true
#             break           # Breaking inner loop if a pair is found
#     if found:
#         print(n1, n2)       # Printing the pair
#         break               # Breaking the outer loop


# The continue Keyword
# num_list = list(range(0, 10)) # [0,1,2,3...]

# for num in num_list:
#     if num % 2 == 1:
#         continue
#     print(num)
# print(num_list)

# sample input : [10, -14, 26, 5, -3, 13, -5]
# sample output : True or False
numb_list = [10, -10, 26, 5, -3, 13, -5]
num = 0
answer = False
for n1 in range(len(numb_list)):
    for n2 in range(n1, len(numb_list)):
        if (numb_list[n1] + numb_list[n2] == num):
            print(f'{num} True')
            answer = True
            break
    if answer == False:        
        print(f'{num} False')