
def custom_write(file_name, string:list):
    file = open(file_name, "w", encoding="utf-8")
    string_positions = dict()
    for i in range(0, len(string)):
        string_positions.update({(i+1, file.tell()): string[i]})
        file.write(f"{string[i]}\n")
    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)

