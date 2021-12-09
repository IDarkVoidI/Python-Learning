# car = ("Ford", "Raptor", 2019, "Red")

# car = {
#     "brand": "Ford",
#     "model": "Raptor",
#     "year": 2019,
#     "color": "Red"
# }
#
# print(car['brand'])

# dict() Constructor

# class Dict:
#     def __init__(self, **kwargs):
#         self.kwarg = kwargs
#
#     def set(self):
#         pass

# empty_dict = dict()
# print(empty_dict)

phone_book = dict(Batman=3223144, Superman=23213131, Jocker=23131313)
# print(phone_book)
# print(phone_book.get('Superman'))
phone_book['Spiderman'] = 424242
# print(phone_book)
#
# phone_book['Batman'] = 555555
# print(phone_book)
#
# phone_book['Batman'] = 3223144
# print(phone_book)
#
# # del phone_book['Jocker']
# # print(phone_book)
#
# jocker = phone_book.pop('Jocker')
# print(phone_book)
# print("Jocker" in phone_book)
#
# backup = {}
#
# backup.update(phone_book)
#
# print(backup)

houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}

# houses.items() => [(1, "Gryffindor"), (2, "Slytherin")...]

print(houses)
print(new_houses)
