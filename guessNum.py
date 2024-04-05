from random import randint
rnum = randint(1,10)
chances = 5
while chances > 0:
    n = int(input("Guess the input: "))
    if (n ==rnum):
        print("You Won")
        break
    elif(n > rnum):
        print("guessed num is greater than actual num")
        chances -= 1
    elif(n < rnum):
        print("guessed num is less than actual num")
        chances -= 1
else:
    print("You lost the game")
    print("the number was :", rnum)