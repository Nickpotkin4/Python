import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))//2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))//2)+12
  return strengthStat

print("⚔️ BATTLE TIME ⚔️")
print()
char1Name = input("Name your Legend:\n")
print()
char1Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(char1Name)
char1Health = health()
char1Strength = strength()
print("HEALTH:", char1Health)
print("STRENGTH:", char1Strength)
print()
print("Who are they battling?")
print()

char2Name = input("Name your Legend:\n")
print()
char2Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(char2Name)
char2Health = health()
char2Strength = strength()
print("HEALTH:", char2Health)
print("STRENGTH:", char2Strength)
print()

round = 1
winner = None  

while True:
  time.sleep(1)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")

  char1Dice = rollDice(6)
  char2Dice = rollDice(6)

  difference = abs(char1Strength - char2Strength) + 1

  if char1Dice > char2Dice:
    char2Health -= difference
    if round == 1:
      print(char1Name, "wins the first blow")
      print()
    else:
      print(char1Name, "wins round", round)
      print()
  elif char2Dice > char1Dice:
    char1Health -= difference
    if round == 1:
      print(char2Name, "wins the first blow")
      print()
    else:
      print(char2Name, "wins round", round)
      print()
  else:
    print("Their sword clash and they draw round", round)
    print()

  print()
  print(char1Name)
  print("HEALTH:", char1Health)
  print()
  print(char2Name)
  print("HEALTH:", char2Health)
  print()

  if char1Health <= 0:
    print(char1Name, "has died!")
    winner = char2Name
    break
  elif char2Health <= 0:
    print(char2Name, "has died!")
    winner = char1Name
    break
  else:
    print("And they're both standing for the next round")
    print()
    round += 1
    
time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")
exit()