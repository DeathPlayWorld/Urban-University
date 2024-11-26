def get_multiplied_digits(number):
        str_number = str(number)
        _first = int(str_number[0])
        if len(str_number) > 2:
            return _first * get_multiplied_digits(int(str_number[1:]))
        else: return _first

result1 = get_multiplied_digits(40203)
print(result1)

result2 = get_multiplied_digits(402030)
print(result2)