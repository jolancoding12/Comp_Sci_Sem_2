x = int(input("hey youre at a store, how many things ya want "))

balance = 0

for(y) in range(1, x + 1):
    z = input("what would you like to buy ")
    a = float(input("how much would that be "))
    print("thank you for buying " + z + " for " + "$" + str(a))
    balance = balance + a
print("ur total is: " + str(balance))

