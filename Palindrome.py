def palindrome(word):
  if len(word) <= 1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])


print("🌟Palindrome Checker🌟")
print()
word = input("Input a word > ").strip().lower()
print()
if palindrome(word):
  print(f"{word.capitalize()} is a palindrome. Yay!")
else:
  print(f"{word.capitalize()} is not a palindrome. Sorry!")