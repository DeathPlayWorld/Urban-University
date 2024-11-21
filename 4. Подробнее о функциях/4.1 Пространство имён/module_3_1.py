
calls = 0
choice = 1
running = True

def count_calls():
    global calls
    calls += 1

def string_info(string:str):
    count_calls()
    _info = (len(string), string.upper(), string.lower())
    return _info

def is_contains(string:str, list_to_search:list):
    count_calls()
    string = string.lower()
    for i in range(len(list_to_search)):
        if string == str(list_to_search[i]).lower():
            return True
    return False

#Main function
while running:
    #Shuting down program
    if choice == 0:
        print("Total calls time:", calls)
        running = False

    elif choice == 1:
        _inputList = []
        _inputString = str(input("\nType string to search:"))
        print("Information about string:", string_info(_inputString))
        #Creating list
        while True:
            if not _inputList:
                _addString = str(input("Type string to add in the list:"))
                _inputList.append(_addString)
            else:
                while True:
                    print("Do you want to add more?\n1 - Yes!      0 - No!")
                    try:
                        choice = int(input())
                        if choice != 1 and choice != 0:
                            print("Invalid choice!\n")
                        else:
                            break
                    except ValueError: print("Invalid choice!\n")

                if choice == 0:
                    break
                elif choice == 1:
                    _addString = str(input("Type string to add in the list:"))
                    _inputList.append(_addString)
                    continue
        #Checking if there is string in the list
        if is_contains(_inputString, _inputList):
            print("\nSearching list:", _inputList, "\nSearching string:", "'"+_inputString+"'")
            print("\nString in this list!\n")
        else:
            print("\nSearching list:", _inputList, "\nSearching string:", "'"+_inputString+"'")
            print("\nString not in this list!\n")

        # Checking if you want to progress through program
        while True:
            print("Do you want to continue?")
            print("1 - Yes!      0 - No!")
            try:
                choice = int(input())
                if choice != 1 and choice != 0:
                    print("Invalid choice!\n")
                else:
                    break
            except ValueError:
                print("Invalid choice!\n")