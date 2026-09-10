name = input("Please input your Name:" )

type_of_item = input("What item will be delivered:"  )

is_fragile = bool(input("The item is fragile:"  ))

weight = float(input("How many kg the item is:" ))

distance = float(input("How far the item will go in km:" ))

is_express = bool(input("The item is rush:" ))

is_international = bool(input("Is this going to be taken internationally:" ))

base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 2 and distance <= 100 and not is_express and not is_international:
    total = 0

elif is_international and is_express:
    total = (base_cost * 1.40) + 50

elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total = base_cost + 30

else:
    total = base_cost




