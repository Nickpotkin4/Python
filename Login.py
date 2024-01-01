def login():
  print("Replit Login System")
  print()

  correctUsername = "admin"
  correctPassword = "password"

  while True:
    inputUsername = input("What is your username: ")
    print()
    inputPassword = input("What is your password: ")
    print()
    if inputUsername == correctUsername and inputPassword == correctPassword:
      print("Welcome to Replit")
      print()
      break
    else:
      print("Incorrect username or password")
      print()
      continue
login()
exit()