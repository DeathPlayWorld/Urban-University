#starting value
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#1
primes = []
not_primes = []
#2
for i in range (0, len(numbers)):
    #4
    is_Prime = True
    #3
    if numbers[i] > 1:
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0: is_Prime = False; break
        #5
        if is_Prime: primes.append(numbers[i])
        else: not_primes.append(numbers[i])

#6
print("\nStarting value:", numbers)
print("\nPrimes numbers from the list:", primes)
print("\nNot Primes number from the list:", not_primes)
