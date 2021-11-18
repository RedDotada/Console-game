import random
number = random.randint(1,100)
words = open('words.txt', 'r')
data = words.read()
strwords = (data)
wordslist = strwords.split(sep=', ')
word = wordslist[number]
print(word)

for i in word:
    pass
    
    

while True:
    raw_input = input("letter: ")
    if raw_input == word:
        print("YOU WIN")
        break
    #print(word.count(raw_input))
    if word.count(raw_input) == 1:
        print("it's letter has")
    




