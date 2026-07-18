number = int (input("Enter a number : "))
original = number
reverse = 0
while number > 0:
    lastdigit = number % 10
    reverse = reverse * 10 + lastdigit
    number = number//10
if original == reverse:
    print("palindrome")
else:
    print("not a palindrome")