from sys import exception

def personal_sum(*numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        try: result += number
        except TypeError: incorrect_data += 1

    return result, incorrect_data

def calculate_average(*numbers):
    try:
        if len(numbers) <= 1: exception(TypeError)
        average = personal_sum(*numbers)[0] / (len(numbers)-personal_sum(*numbers)[1])
    except ZeroDivisionError:
        print("\nError! Division by zero(length of numbers is 0) in calculate_average!\n")
        return 0
    except TypeError:
        print("\nError! Numbers are not in the collection in caclulate_average!\n")
        return  None
    else: return average

print(f"Result 1: {calculate_average("1", "2", "3")}") # String only
print(f"Result 2: {calculate_average(1, "String", 3, "Another string")}") # Only 1 and 3
print(f"Result 3: {calculate_average(567)}") # Not collection(single number)
print(f"Result 4: {calculate_average(42, 15, 36, 13)}") # Without error