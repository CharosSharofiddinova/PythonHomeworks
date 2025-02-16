# Number Guessing Game Create a simple number guessing game
import random
def number_guessing_game():
    while True:
        secret_number = random.randint(1, 100)  
        attempts = 10  
        print("\n🔢 Welcome to the Number Guessing Game!")
        print("Guess a number between 1 and 100. You have 10 attempts.")
        for attempt in range(1, attempts + 1):
            try:
                guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess ➡️ "))
                if guess < secret_number:
                    print("📉 Too low!")
                elif guess > secret_number:
                    print("📈 Too high!")
                else:
                    print("🎉 You guessed it right! 🎯")
                    break  
            except ValueError:
                print("❌ Please enter a valid number!")       
        else:  
            print(f"\n❌ You lost! The number was {secret_number}.")
            play_again = input("Want to play again? (Y/YES/ok) ➡️ ").strip().lower()
            if play_again not in ['y', 'yes', 'ok']:
                print("👋 Thanks for playing! Goodbye!")
                break  
if __name__ == "__main__":
    number_guessing_game()