
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(word[0]) - len(word[1]) for word in list(zip(first, second)) if len(word[0]) != len(word[1]))
print(list(first_result))

second_result = (len(first[i]) == len(second[i]) for i in range(0, 3))
print(list(second_result))