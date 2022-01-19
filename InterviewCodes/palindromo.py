"""
With this code you can verify if a word is a palindrome or not.
The output will be either "Not Palindrome" or "Is Palindrome" depending on the input.
"""

def isPalindrome(s):
    l = int(len(s))
    for i in range(int(l/2)):
        if s[i]!=s[l-i-1]:
            return False
    return True
            

s = "anitalavalatina"
a = (isPalindrome(s))
if a:
    print('Is Palindrome')
else:
    print('Not Palindrome')