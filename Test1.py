print("=== Number Guessing Game")
print("Computer will choose a number from 1 to 50 and you have to guess it!")

secretnumber = 32
print("Computer has chosen number.")
guess1 = int(input("Enter your guess: "))
if guess1 == secretnumber:
    print("First try! You win!!")
    Win = "Winner"
else:
    print("Wrong! Try again")

    guess2 = int(input("Enter your guess: "))
    if guess1 == secretnumber:
        print("First try! You win!!")
        Win = "Winner"
