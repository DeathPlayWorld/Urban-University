from random import choice

#1
print("\nFirst:")
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x,y: x == y, first, second)))

#2
print("\nSecond: look at the file with name 'example.txt'")
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, "w", encoding="utf-8") as file:
            for data in data_set: file.write(f"{str(data)}\n")

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#3
print("\nThird:")
class MysticBall:
    def __init__(self, *args):
        self.words = [*args]

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

