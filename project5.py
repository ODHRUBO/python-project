##dice gaming##

import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    players = input("Enter the number of player(1-4): ")
    if players.isdigit():
        players = int(players)

        if 2 <= players <= 4:
            break
        else:
            print("player must be between (2-4)")
    else:
        print("invalid , Try again.")

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:

    for player_idx in range(players):
        print("\n player number",player_idx + 1,"turn has just started")
        print("your total score is : ",player_score[player_idx])
        current_score = 0

        while True:
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1 :
                print("you rolledd a 1.Turn done!!")
                current_score = 0
                break
            else:
                current_score +=value
                print("you rolled a :",value)

            print("your score is:",current_score)

        player_score[player_idx] += current_score
        print("your total score is : ",player_score[player_idx])

max_score = max(player_score)
winning_idx = player_score.index(max_score)
print('player position',winning_idx+1,"is winner with a score of",max_score)
    





    