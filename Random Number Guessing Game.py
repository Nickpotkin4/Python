import random

print("Totally Random One-Million-to-One ")
print()

myNumber = random.randint(1, 1000000)
attempt = 1

while True: 
  user_guess = int(input("Pick a number between 1 and 1,000,000: "))
  if user_guess < myNumber:
    print("That number is too low. Try again!")
    print()
    attempt += 1
  elif user_guess > myNumber:
    print("That number is too high. Try again!")
    print()
    attempt += 1
    continue
  elif user_guess == myNumber:
    print("You are a winner! 🥳🥳")
    print()
    break
    exit()
  else:
    print("That is not a number I recognize.")
    exit()
print("It took you", attempt, "attempt(s) to get the correct answer.")
exit()