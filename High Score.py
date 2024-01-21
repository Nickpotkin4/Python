import time, os

while True:
  print("🌟HIGH SCORE TABLE🌟")
  print()
  f = open("highScore.txt", "a+")
  initials = input("Input your initials > ").upper()
  print()
  score = input("Input your score > ")
  print()
  f.write(f"{initials}: {score}\n")
  f.close()
  print("Added to high score table.")
  time.sleep(2)
  os.system("clear")
  
  another = input("Add another? y/n? ")
  print()
  if another == "y":
    continue
  else:
    break

