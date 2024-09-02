import random

options = ("rock", "paper", "scissors")
playing = True
user_count = 0
computer_count = 0

print("Welcome To The Game!")

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
        print(f"User_count: {user_count} \nComputer_count: {computer_count}")
    elif player == "rock" and computer == "scissors":
        print("You win!")
        user_count += 1
        print(f"User_count: {user_count} \nComputer_count: {computer_count}")
    elif player == "paper" and computer == "rock":
        print("You win!")
        user_count += 1
        print(f"User_count: {user_count} \nComputer_count: {computer_count}")
    elif player == "scissors" and computer == "paper":
        print("You win!")
        user_count += 1
        print(f"User_count: {user_count} \nComputer_count: {computer_count}")
    else:
        print("You lose!")
        computer_count += 1
        print(f"User_count: {user_count} \nComputer_count: {computer_count}")

    if not input("Play again? (yes/no): ").lower() == "yes":
        playing = False

print("Thanks for playing, See you again!")
