import os, time
todo = []

def add():
  time.sleep(1)
  os.system("clear")
  name = input("What is the name of the task? > ")
  date = input("When is it due by? > ")
  priority = input("What is the priority? > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Task Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("Enter 1 to view all tasks\nEnter 2 to view tasks by priority\n> ")
  if options == "1":
    for row in todo:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  time.sleep(1)

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of task to edit > ")
  found = False
  for row in todo:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in todo:
    if find in row:
      todo.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Updated!")

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of task to remove > ")
  for row in todo:
    if find in row:
      todo.remove(row)

while True:
  print("🌟Life Organizer🌟")
  print()
  menu = input("Welcome to the life organizer. Do you want to add, view, edit or remove a to do? > ").lower()
  print()
  if menu == "add":
    add()
  elif menu == "view":
    view()
  elif menu == "edit":
    edit()
  elif menu == "remove":
    remove()
  else:
    print("Invalid input")
  quit = input("Do you want to see the menu again or quit? > ").lower()
  print()
  
  if quit == "quit":
    break
  
  time.sleep(1)
  os.system("clear")