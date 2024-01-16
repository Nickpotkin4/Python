import random, os, time

listOfWords = ["british", "suave", "accent", "evil"]
lettersPicked = []
lives = 6

word = random.choice(listOfWords)

while True:
  time.sleep(2)
  os.system("clear")
  letter = input("Choose a letter: ").lower()

  if letter in lettersPicked:
    print("You've tried that before!")
    continue

  lettersPicked.append(letter)

  if letter in word:
    print("You found a letter!")
  else:
    print("Nope, letter not in there!")
    lives -= 1

  allLetters = True
  print()
  for i in word:
    if i in lettersPicked:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False
  print()

  if allLetters:
    print(f"You won with {lives} left!")
    break

  if lives <= 0:
    print(r"""\
       +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
      =========''' 
    
    """)
    print(f"You ran out of lives! The answer was {word}")
    break
  else:
    print(f"Only {lives} left!")

exit() 