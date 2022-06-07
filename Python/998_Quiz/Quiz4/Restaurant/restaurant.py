import random
restyrantes = ["mkdonald", "borguer kang", "kung foo pangah"]
mcdonnies = ["fish fillet ", "travvy patty " , "spanish rice "]
kuger_king = ["whooper ", "chicken fingers (yuky imo) ", "SODAAA "]
kung_foo_panda = ["organ chicken ", "bcorrili & steek ", "fortune cokes "]
restys = input("ayoooooo what resturants do you wanna go to? we got mcdonalds, burger king, and panda express ")

if restys == "mcdonalds":
    print("ok we got beutiful foods, heres our menu: " + str(mcdonnies))
    print("our suggested item is " + mcdonnies[random.randrange(0,3)])
elif restys == "burger king":
    print("ok we got beutiful foods, heres our menu: " + str(kuger_king))
    print("our suggested item is " + kuger_king[random.randrange(0,3)])
elif restys == "panda express":
    print("ok we got beutiful foods, heres our menu: " + str(kung_foo_panda))
    print("our suggested item is " + kung_foo_panda[random.randrange(0,3)])
else:
    print("that aint one of the restaurants here, try again")