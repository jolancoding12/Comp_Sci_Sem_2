sentence = "whale hello there. Don't we all love Whales? I absolutely love whales! whales are so huge!!!"
count = 0
counter = 0
find = 0
for z in range(0,len(sentence)):
    counter = counter + 1
    if sentence[z:counter] == "w":
        if sentence[z:counter+4] == "whale":
            count = count + 1
        elif sentence[z:counter+5] == "whales":
            count = count + 1
    if sentence[z:counter] == "W":
        if sentence[z:counter+4] == "Whale":
            count = count + 1
        elif sentence[z:counter+5] == "Whales":
            count = count + 1
print("theres " + str(count) + " whales in the thing")

for i in range(0,len(sentence)):
    find = find + 1
    if sentence[i:find+4] == "whale":
        print(i)
    if sentence[i:find+4] == "Whale":
        print(i)
        
with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()
        count = 0
counter = 0
find = 0
for z in range(0,len(sentence)):
    counter = counter + 1
    if sentence[z:counter] == "w":
        if sentence[z:counter+4] == "whale":
            count = count + 1
        elif sentence[z:counter+5] == "whales":
            count = count + 1
    if sentence[z:counter] == "W":
        if sentence[z:counter+4] == "Whale":
            count = count + 1
        elif sentence[z:counter+5] == "Whales":
            count = count + 1
print("theres " + str(count) + " whales in the thing")

for i in range(0,len(sentence)):
    find = find + 1
    if sentence[i:find+4] == "whale":
        print(i)
    if sentence[i:find+4] == "Whale":
        print(i)

f.close()

#with open('moby.txt') as f:
#    for line in f:
#        sentence = line.strip()
#        ##YOUR CODE GOES HERE
#
#f.close()
