class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

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

    def __del__(self):
        return print(f"'{self}' was demolished but it will remain in history!")

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
print(House.houses_history)
house_2 = House("Burj Khalifa", 163)
print(House.houses_history)
house_3 = House("Merdeka 118", 118)
print(House.houses_history, "\n")

del house_1, house_2
print(House.houses_history)
