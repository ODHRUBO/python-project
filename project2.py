##Guess random number##
import random

top_of_range = input("input top range of number? : ")
if top_of_range.isdigit():
    top_of_range = int (top_of_range)
    if top_of_range <=0:
        print("your digit is low of range")
        quit()
else:
    print("please,, inter a digit")


random_number = random.randint(0,top_of_range)
count = 0
while True:
    count +=1
    user_guess = input("make a guess : ")

    if user_guess.isdigit():
        user_guess = int (user_guess)

    else:
        print("please enter a number  next time.")
        continue

    if user_guess == random_number:
        print("congress!!you guess correctly")
        break

    elif user_guess > random_number:
                print("you were avove the number")


    else:
                print("you were below the number")

print("try",count,"times")

        
      

