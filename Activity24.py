route = ["Terminal", "Perez Park", "Pacific Mall"]
passenger = []
SEATS = 6
FARE = 13
total = 0

while True:
    print()
    print("SAKAY:", passenger)
    print(len(passenger), "of", SEATS, "seats")
    print("1 Sakay 2 Priority seat 3 Para po!")
    print("4 Baba sa pinto 5 baba sa harap")
    print("6 Seat check 7 Balikan 8 Exit")
    choice = input("Choice:  ")

    if choice == "1":
        if len(passenger) == SEATS:
            print("PUNO NA NGANI")
        else:
            name = input("Name:  ")
            passenger.append(name)
            total = total + FARE
            print(name, "boarded at the back. ")

    elif choice == "2":
        if len(passenger) == SEATS:
            print("PUNO NA NGANI")
        else:
            name = input("NAME:  ")
            passenger.insert(0, name)
            total = total + FARE
            print(name, "took the priority seat")

    elif choice == "3":
        name = input ("who is getiting off?")
        if name in passenger:
            passenger.remove(name)
            print(name, "Got off, Mag ingat ka baby")
        else:
            print(name, "is not on this jeep")

    elif choice == "4":
        if len(passenger) == 0:
            print("the jeep is empty. ")
        else:
            left = passenger.pop(0)
            print(left, "got off on the door.")


    elif choice == "5":
        if len(passenger) == 0:
            print("the jeep is empty. ")
        else:
            front = passenger.pop(0)
            print(front, "got off at the front. ")

    elif choice == "6":
        for i in range(len(passenger)):
            print("Seat", i + 1, passenger [i])

    elif choice == "7":
        route.reverse()
        print("Route:", route)

    elif choice == "8":
        print("total fare today:", total)
        break

    else:
        print("invalid choice boy.")
