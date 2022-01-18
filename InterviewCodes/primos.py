def primos(n):
    for i in range(2, n):
        if (n % i == 0):
            return True

num = 4
a = primos(num)
if a:
    print('Not prime')
else:
    print('Is Prime')