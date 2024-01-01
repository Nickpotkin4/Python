import os, time

todoList = []

def printList():
  print() 
  for item in todoList:
    print(item)
  print() 
  time.sleep(1)
  os.system("clear")

while True:
  menu = input("ToDoList Manager\n\nDo you want to view, add or edit the todo list?\n")
  if menu == "view":
    printList()
  elif menu == "add":
    item = input("What do you want to add?: ")
    todoList.append(item)
    time.sleep(1)
    os.system("clear")
  elif menu == "edit":
    item = input("What do you want to remove?: ")
    if item in todoList:
      todoList.remove(item)
    else:
      print(f"{item} was not in the list")
    time.sleep(1)
    os.system("clear")
