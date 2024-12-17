import random  

def main():
    print("Hello! Thanks for playing Guess the Number!")
    print("Are you ready to play? I'm going to think of a number, guess it now!")
    gameInt = random.randint(1, 10)
    gameDone = -1

    while gameDone != 1:
        userInput = input("Enter your number between 1 to 10\n")
        
        if not userInput.isdigit():  # Check if input is not a number
            print("Silly billy, this isn't a number!\n")
            continue  # Go back to the beginning of the loop
        
        userInput = int(userInput)  # Convert input to an integer
        
        if userInput > gameInt:
            print("That's too high!!\n")
        elif userInput < gameInt:
            print("That's too low!!\n")
        elif userInput == gameInt:
            print("That's correct!!\n")
            gameDone = 1

main()
