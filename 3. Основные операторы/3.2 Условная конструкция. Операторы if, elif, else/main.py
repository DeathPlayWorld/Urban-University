#Input
print("Type first number:")
a = int(input())
print("Type second number:")
b = int(input())
print("Type third number:")
c = int(input())

#Output
#1
if(a==b==c):
    print("All variables are equal:", 3)
#2
elif(a == b or a == c or b == c):
    print("Two variables are equal:", 2)
#3
else:
    print("There are no equal variables:", 0)
