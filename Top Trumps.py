import os, time, random

trumps = {}
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Monica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}

while True:
  print("TOP TRUMPS")
  print()
  print("Characters")
  print()
  for key in trumps:
    print(key)
  print()
  user = input("Pick your character\n> ").strip()
  if user not in trumps:
    print("Character not found! Try again.")
    time.sleep(1)
    os.system("clear")
    continue
  comp = random.choice(list(trumps.keys()))
  print(f"Computer has picked {comp}")
  print()

  print("Choose your stat: Intelligence, Speed, Guile & Baldness Level")

  answer = input("> ").capitalize()
  if answer not in trumps[user]:
    print("Stat not found! Try again.")
    time.sleep(1)
    os.system("clear")
    continue
  print()
  print(f"{user}: {trumps[user][answer]}")
  print(f"{comp}: {trumps[comp][answer]}")

  if trumps[user][answer] > trumps[comp][answer]:
    print(user, "wins")
  elif trumps[user][answer] < trumps[comp][answer]:
    print(comp, "wins")
  else:
    print("Draw")

  print()
  time.sleep(2)
  os.system("clear")