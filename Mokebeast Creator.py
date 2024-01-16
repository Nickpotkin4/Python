import os, time

mokeBeast = {}

def prettyPrint():
  print("Name\t\tType\t\tMove\t\tHP\t\tMP")
  for key, value in mokeBeast.items():
    print(f"""{key:^10}|{value["type"]:^10}|{value["move"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""")

while True:
  print("🌟MokeBeast Generator🌟")
  print()
  name = input("Input the beast name > ")
  print()
  type = input("Input the beast element > ")
  print()
  move = input("Input the beast special move > ")
  print()
  hp = input("Input the beast starting HP > ")
  print()
  mp = input("Input the beast starting MP > ")
  print()
  again = input("Again? y/n > ").strip()
  print()
  if again == "y":
    continue
  else:
    mokeBeast[name] = {"type": type, "move": move, "hp": hp, "mp": mp}
    print("----------")
    print()
    prettyPrint()
    time.sleep(2)
    os.system("clear")
    break