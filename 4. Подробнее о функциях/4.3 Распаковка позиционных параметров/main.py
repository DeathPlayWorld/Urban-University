def print_params(number = 1, string = "String", choose = True):
    print(number, string, choose)

def function_with_params():
    print("\nWithout variables:")
    print_params()
    print("\nWith a = 5:")
    print_params(5)
    print("\nWith a = 2 and b = 'Petya':")
    print_params(2, "Petya")
    print("\nWith a = 54, b = 'Berlin' and c = False:")
    print_params(54, "Berlin", False)
    print("\nWith b = 25:")
    print_params(string=25)   #Warning because of the terms of the task
    print("\nWith c = [1,2,3]:")
    print_params(choose=[1, 2, 3]) #Warning because of the terms of the task

def unpacking_parameters():
    value_list = ["Faith", 99, False]
    value_dict = {"number": 47, "string": "Blood magic", "choose": False}
    print("\nWith value list:")
    print_params(*value_list)
    print("\nWith value dictionary:")
    print_params(**value_dict)

def unpacking_and_other_parameters():
    values_list_2 = [31.21, "Something"]
    print("\nWith value list 2:")
    print_params(*values_list_2, 42)

function_with_params()
unpacking_parameters()
unpacking_and_other_parameters()