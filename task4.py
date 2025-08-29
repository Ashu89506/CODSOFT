import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    
    print("🎮 Welcome to Rock-Paper-Scissors Game 🎮")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n")
    
    while True:
        user_choice = input("👉 Enter your choice (rock, paper, scissors): ").lower()
        
        if user_choice not in choices:
            print("❌ Invalid choice. Please choose rock, paper, or scissors.\n")
            continue
        
        computer_choice = random.choice(choices)
        print(f"🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")
        
        # Game Logic
        if user_choice == computer_choice:
            print("😐 It's a Tie!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("✅ You Win! 🎉\n")
            user_score += 1
        else:
            print("❌ You Lose! 😢\n")
            computer_score += 1
        
        print(f"📊 Score -> You: {user_score} | Computer: {computer_score}\n")
        
        play_again = input("🔄 Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n🏁 Final Score -> You: {} | Computer: {}".format(user_score, computer_score))
            print("🎯 Thanks for playing! Goodbye 👋")
            break

# Run the game
play_game()
