
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string) for string in first_strings if len(string) >= 5]
print(first_result)
second_result = [(string1, string2) for string1 in first_strings for string2 in second_strings if len(string1) == len(string2)]
print(second_result)
third_result = {string: len(string) for lists in zip(first_strings, second_strings) for string in lists if len(string) % 2 == 0 }
print(third_result)