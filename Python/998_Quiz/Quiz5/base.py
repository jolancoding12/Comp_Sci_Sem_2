x = input("whats your fav number? ")
y = int(input("how old you is "))
z = 0
counter = 0
for i in range(0,len(x)):
    counter = counter + 1
    if x[i:counter] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0":
        print(x[i:len(x)] * y)

#i know i was sposed to use casting to use the splice but idk how