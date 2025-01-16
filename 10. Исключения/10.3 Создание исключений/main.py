
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model

        def __is_valid_vin():
            if isinstance(vin, int):
                if 1000000 <= vin <= 9999999:
                    return True
                else: raise IncorrectVinNumber("Wrong interval for vin number!")
            else: raise IncorrectVinNumber("Wrong vin number!")

        def __is_valid_numbers():
            if isinstance(numbers, str):
                if len(numbers) == 6:
                    return True
                else: raise IncorrectCarNumbers("Wrong length of car numbers!")
            else:
                raise IncorrectCarNumbers("Wrong type for car numbers!")

        if __is_valid_vin(): self.__vin = vin
        if __is_valid_numbers(): self.__numbers = numbers

#Model 1
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} successfully created!')

#Model 2
try:
  second = Car('Model2', 300, 't001tp')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} successfully created!')

#Model 3
try:
  third = Car('Model3', 2020202, 'no numbers')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} successfully created!')