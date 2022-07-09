def fib(limit,a,b):           
    if a == 0:
        print(a)
    sum = a + b
    a = b
    b = sum
    if limit >= 1:
        print(sum)
        fib(limit-1,a,b)


fib(10,0,1)
    