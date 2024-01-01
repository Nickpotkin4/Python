import random
print("Infinity Dice 🎲")
print()

playGame = "yes"

def rollDice(sides):
  print("You rolled ", random.randint(1, sides))
  print()

sides = int(input("How many sides?: "))
print()

while playGame == "yes":
  rollDice(sides)
  playGame = input("Roll Again?: ")
  print()
quit()