import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        day = 0
        print(f"{self.name}, we are under attack!")
        while enemies > 0:
            time.sleep(1)
            day += 1
            enemies -= self.power
            print(f"{self.name} fighting for {day} day(s)... Enemies left: {enemies}!")
        print(f"\n{self.name} won in {day} day(s)!\n")


knights = []
characteristics = [("Sir Lancelot", 10), ("Sir Galahad", 20)]

for characteristic in characteristics:
    knight = Knight(*characteristic)
    knights.append(knight)
    knight.start()

for knight in knights:
    knight.join()

print("All battles are over!")
