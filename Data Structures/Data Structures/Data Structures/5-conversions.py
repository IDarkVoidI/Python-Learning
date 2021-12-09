# Explicit conversion

# distionation_structure_name(source_structure_object)

# converting the list

star_wars_tup = ("Anakin", "Darth Vader", 1000)
print(star_wars_tup)
star_wars_set = {"Anakin", "Darth Vader", 1000}
print(star_wars_set)
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

# star_wars_list = list(star_wars_tup)  # converting from tuple
# print(star_wars_list)

# star_wars_list = list(star_wars_set)  # converting from set

star_wars_list = list(star_wars_dict)  # converting from dict
print('a', star_wars_list)
# # dict.items()

star_wars_list = list(star_wars_dict.items())
print('b', star_wars_list)


# Tuple

star_wars_list = ["Anakin", "Darth Vader", 1000]
print(star_wars_list)
star_wars_set = {"Anakin", "Darth Vader", 1000}
print(star_wars_set)
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

star_wars_tup = tuple(star_wars_list)  # Converting from list
print(star_wars_tup)

star_wars_tup = tuple(star_wars_set)  # Converting from set
print(star_wars_tup)

star_wars_tup = tuple(star_wars_dict)  # Converting from dictionary
print(star_wars_tup)


star_wars_list = ["Anakin", "Darth Vader", 1000]
print(star_wars_list)
star_wars_tup = ("Anakin", "Darth Vader", 1000)
print(star_wars_tup)
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

star_wars_set = set(star_wars_list)  # Converting from list
print(star_wars_set)

star_wars_set = set(star_wars_tup)  # Converting from tuple
print(star_wars_set)

star_wars_set = set(star_wars_dict)  # Converting from dictionary
print(star_wars_set)


star_wars_list = [[1, "Anakin"], [2, "Darth Vader"], [3, 1000]]
print(star_wars_list)
star_wars_tup = ((1, "Anakin"), (2, "Darth Vader"), (3, 1000))
print(star_wars_tup)
star_wars_set = {(1, "Anakin"), (2, "Darth Vader"), (3, 1000)}
print(star_wars_set)

star_wars_dict = dict(star_wars_list)  # Converting from list
print(star_wars_dict)

star_wars_dict = dict(star_wars_tup)  # Converting from tuple
print(star_wars_dict)

star_wars_dict = dict(star_wars_set)  # Converting from set
print(star_wars_dict)


# list
# A) ordered, immutable, indexed
# B) unordered, immutable, unindexed
# C) Ordered, mutable, indexed
# D) ordered, immutable, unindexed


# A set can contain a tuple, but not a list.

# True or False
