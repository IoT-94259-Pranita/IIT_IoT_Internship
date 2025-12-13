num = input("Enter a 5 digit number: ")
if num == num[::-1]:
    print("The number is a Palindrome")
else:
    print("The number is not a Palindrome")