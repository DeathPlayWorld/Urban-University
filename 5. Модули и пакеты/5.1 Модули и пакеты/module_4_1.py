from fake_math import divide as false_divide
from true_math import divide as true_divide

first = int(input("\nType first number:"))
second = int(input("Type second number:"))

print("\nFalse divide:")
print("Answer:", false_divide(first, second))
print("\nTrue divide:")
print("Answer:", true_divide(first, second))