import random, os, time
from replit import db


def addUser():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  print()
  password = input("Password: ")
  print()
  keys = db.keys()
  if username in keys:
    print("ERRROR: Username exists")
    return
  salt = random.randint(1000, 9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  db[username] = {"password": newPassword, "salt": salt}
  print("User added")
  print()


def login():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  print()
  password = input("Password: ")
  print()
  keys = db.keys()
  if username not in keys:
    print("ERROR: Username does not exists")
    return
  salt = db[username]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  if db[username]["password"] == newPassword:
    print("Logged in successfully")
  else:
    print("Username or password incorrect")


while True:
  print("🌟Login System🌟")
  print()
  menu = input("1. Add User, 2. Login > ")
  print()
  if menu == "1":
    addUser()
  elif menu == "2":
    login()
    break
  else:
    print("Invalid input")
    keys = db.keys()
    for key in keys:
      print(db[key])
  time.sleep(3)
  os.system("clear")