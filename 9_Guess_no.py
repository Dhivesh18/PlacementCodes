from random import choice
c = choice([1,2,3,4,5,6,7,8,9])
while True:
    if c==int(input("Make a guess ")):
        print("Well guessed!")
        break
