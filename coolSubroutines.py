import random

def colorWord(color):
  if color == "red":
    print("\033[31m", sep="", end="")
  elif color == "green":
    print("\033[32m", sep="", end="")
  elif color == "blue":
    print("\033[34m", sep="", end="")
  else:
    print("\033[0m", sep="", end="")

def factorial(number):
  if number == 1:
    return 1
  else: 
    return number * factorial(number - 1)

def rollDice(sides):
  print("You rolled ", random.randint(1, sides))
  print()