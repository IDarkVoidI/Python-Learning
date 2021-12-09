# A data structure is a way of storing and organizing data according to a
# certain format or structure.

# List []
# Tuple ()
# Dictionary {}
# Set {}


# List
# list_demo = [1, 'text', True, 2.3]

# list_demo[1]


# # range()
# num_seq = range(0, 10)
# num_list = list(num_seq)
# print(num_list)

# num_seq = range(3,  20, 3)
# print(list(num_seq))

# List-Ception
# world_cup_winners = [[2006, 'Italy'], [2010, 'Spain'], [2014, 'Germany']]
# print(world_cup_winners[1][1])

# merging lists
# part_A = [1, 3, 4, 5, 6]
# part_B = [7, 8, 9, 0]

# merged = part_A + part_B

# part_A.extend(part_B)

# print(merged)
# print(part_A)
# print(part_B)

# Append
# num_list = []
# num_list.append(1)
# num_list.append(2)
#
#
# # insert()
# num_list.insert(1, 5)
#
# # pop()
# num_list.pop()
# print(num_list)


# remove

# world_cup_winners = [[2006, 'Italy'], [2010, 'Spain'], [2014, 'Germany']]
#
# world_cup_winners[0].remove('Italy')
#
# print(world_cup_winners)


# list slicing
# houses = ("Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin")
# # game = houses[0::3]
# # print(game)
# #
# #
# # # index
# #
# # print(houses.index('Ravenclaw'))
# #
# # print('Ravenclaw' in houses)
#
# list_of_numbers = [1, 245, 5353, 7764, 5]
#
#
# sorted_houses = sorted(houses)
#
# print(sorted_houses)
#
# list_of_numbers.sort(reverse=True)
# print(list_of_numbers)

# a = ("b", "g", "a", "d", "f", "c", "h", "e")
# x = sorted(a)
# print(type(x))

# list comprehension

# nums = [10, 20, 30, 40, 50]
# numb_double = []
#
# for n in nums:
#     numb_double.append(n * 2)
#
# print(nums)
# print(numb_double)

nums1 = [10, 20, 30, 40, 50]
nums2 = [60, 70, 80, 90, 100]

# nums_double = [n * 2 for n in nums]
nums_double = [(n1 * 2, n2 * 2) for n1 in nums1 for n2 in nums2]


print(nums_double)
