import os, time
inventory = []

try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except:
  pass 

def addItem():
  time.sleep(2)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  item = input("Item to add > ").title()
  inventory.append(item)
  print("Item added")

def viewItem():
  time.sleep(2)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  seen = []
  for item in inventory:
    if item not in seen:
      print(f"{item} {inventory.count(item)}")
      seen.append(item)

  time.sleep(2)

def removeItem():
  time.sleep(2)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  item = input("Item to remove > ").title()
  if item in inventory:
    inventory.remove(item)
    print("Item removed")
  else:
    print("You don't have that item")

while True:
  time.sleep(2)
  os.system("clear")
  print("🌟RPG Inventory🌟")
  print()
  menu = input("1: Add\n2: View\n3: Remove\n> ")
  if menu == "1":
    addItem()
  elif menu == "2":
    viewItem()
  elif menu == "3":
    removeItem()
  else:
    print("Invalid input")

  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()