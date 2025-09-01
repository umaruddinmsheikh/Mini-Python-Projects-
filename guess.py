import random 

print("Welcome to the number guessing game!")

while True: # outer loop for replay

    # ask for difficulty
    level = input("Choose the difficulty level (easy / medium / hard): ").lower()

    if level == "easy":
        max_number = 10
    elif level == "hard":
        max_number = 500
    else:
        max_number = 100 # medium by default
    secret = random.randint(1,max_number)
    print(f"i am thinking of a number between 1 and {max_number}.")

    tries = 0 # counter

    # guessing loop
    while True:
        guess = int(input("Enter your guess:"))
        tries += 1

        if guess < secret:
            print("too low!")
        elif guess > secret:
            print("too high!")
        else:
            print(f"correct! you guessed it in {tries} tries.")
            break
    
        # extra hint if very close
        if abs(guess - secret) <= 5:
            print("You are very close")

    # ask if they want to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("thanks for playing")

    break # exit outer loop