#1
import random

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

print("Want to randomize list?")
Randomize = int(input("1 - Yes!        0 - No!\n"))
if Randomize == 1:
    for i in range (0, len(my_list)):
        my_list[i] = random.randint(-5, 10)
print("Ok! Your list is:", my_list)

#2
i = 0
running = True
print("\nFirst variant(with bool):")
while running:
    if my_list[i] >= 0:
        if my_list[i] != 0:
            print(my_list[i])
        i += 1
    if my_list[i] < 0:
        running = False
    elif my_list[i] == len(my_list):
        running = False

#3
i = 0
print("\nSecond variant(with break):")
while True:
    if my_list[i] >= 0:
        if my_list[i] != 0:
            print(my_list[i])
        i += 1
    if my_list[i] < 0:
        break
    elif my_list[i] == len(my_list):
        break
