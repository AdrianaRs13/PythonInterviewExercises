def fibonacci(num):
    n1=0
    n2=1
    print(n1)
    print(n2)
    for i in range (num-2):
        print(n1+n2)
        aux=n1
        n1=n2
        n2=aux+n1
        
fibonacci(10)

