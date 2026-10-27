
size = int(input("Enter size --->"))
code = 1

for x in range(size):
    for y in range(size - x - 1):
        print(" ", end=" ")

    for y in range(2 * x + 1):
        print(code, end=" ")
        code += 1

    print()

for x in range(size - 2, -1, -1):
    for y in range(size - x - 1):
        print(" ", end=" ")

    for y in range(2 * x + 1):
        print(code, end=" ")
        code += 1

    print()