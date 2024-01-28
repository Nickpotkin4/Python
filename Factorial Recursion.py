def factorial(number):
  if number == 1:
    return 1
  else: 
    return number * factorial(number - 1)

while True:
  print("🌟Factorial Finder🌟")
  print()
  number = int(input("Input a number > "))
  print()
  print(f"The factorial of {number} is {factorial(number)}.")
  print()
  again = input("Again? y/n > ").strip()
  print()
  if again == "y":
    continue
  elif again == "n":
    break
  else:
    print("Invalid input.")
    break
exit()