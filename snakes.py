# Snakes and Ladders
import random

#variables
diceroll = 0
snake1start = random.randrange(25,76)
snake1end = random.randrange(5,snake1start)
ladder1start = random.randrange(10,51)
ladder1end = random.randrange(ladder1start + 1,101)
snake2start = random.randrange(25,76)
snake2end = random.randrange(5,snake2start)
ladder2start = random.randrange(10,51)
ladder2end = random.randrange(ladder2start + 1,101)
snake3start = random.randrange(25,76)
snake3end = random.randrange(5,snake3start)
ladder3start = random.randrange(10,51)
ladder3end = random.randrange(ladder3start + 1,101)
snake4start = random.randrange(25,76)
snake4end = random.randrange(5,snake4start)
ladder4start = random.randrange(10,51)
ladder4end = random.randrange(ladder4start + 1,101)
snake5start = random.randrange(25,76)
snake5end = random.randrange(5,snake5start)
ladder5start = random.randrange(10,51)
ladder5end = random.randrange(ladder5start + 1,101)
space = 0
times = 0

#the game obvs
while space < 100:
    times = times + 1
    goodinp = False
    diceroll = random.randrange(1,7)
    #if you want to roll
    while goodinp == False:
        print("Press any key to roll!")
        lalaland = str(input())
        if lalaland != "":
            goodinp = True
    space = space + diceroll
    print("You rolled a " + str(diceroll) + ", sending you up to space " + str(space) + ".")
    #snake detector
    if space == snake1start or space == snake2start or space == snake3start or space == snake4start or space == snake5start:
        if space == snake1start:
            space = snake1end
        if space == snake2start:
            space = snake2end
        if space == snake3start:
            space = snake3end
        if space == snake4start:
            space = snake4end
        if space == snake5start:
            space = snake5end
        print("Uh-oh! You slid down a snake and are now on space " + str(space) + "! :-(")
    #ladder detector
    if space == ladder1start or space == ladder2start or space == ladder3start or space == ladder4start or space == ladder5start:
        if space == ladder1start:
            space = ladder1end
        if space == ladder2start:
            space = ladder2end
        if space == ladder3start:
            space = ladder3end
        if space == ladder4start:
            space = ladder4end
        if space == ladder5start:
            space = ladder5end
        print("Yay! You climbed a ladder and are now on space " + str(space) + "! :-)")

#when you win
print("Yay! You won! Good job! See if you can beat it in fewer than your " + str(times) + " rolls!")