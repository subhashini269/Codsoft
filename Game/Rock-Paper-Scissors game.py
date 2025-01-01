import random

def get_user_choice():
    print("\n Enter your Choose:")
    for i, choice in enumerate(['Rock', 'Paper', 'Scissors'], start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            user_input = int(input("Enter your choice (1-3): "))
            if 1 <= user_input <= 3:
                return ['rock', 'paper', 'scissors'][user_input - 1]
            else:
                print("Invalid choice. Please select a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"

    if (user == 'rock' and computer == 'scissors') or \
       (user == 'scissors' and computer == 'paper') or \
       (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"\nYou chose: {user.capitalize()}")
        print(f"Computer chose: {computer.capitalize()}")
        print(determine_winner(user, computer))

        if input("\nPlay again? (yes/no): ").lower() != 'yes':
            print("Nice To Play With You,Goodbye!")
            break

if __name__ == "__main__":
    play_game()