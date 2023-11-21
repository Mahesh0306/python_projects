import random
options = ('rock','paper','scissor')

running = True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter the options(rock,paper,scissor):")
    print("player :",player)
    print("computer :",computer)
    if computer == player:
        print("Its Tie!")
    elif player == 'rock' and computer == 'scissor':
        print("You win!")
    elif player=='paper' and computer == 'rock':
        print("You win!")
    elif player == 'scissor' and computer == 'paper':
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Enter y/n :").lower()
    if not play_again == 'y':
        running = False
print("Thanks for playing!")