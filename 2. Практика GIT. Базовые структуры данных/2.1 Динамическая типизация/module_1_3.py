"Практическая работа по уроку 'Динамическая типизация'"

print("What is your name?")
_Name = input()
print("Hello", _Name + ",", "I hope you will have a great day!")
print("How old are you?")
_Age = int(input())
print("So you are",_Age, "years old...")
print("How many years older would you like to be?")
_NewAge = int(input())
_Age = int(_Age) + int(_NewAge)
print("Congratulations! Now your age is", str(_Age) + "!")
print("Are you a student?")
print("'1' - yes      '0' - no")
_Is_Student = int(input())
if (_Is_Student == 0):
    _Is_Student = bool(False)
else:
    _Is_Student = bool(True)
print("So......")
print("Your name is", _Name+",", "you are", _Age, "years old.")
print("Checking to see if you are a student:", _Is_Student)