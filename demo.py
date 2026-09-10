name = input("Please input your Name:" )

type_of_item = input("What item will be delivered:"  )

is_fragile = bool(input("The item is fragile:"  ))

weight = float(input("How many kg the item is:" ))

distance = float(input("How far the item will go in km:" ))

is_express = bool(input("The item is rush:" ))

is_international = bool(input("Is this going to be taken internationally:" ))

if weight <= 2:
   print("the shipping will be free")



