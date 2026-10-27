size = int(input("Enter size --->"))
code = 1
for x in range (size):
    for y in range (x):
        print(code, end = " ")
        code +=1
    print()