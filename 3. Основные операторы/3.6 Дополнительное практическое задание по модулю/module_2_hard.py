import random

def calculations(value, list_to_add):
    for i in range(1, 20):
        for j in range(1, 20):
            sum_number = i + j
            if value % sum_number == 0 and i != j:
                if checking_number(i, j, list_to_add):
                    list_to_add.append(str(i)+str(j))

def checking_number(digit_1, digit_2, checking_list):
    good_value = True
    for q in range(0, len(checking_list)):
        if (int(checking_list[q]) == int(str(digit_1) + str(digit_2))
                or int(checking_list[q]) == int(str(digit_2) + str(digit_1))): good_value = False
    return good_value

def convert_to_string(list_to_parse):
    ending_string = str()
    for t in range(0, len(list_to_parse)):
        ending_string += str(list_to_parse[t])
    return ending_string

running = True
print("\nI don't envy your fate... Do you want to print all answers or only for one specific?")

while running:
    answer = []
    print("\n1 - For one         2 - For all         3 - Random         0 - Exit")
    choice = int(input())

    if choice == 1:
        print("\nPlease type your number:")
        inter_value = int(input())
        if inter_value > 2:
            calculations(inter_value, answer)
            print(convert_to_string(answer))
        else: print("Incorrect number!")

    elif choice == 2:
        for g in range(3, 21):
            calculations(g, answer)
            print(str(g) + ".", convert_to_string(answer))
            answer = []

    elif choice == 3:
        inter_value = random.randint(3, 20)
        calculations(inter_value, answer)
        print(str(inter_value) + ".", convert_to_string(answer))

    elif choice == 0:
        running = False

    else: print("There is no choice with that value!")