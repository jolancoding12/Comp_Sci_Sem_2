import random
word_list = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        word_list.append(l)

num = random.randrange(0,12972)
answer= word_list[num]
print(answer)
a = 0
for i in range(0,6):
    guess = input("guess a word (you'll never get it) ")
    if guess == answer:
        print("wow. twelve thousand words and you actually got it in six tries")
        break
    else:
        print("again. ")
if a == 0:
    print("loser (answer is " + answer + ")")

f.close()
