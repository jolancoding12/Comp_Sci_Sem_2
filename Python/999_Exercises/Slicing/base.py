first = input("whats ur name ")

cnt = 0
for i in range(0,len(first)):
    cnt = cnt + 1
    print(first[i:cnt])
cnt = 0
for i in range(0,len(first)):
    cnt = cnt + 1
    if first[i:cnt] == " ":
        print(first[i:len(first)])
        print(first[0:i])