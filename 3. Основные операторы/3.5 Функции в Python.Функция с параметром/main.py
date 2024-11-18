def get_matrix(n, m, value):
    matrix = []
    for i in range (0, int(n)):
        matrix.append([])
        for j in range(0, int(m)):
            matrix[i].append(value)

    return matrix

running = True

while running:
    print("Do you want to exit?")
    n = input("Type number for n:")
    m = input("Type number for m:")
    value = input("What value do you want to type?\n")
    result = get_matrix(n, m, value)
    print(result)

    print("\nDo you want to leave this program?")
    print("0 - No!     1 - Yes!")
    leaving = int(input())
    if leaving == 1: running = False
