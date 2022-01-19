"""
With this code, the output will be a list with the first 'n' numbers of the fibonacci serie.
"""

def fibonacciNumbers(num):
    print("The first", num ,"numbers of the fibonacci series are:")
    n1=0
    n2=1
    print(n1)
    print(n2)
    for i in range (num-2):
        print(n1+n2)
        aux=n1
        n1=n2
        n2=aux+n1


fibonacciNumbers(10)

