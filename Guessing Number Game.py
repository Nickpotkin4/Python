print("Welcome to the Guessing Number Game.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Okay, let's play!")
print()

correctNumber = 4200
attempt = 1

while True:
    playerGuess = int(input("Enter a number between 1 and 1,000,000: "))
    print()
    if playerGuess < 0:
      print("Sorry, you can't guess a negative number. Try again.")
      exit()
    if playerGuess < correctNumber:
      print("That number is too low. Try again!")
      print()
      attempt += 1
    elif playerGuess > correctNumber:
      print("That number is too high. Try again!")
      print()
      attempt += 1
      continue
    elif playerGuess == correctNumber:
      print("You've won! Hooray!")
      print()
      break
    else:
      print("That number is not one I recognize.")
print("It took you", attempt, "attempt(s) to guess the correct answer.")
quit()