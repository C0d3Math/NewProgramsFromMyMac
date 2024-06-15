from random import *
def wait():
    i = input("Press enter when you are ready. ")
values = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
suits = ["Hearts","Clubs","Spades","Diamonds"]
deck = []
for v in range(0,len(values)):
    for s in range(0,len(suits)):
        deck.append(values[v] + " of " + suits[s])
for x in range(2):
    deck.append("Joker")
exercises = ["seconds in bridge","seconds in spider pose","three pointers","push-ups","sit-ups","wall push-ups","lunges","burpees"]
exercisesUsed = [exercises[randint(0,7)] for i in range(4)]
multipliers = [randint(1,4) for i in range(4)]
amounts = [2,3,4,5,6,7,8,9,10,randint(2,15),randint(2,15),randint(2,15),randint(10,20)]
for i in range(0,3):
    print(suits[i] + " are " + multipliers[i] + " times the value of " + exercisesUsed[i] ".")
wait()
doNext = True
while doNext == True:
    v = 0
    card = deck[randrange(0,len(deck))]
    for i in range(0,12):
        if values[i] in card:
            v = i
    if v == 0:
        print("This is a joker! Do 5 somersaults, 5 backwards somersaults, and 1 minute in tree pose!")
    else:
        for i in range(0,3):
            if suits[i] in card:
                s = i
        amount = amounts[v] * multipliers[s]
        exercise = exercisesUsed[s]
        print("It is the " + values[v] + " of " + suits[s] + ", which requires you to do " + amount + exercise ".")
        wait()
        print("Do you want to finish? 0/1")
        if input == 1:
            doNext = False