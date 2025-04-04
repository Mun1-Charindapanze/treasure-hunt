import random

def get_valid_input(answer, valid_options):
    """Helper function to ensure user input is valid."""
    while True:
        user_input = input(answer).lower()
        if user_input in valid_options:
            return user_input
        else:
            print("❌ Invalid input! Please choose a valid option.")

def treasure_hunt():
    print(" Welcome to Treasure Hunt! 🏆")
    print("You see two doors:  RED and  BLUE")
    print("If YES ,now start the game")
    print ("if NO ,restart the game")
    
    # Randomly decide which door has the treasure
    treasure_door = random.choice(["red", "blue"])
    
    # List of questions and answers
    questions = [
        ("What's your favorite color? (red/blue)", ["red", "blue"]),
        ("Which would you choose - Ruby or Sapphire? (ruby/sapphire)", ["ruby", "sapphire"]),
        ("Pick a gemstone: 1) Garnet 2) Topaz (1/2)", ["1", "2"]),
        ("Fire or Water? (fire/water)", ["fire", "water"]),
        ("Hot or Cold? (hot/cold)", ["hot", "cold"])
    ]
    
    score = 0
    
    # Ask 3 random questions
    for i in range(3):
        question, options = random.choice(questions)
        print(f"\nQuestion {i+1}: {question}")
        answer = get_valid_input(f"Choose {options[0]} or {options[1]}: ", options)
        
        # Give points for answers matching the treasure door color
        if (treasure_door == "red" and answer in ["red", "ruby", "1", "fire", "hot"]) or \
           (treasure_door == "blue" and answer in ["blue", "sapphire", "2", "water", "cold"]):
            print("✅ Good choice!")
            score += 1
        else:
            print("❌ Not this time!")

    # Final door choice
    print("\n🚪 Time to choose a door!")
    choice = get_valid_input("Which door will you open? (red/blue): ", ["red", "blue"])
    
    if choice == treasure_door:
        print(f"\n Congratulations! You found the treasure behind the {treasure_door.upper()} door! 🎉")
        print(f"Your intuition score was {score}/3")
    else:
        print(f"\n Oh no! The treasure was behind the {treasure_door.upper()} door.")
        print(f"Your intuition score was {score}/3 - better luck next time!")

# Start the game
treasure_hunt()
