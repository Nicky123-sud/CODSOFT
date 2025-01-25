import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Enter your choice as 'rock', 'paper', or 'scissors'.")
    
    # Initialize scores
    user_score = 0
    computer_score = 0
    
    while True:
        # User's turn
        user_choice = input("\nYour turn (rock, paper, scissors): ").strip().lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue
        
        # Computer's turn
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print(f"Draw! You chose {user_choice} and the computer chose {computer_choice}.")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        # Display scores
        print(f"\nScores:\nYou: {user_score} | Computer: {computer_score}")

        # Ask to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThank you for playing!")
            print(f"Final Scores:\nYou: {user_score} | Computer: {computer_score}")
            break

# Run the game
rock_paper_scissors()
