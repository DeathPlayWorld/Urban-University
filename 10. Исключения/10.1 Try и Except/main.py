

def add_everything_up(first, second):
    try:
        total = first + second
    except TypeError:
        total = str(first) + str(second)
    finally: return  total


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(str.format("{0:.3f}", add_everything_up(123.456, 7)))