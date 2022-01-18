def isPalindrome(s):
    l = int(len(s))
    for i in range(l/2):
        if s[i]!=s[l-i-1]:
            return False
    return True
            

 
s = "apapa"
print(isPalindrome(s))