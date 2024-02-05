from replit import db
import datetime, os, time

def addEntry():
  time.sleep(2)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("Enter entry > ")
  db[timestamp] = entry

def viewEntry():
  keys = db.keys()
  for key in keys:
    time.sleep(2)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if (opt.lower()[0] == "e"):
      break


passwordEntered = input("Enter password to access diary > ")
print()
if passwordEntered != "lokirules":
  print("Incorrect password. Try again.")
  print()
  time.sleep(2)
  os.system("clear")
  exit()
else:
  print("Welcome to your diary!")
  print()
  time.sleep(2)
  os.system("clear")
while True:
  os.system("clear")
  menu = input("1. Add\n2. View\n")
  print()
  if menu == "1":
    addEntry()
  elif menu == "2":
    viewEntry()
  else:
    print("Invalid input.")
    time.sleep(2)
    os.system("clear")

