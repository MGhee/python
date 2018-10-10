import random
print("rock...")
print("paper...")
print("scissors...")

player = input("Player, playes: ").lower()
rand_num=random.randint(0,2)
if rand_num == 0:
    computer="rock"
elif rand_num == 1:
    computer="paper"
else:
    computer="scissors"
print(f"Computer plays {computer}")

if player == "rock" and computer == "paper":
    print("computer wins!")
elif player == "rock" and computer == "scissors":
    print("player wins!") 
elif player == "paper" and computer == "scissors":
    print("computer wins!")  
elif player == "paper" and computer == "rock":
    print("player wins!")
elif player == "scissors" and computer == "paper":
    print("player wins!")
elif player == "scissors" and computer == "rock":
    print("computer wins!")
elif player == computer:
    print("It is a tie!")
else:
    print("smth went wrong")
