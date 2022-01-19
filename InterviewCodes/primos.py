"""
    With this function you can determine if a number is a Prime or not. 
    The output will be either "Not Prime" or "Is Prime" depending on the input.
"""
def isPrime(n):
    for i in range(2, n):
        if (n % i == 0):
            return True
        return False


num = 13
a = isPrime(num)
if a:
    print('Not prime')
else:
    print('Is Prime')