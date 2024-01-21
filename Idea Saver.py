import os, time, random

def add():
  os.system("clear")
  idea = input("Enter Idea > ").title()
  print()
  f = open("my.ideas", "a+")
  f.write(f"{idea}\n")
  f.close()
  print("Idea Added!")
  time.sleep(2)
  os.system("clear")

def show():
  os.system("clear")
  f = open("my.ideas", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  idea = random.choice(ideas).title()
  print(idea)
  time.sleep(2)
  os.system("clear")

while True:
  menu = input("Enter 1 to add an idea\nor enter 2 to see a random idea? > ")
  print()
  if menu == "1":
    add()
  elif menu == "2":
    show()
  else:
    print("Invalid Input")
    time.sleep(2)
    os.system("clear")