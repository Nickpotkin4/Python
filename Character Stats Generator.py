import random

def rollDice(sides):
  result = random.randint(1, sides)
  return result

def roll6And8():
  roll6SidedDice = rollDice(6)
  roll8SidedDice = rollDice(8)
  health = roll6SidedDice * roll8SidedDice
  return health
  
print("⚔️ Character stats generator ⚔️")
print()

createAnotherCharacter = "yes"
charactersCreated = 0

while createAnotherCharacter == "yes":
  character = input("Name your warrior: ")
  health = str(roll6And8())
  charactersCreated += 1
  if(charactersCreated == 1):
    print("\033[0;32mTheir health is",health,"hp.\033[0m")
    print()
  elif(charactersCreated == 2):
    print("\033[0;34mTheir health is",health,"hp.\033[0m")
    print()
  elif(charactersCreated > 2):
    print("\033[0;31mTheir health is",health,"hp.\033[0m")
    print()
  createAnotherCharacter = input("Want to create another character?: ")
  print()
exit()