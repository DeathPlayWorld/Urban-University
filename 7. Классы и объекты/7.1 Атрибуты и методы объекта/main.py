
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

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

house_1.go_to(5)
house_2.go_to(10)