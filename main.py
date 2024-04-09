print("Palindrome Checker")
print()

def palindrome(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])

while True:
  word = input("Input a word > ")
  print()
  if palindrome(word):
    print(f"{word} is a palindrome. Yay!")
  else:
    print(f"{word} is not a palindrome. Sorry!")

  print()
  again = input("Try again? (y/n) > ")
  print()
  if again == "y":
    continue
  else:
    break





