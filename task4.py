import random

def score_tracker(user_score, computer_score):
    """
    Function to print the scores.
    """
    scores = {"Your score": user_score, "Computer score": computer_score}
    for key, value in scores.items():
        print(f"{key}: {value}")

def game(user_score, computer_score):
    """
    Function to execute one round of the game.
    """
    print("""
    Welcome to the Rock Paper Scissor Game. Let's Begin!
    Options:
    Rock
    Paper
    Scissor
    """)
    options = ["rock", "paper", "scissor"]
    user_input = input("Enter your choice: ").lower()
    computer_choice = random.choice(options)

    if user_input not in options:
        print("Invalid choice! Please choose Rock, Paper, or Scissor.")
        return user_score, computer_score

    print(f"Your choice: {user_input}")
    print(f"Computer's choice: {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissor" and computer_choice == "paper") or \
         (user_input == "rock" and computer_choice == "scissor"):
        print("You won this round!")
        user_score += 1
    else:
        print("Computer won this round!")
        computer_score += 1

    score_tracker(user_score, computer_score)
    return user_score, computer_score

def main():
    """
    Main function to control the flow of the game.
    """
    user_score = 0
    computer_score = 0

    while True:
        user_score, computer_score = game(user_score, computer_score)
        another_round = input("Want to play another round (yes/no)? ").lower()
        if another_round == "no":
            print("Thanks for playing! Final scores:")
            score_tracker(user_score, computer_score)
            break
        elif another_round != "yes":
            print("Invalid input! Please enter 'yes' or 'no'.")


main()
