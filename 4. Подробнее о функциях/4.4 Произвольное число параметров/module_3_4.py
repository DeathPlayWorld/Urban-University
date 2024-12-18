
def single_root_words(root_word, *other_words):
    same_words = []
    for name in other_words:
        if root_word.lower() in name.lower():
            same_words.append(name)
        elif name.lower() in root_word.lower():
            same_words.append(name)
    return same_words

running = True

while running:
    while True:
        print("\nDo you want to use your words or default?")
        print("0 - Default      1 - Your")
        try:
            _choice = int(input())
            if _choice != 1 and _choice != 0:
                print("Invalid choice!\n")
            else:
                break
        except ValueError:
            print("Invalid choice!\n")
    if _choice == 0:
        print("\nAll root words for 'rich':")
        print(single_root_words('rich', 'richest', 'orichalcum', 'cheers', 'riches'))
        print("\nAll root words for 'Disablement':")
        print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
    else:
        _other_words = []
        _root_word = str(input("Type root word:"))
        while True:
            while True:
                _other_words.append(str(input("Type string to put in list of words:")))
                print("Do you want to add more?")
                print("0 - No      1 - Yes")
                try:
                    choice = int(input())
                    if choice != 1 and choice != 0:
                        print("Invalid choice!\n")
                    else:
                        break
                except ValueError:
                    print("Invalid choice!\n")
            if choice == 0: break
        print("\nAll root words:")
        print(single_root_words(_root_word, *_other_words))
    print("\nDo you want to exit program?")
    print("0 - No      1 - Yes")
    while True:
        try:
            choice = int(input())
            if choice != 1 and choice != 0:
                print("Invalid choice!\n")
            else:
                break
        except ValueError:
            print("Invalid choice!\n")
    if choice == 1: running = False
