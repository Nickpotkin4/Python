print("Math Game!")
print()
print()

multiples = int(input("Name your multiples: "))
correct = 0
print()

for i in range(1, 11):
  print(i, "x", multiples, "= ")
  answer = int(input("> "))
  print()
  if(answer == i * multiples):
    print("You got it right!")
    print()
    correct += 1
  else:
     print("That's not correct. It should have been", i * multiples)
     print()
print("You scored", correct, "out of 10!")
if (correct == 10):
  print("Wow! A perfect score! 🥳")
exit()