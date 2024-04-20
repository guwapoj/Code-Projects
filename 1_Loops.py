#Ooremide Adegbola
#Comp163 section 2
#2/21/24
#Creating a program to play Ro-Sham-Bo. Two players make one of three hand
#signals at the same time. Hand signals represent a rock, a piece of paper, or a
#pair of scissors. Each combination results in a win for one of the players.

import random

#Constants
ROCK = 0
PAPER = 1
SCISSORS = 2

#User Input
seed = int(input("Seed : "))
player1 = input("Player 1 Name : ")
player2 = input("Player 2 Name : ")
rounds = int(input("Rounds Played : "))
#Error message if input for rounds is 0
while rounds < 1:
    print("Rounds must be > 0")
    rounds = int(input("Rounds Played : "))

#Random seed
random.seed(seed)

#Initialized win counts
player1_wins = 0
player2_wins = 0

#Game message
print(f"{player1} vs {player2} for {rounds} rounds")

for round_num in range(1, rounds + 1):

    #rounds played
    player1_choice = random.randint(0, 2)
    player2_choice = random.randint(0, 2)

    while player1_choice == player2_choice:
        print("Tie")
        player1_choice = random.randint(0, 2)
        player2_choice = random.randint(0, 2)

    #To determine the winner
    if (player1_choice == ROCK and player2_choice == SCISSORS) or \
       (player1_choice == PAPER and player2_choice == ROCK) or \
       (player1_choice == SCISSORS and player2_choice == PAPER):
        print(f"{player1} wins with {'rock' if player1_choice == ROCK else 'paper' if player1_choice == PAPER else 'scissors'}")
        player1_wins += 1
    else:
        print(f"{player2} wins with {'rock' if player2_choice == ROCK else 'paper' if player2_choice == PAPER else 'scissors'}")
        player2_wins += 1

#Output of the final result
print(f"{player1} wins {player1_wins} and {player2} wins {player2_wins}")
