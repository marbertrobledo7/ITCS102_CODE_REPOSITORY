from getpass import getpass

u = "Marbertcutie"
p = "Marbertlovesclaire"
isLogin= False

while isLogin == False:
    username = input("Input USERNAME ------> ")
    password = input("input PASSWORD----> ")

    if username == u and password == p:
        print("Access granted")
        isLogin = True
    else:
        print("MALI KA BOY")
        isLogin == False
