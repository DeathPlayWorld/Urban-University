#2
print("\nFirst part(Dictionaries):")
my_dict = {"Kerby": 1992, "Pikachu": 1996, "Mario": 1981}
print("Dictionary:", my_dict)
_error_message = "There is no key with this value!"
print("Looking for Mario...:", my_dict.get("Mario", _error_message)), print("Looking for Azazel...:", my_dict.get("Azazel", _error_message))
my_dict.update({"Goofy": 1932, "Mega man": 1987})
_valueOfDeleted = my_dict.pop("Pikachu")
print("Deleted value was:", _valueOfDeleted)
print("Final dictionary:", my_dict)
del my_dict, _error_message, _valueOfDeleted

#3
print("\nSecond part(sets):")
my_set = {1, 2, 3, 3, 2, 1, "Apple", "Orange", "Apple", False}
print("Set:", my_set)
my_set.add("Melon")
my_set.add("Toothpaste")
print("Deleting 'Apple'...")
print("Before:", my_set)
my_set.discard("Apple")
print("After:", my_set)

