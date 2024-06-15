# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:37:11 2022

@author: Max
"""
stop = False

while stop == False:
    steps = 0
    itsone = False
    print("What number do you want to test?")
    number = int(input())
    begin = number
    while itsone == False:
        print(number)
        if number % 2 == 0:
            number = int(number/2)
        else:
            number = (number * 3) + 1
        steps = steps + 1
        if number == 1:
            itsone = True
    print(str(begin) + " took " + str(steps) + " tries to get to 1.")
    print()
    print("Do you want to try again? (y/N)")
    answer = str(input())
    if answer == "N":
        stop = True