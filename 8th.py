#Check whether a string is a palindrome.
text = input("Enter a string: ")
rev = ""

for ch in text:
    rev = ch + rev

if text == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
