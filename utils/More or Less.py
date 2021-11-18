import random 
import math
j = int(input("Число: "))
x = random.randint(1,1000)
while x!=j:
    if j>x:
        print("Загадоное число меньше")
    if j<x:
        print("Загадоное число больше")
    j = int(input("Число: "))
    if x!=j:
        print("Ты угадал число!")
        break
    
