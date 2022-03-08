def CheckPalindrome(User_input):
    Backward_string = User_input[::-1]
    return User_input == Backward_string

if CheckPalindrome(input("Enter your string to check palindrome or not")):
    print("the input is a palindrome")
else:
    print("Not a palindrome")
