
class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner:str, model:str, color:str, engine_power:int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self): print(f"Model: {self.__model}")

    def get_horsepower(self): print(f"Engine power: {self.__engine_power}")

    def get_colour(self): print(f"Colour: {self.__color}")

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_colour()
        print(f"Owner: {self.owner}")

    def set_color(self, new_color:str):
        can_change_color = False
        for i in range(0, len(self.__COLOR_VARIANTS)):
            if new_color.lower() == self.__COLOR_VARIANTS[i].lower():
                can_change_color = True
        if can_change_color: self.__color = new_color
        else: print(f"You can't change to {new_color} color!")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()