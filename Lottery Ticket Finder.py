"""
Author: Keshav
Date: 30/10/2020
Purpose: To check the odd of winning a lottery
"""

from random import choice

lottery = [0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

print("The ticket number should only consist of numbers and letter(lowercase) or both.\nAnd the length should be only 4")

#Enter the ticket number

your_draw=input("What is ''your ticket number? ")

turns=0

while True:

    if len(your_draw) != 4:

        print("Please enter a valid ticket number.\nThe ticket number should only consist of numbers and letter(lowercase) or both.\nAnd the length should be only 4")

        break

    draw1 = str(choice(lottery))

    draw2 = str(choice(lottery))

    draw3 = str(choice(lottery))

    draw4 = str(choice(lottery))

    draw = draw1+draw2+draw3+draw4

    print(f"The draw is {draw}")    

    turns+=1

    if draw==your_draw:

        print("\nIt's a match!!")

        print(f"\nIt took {turns} turns to find the match")

        break    

    continue
