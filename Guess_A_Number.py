import random
#start
print("let me think of a number 1 to 50")
answer=random.randint(1,50)
easy_level_attempts=10
hard_level_attempts=5
#Attempts
def set_difficulty(level):
    if(level=='easy'):
        return easy_level_attempts
    else:
        return hard_level_attempts


#for guessing the number
def check_answer(guessed_number,answer):

    if(guessed_number<answer):
        print("your guess is Too Low")
        return attempts-1
    elif(guessed_number>answer):
        print("your guess is Too high")
        return attempts-1
    else:
        print(f"your Guess is right..The answer was {guessed_number}")
    

level=input("choose level of difficulty..Type 'easy' or 'hard': ").lower()
attempts=set_difficulty(level)
guessed_number=0
while(guessed_number!=answer):
    print(f"you have {attempts} remaining to guess the number!")
    guessed_number=int(input("make a guess:"))
    attempts=check_answer(guessed_number,answer)
    if(attempts==0):
        print("you are out of guesses.. you lose!!")
    else:
        print("try again")


    



