import os, time 
toDoList = []

def printList():
  print()
  for items in toDoList:
    print(items)
  print()
  time.sleep(2)
  os.system("clear")

while True:
  menu = input("ToDoList Manager\n\nDo you want to view, add, edit, or remove an item from the to do list?\n")
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n")
    if item in toDoList:
      print("This item is already in the list")
    else:
      toDoList.append(item)
  elif menu=="remove":
    item = input("What do you want to remove?\n")
    check = input("Are you sure you want to remove this?\n")
    if check[0]=="y":
      if item in toDoList:
        toDoList.remove(item)
  elif menu=="edit":
    item = input("What do you want to edit?\n")
    new = input("What do you want to change it to?\n")
    for i in range(0,len(toDoList)):
      if toDoList[i]==item:
        toDoList[i]=new
  elif menu=="delete":
    toDoList = []
  time.sleep(1)
  os.system('clear')