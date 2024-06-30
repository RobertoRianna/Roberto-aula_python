#funzioni. sequnza di fibonacci fino ad n


def fibonacci(n):
    a=1
    b=1
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        
    return b
    

    
fibonacci(100)
