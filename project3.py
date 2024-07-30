#rock paper Scissors#

import random

user_wins=0
computer_wins=0
options = ["rock","paper","scissors"]
while True:
    user_input = input("Type Rock/Paper/Seasor or Q to quit :) ").lower()
    if user_input =="q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)

    computer_pick = options[random_number]
    print("compputer picked",computer_pick+".")

    if user_input =="rock"and computer_pick == "scissors":
        print("you wins!")
        user_wins += 1

    elif user_input =="scissors"and computer_pick == "paper":
        print("you wins!")
        user_wins += 1
    
    elif user_input =="paper"and computer_pick == "rock":
        print("you wins!")
        user_wins += 1
    
    elif (user_input == "rock" and computer_pick=="rock") or (user_input == "paper"  and computer_pick=="paper") or (user_input == "scissors"  and computer_pick=="scissors"): 
        print("dismiss")

    else:
        print('you lost!')
        computer_wins += 1

print("you wins",user_wins,"times")
print("you lost",computer_wins,"times")
print("goodbye :(")
    
    

