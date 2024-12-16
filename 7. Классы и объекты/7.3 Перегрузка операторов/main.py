
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print("Error! Invalid type!")

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors + other)
        elif isinstance(other, House):
            return House(self.name, self.number_of_floors + other.number_of_floors)
        else:
            print("Error! Invalid type!")

    def __radd__(self, other):
        return House.__add__(self, other)

    def __iadd__(self, other):
        return House.__add__(self, other)

    def go_to(self, new_floor):
        print(f"\n{self.name}")
        if new_floor > self.number_of_floors:
            print("This floor doesn't exist!")
        else:
            print(f"Going to {new_floor} floor!")
            for i in range(1, new_floor):              # if you want to iterate up to new floor then type new_floor + 1
                print(i)                               # and delete down message about arrival
            print(f"We arrive at {new_floor} floor!")  # <--------------

house_1 = House("One World Trade Center", 94)
house_2 = House("Burj Khalifa", 163)

# __eq__
print(f"\nChecking if {house_1.name} is equal to {house_2.name}...")
print(f"{house_1.number_of_floors}  and {house_2.number_of_floors}: {house_1 == house_2}\n")

# __add__
print(f"Adding {10} to {house_1.name}...")
print(f"Before {house_1.number_of_floors}")
house_1 = house_1 + 10
print(f"After {house_1.number_of_floors}\n")

# __iadd__
print(f"Adding {10} to {house_1.name}...")
print(f"Before {house_1.number_of_floors}")
house_1 += 10
print(f"After {house_1.number_of_floors}\n")

# __radd__
print(f"Adding {10} to {house_2.name}...")
print(f"Before {house_2.number_of_floors}")
house_2 = 10 + house_2
print(f"After {house_2.number_of_floors}\n")

# __gt__
print(f"Checking if {house_1.name} is bigger then {house_2.name}...")
print(f"{house_1.number_of_floors}  and {house_2.number_of_floors}: {house_1 > house_2}\n")
# __ge__
print(f"Checking if {house_1.name} is bigger or equal to {house_2.name}...")
print(f"{house_1.number_of_floors}  and {house_2.number_of_floors}: {house_1 >= house_2}\n")
# __lt__
print(f"Checking if {house_1.name} is lower then {house_2.name}...")
print(f"{house_1.number_of_floors}  and {house_2.number_of_floors}: {house_1 < house_2}\n")
# __le__
print(f"Checking if {house_1.name} is lower or equal to {house_2.name}...")
print(f"{house_1.number_of_floors}  and {house_2.number_of_floors}: {house_1 <= house_2}\n")
# __ne__
print(f"Checking if {house_1.name} is not equal to {house_2.name}...")
print(f"{house_1.number_of_floors}  and {house_2.number_of_floors}: {house_1 != house_2}\n")
