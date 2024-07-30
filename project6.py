##rendomly generate math problem##
##also add timer##

import random
import time
#constant value
OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERATND =12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERATND)
    right = random.randint(MIN_OPERAND,MAX_OPERATND)
    operator = random.choice(OPERATORS)

    expr = str(left) +" "+operator + " " + str(right)
    answer =eval(expr)   # eval function used to generate the arithmatic operation automatically
    return expr, answer

wrong = 0
input("press enter to start!")
print("-----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):

    expr,answer = generate_problem()
    while True:
        guess = input("problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong +=1

end_time = time.time()
total_time =round(end_time - start_time)

print("----------------------")
print("Nice work!you finish in",total_time,"seconds")

