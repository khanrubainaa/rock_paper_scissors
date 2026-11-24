import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice! Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "tie"

    elif user_choice == "rock" and computer_choice == "scissors":
        return "user"

    elif user_choice == "paper" and computer_choice == "rock":
        return "user"

    elif user_choice == "scissors" and computer_choice == "paper":
        return "user"

    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    for round_number in range(1, 6):
        print(f"\n--- Round {round_number} ---")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = decide_winner(user_choice, computer_choice)

        if winner == "user":
            print("You win this round!")
            user_score += 1

        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1

        else:
            print("This round is a tie!")

        print(f"Score: You {user_score} - Computer {computer_score}")

    print("\n===== FINAL RESULT =====")
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")

    if user_score > computer_score:
        print(f"You won the game with {user_score} points!")

    elif computer_score > user_score:
        print(f"Computer won the game with {computer_score} points!")

    else:
        print(f"The game ended in a tie! Both scored {user_score} points.")

play_game()
