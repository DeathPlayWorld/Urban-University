from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] += (dx * self.speed)
        self._cords[1] += (dy * self.speed)
        self._cords[2] += (dz * self.speed)

    def get_cords(self):
        print(f"X: {self._cords[0]}", end=" ")
        print(f"Y: {self._cords[1]}", end=" ")
        print(f"Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5: print("Sorry, I'm peaceful :D")
        else: print("Be careful, I'm attacking you now! >:D")

    def speak(self): print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self): print(f"Here is(are) {randint(1, 4)} egg(s) for you!")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        if dz >= 0: self._cords[2] += -abs(dz * int((self.speed/2)))

class PoisonousAnimal(Animal): _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()