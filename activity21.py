sum = 0

back = True
while back == True:
    x = int(input("Please enter a number"))

    if x == 0:
        print("loop terminated")
        print("Total of all number is ",sum)
        break

    else:
        print("continue loop")
        sum += x
        print("Current total is ",sum)
        continue
