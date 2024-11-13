'1st program'
print("\nFirst programm: (9)^0.5 * 5")
answer = float((9 ** 0.5) * 5)
print("Answer:", int(answer))
'1st program(alt)'
print("First programm(alt): (9)^0.5 * 5")
answer: float = pow(9, 0.5) * 5
print("Answer:", int(answer))

'2nd program'
print("\nSecond program:")
a = float(9.99); b = float(9.98); c = float(1000); d = float(1000.1)
print("Answer:", a>b and c!=d)
'2nd program(alt)'
print("Second program(alt):")
print("Answer:", 9.99>9.98 and 1000!=1000.1)

'3rd program'
print("\nThird program:")
print("Answer:",2*2+2 ,2*(2+2) ,2*2+2 == 2*(2+2))
'3rd program(alt)'
print("Third program(alt):")
a = int(2*2+2); b = int(2*(2+2))
print("Answer:",a ,b ,a == b)

'4th program'
print("\nFourth program")
print("Answer:",int(float(str("123.456")) * 10) % 10)
'4th program(alt)'
print("Fourth program(alt)")
a = str("123.456"); b = int((float(a) * 10)%10); del(a)
print("Answer:",b)

input()