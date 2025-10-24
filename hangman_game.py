import random

word=["apple","banana","mango","grapes","papaya"]
life_lines=6

hangman=[r'''
-------------
|     O     |
|    /|\    |         
|    / \    |
------------- 
''',
r'''
-------------
|     O     |
|    /|\    |
|    /      |
------------- 
''',

r'''
-------------
|     O     |
|    /|\    |
|           |
|           |
-------------  
''',
r'''
-------------
|     O     |
|    /|     |
|           |
|           |
-------------   
''',
r'''
-------------
|     O     |
|     |     | 
|           |
-------------  
''',
r'''
-------------
|     O     |
|           |
|           |
|           |
-------------        
''',
r'''
-------------
|           |
|           |
|           |
|           |
------------- '''                                 
]


#word generation
word_generation=random.choice(word)
print(word_generation)

# generating blanks

word_guess=[]
for i in range(len(word_generation)):
    #word_guess.append("_")
    word_guess+='_'
print(word_guess)

game_over=False
while not game_over:

    guessed_letter=input("Guess a letter:")

    for position in range(len(word_generation)): #apple
        letter=word_generation[position]  #word_generation[0]=a
        if letter==guessed_letter:
            word_guess[position]=guessed_letter
    print(word_guess)

    if guessed_letter not in word_generation:
        life_lines-=1
        
        if life_lines==0:
            game_over=True
            print("the game is over you lost")
            
    if '_' not in word_guess:
        game_over=True
        print("you won the game") 
        
    print(hangman[life_lines])

    