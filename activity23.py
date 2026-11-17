shonen =[]
korean =[]
isekai =[]
adverture =[]
fantasy =[]

while True:
    answer = input("What type of anime do you like? (shonen, korean, isekai, adventure, fantasy) or type 'exit' to finish: ").lower()
    if answer == 'yes':
        print("What kind of anime do you watch or read?    ")
        print("1 shonen \n2 korean \n3 isekai \n4 adventure \n5 fantasy")

        choice = int(input("input --->  "))

        if choice == 1:
            print("Shonen")
            title = input("please input the title of the anime?    ")
            shonen.append(title)
            print("list of shonen")
            con = input("Do you wish to continue yes \ no "). lower()
            if con == yes:
                continue
            else:
                break
        else:
            print("invalid choice")