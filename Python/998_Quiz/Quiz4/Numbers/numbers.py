mynumbers = [6,9,32,82,15,22,3,18]
minimum = mynumbers[0]
maximum = mynumbers[0]
sum = 0 
x = (len(mynumbers))
todos = x
for i in range(0, len(mynumbers)):
    if maximum < mynumbers[i]:
        maximum = mynumbers[i]

print(str(maximum))    

for i in range(0, len(mynumbers)):
    if minimum > mynumbers[i]:
        minimum = mynumbers[i]

print(str(minimum))    

for i in range(0, len(mynumbers)):
    sum = sum + mynumbers[i]
    avg = sum/todos
print(avg)