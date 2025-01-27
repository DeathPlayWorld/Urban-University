

def is_prime(func):
    def wrapper(*args):
        result_of_func = func(*args)
        divider = 0
        for i in range(1, result_of_func):
            if result_of_func % i == 0: divider += 1
            if divider >= 3:
                print("Not prime!")
                break
        if divider == 1: print("Prime")
        return result_of_func
    return wrapper

@is_prime
def sum_three(*args):
    sum_ = 0
    for number in args:
        sum_ += number
    return sum_

result = sum_three(2, 3, 6)
print(result)

