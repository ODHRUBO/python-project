###My first project##
#computer quiz
print("################################")
print("Welcome, to my computer quiz!!")
print("################################")


playing = input("Do you want to play ?  ").lower()
if playing.lower() != "yes":
    quit()
print("################################")
print("Okey! Let's play :)") 
print("################################")
score=0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score+=1

else:
    print("Incorrect!")

answer = input("What does IC stand for? ").lower()
if answer == "integrated circuit":
    print("Correct!")
    score+=1

else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "grapics processing unit":
    print("Correct!")
    score+=1

else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "rendom access memory":
    print("Correct!")
    score+=1

else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")
if answer == "read only memory":
    print("Correct!")
    score+=1

else:
    print("Incorrect!")

if score > 0:
    print("################################")
    print("weldone")
    print("#######################################################")
    print("you got " + str(score) + " for answring question correct")
    print("########################################################")
    print("you got " + str((score/5)*100 )+ "%.")
    print("########################################################")
else:
    print("################################")
    print("You can't correct any answer")
    print("try again..Best of Luck")
    print("################################")