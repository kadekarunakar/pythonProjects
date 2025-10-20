import random

print(f"1.rock\n2.paper\n3.seissor")
player1_user=int(input("Enter the choice from the above list: "))
player2_computer=random.randint(1,3)

print(f"player1_user choice is {player1_user}")
print(f"player2_computer choice is {player2_computer}")

if(player1_user==player2_computer):
    print("It\'s a draw")

elif(player1_user==1 and player2_computer==3 ) or (player1_user==2 and player2_computer==1) or (player1_user==3 and player2_computer== 2):
    print("you wins")
else:
    print("you lost the game")
