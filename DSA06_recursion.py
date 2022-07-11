#Recursion
# --------

#Recursion means a function calling itself with break conditon

#Two Tracks In Recursion:

#1.Forward Trace

#2.Backward Trace

def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1) 
#1.Forward Trace

#fact(n*4)->fact(n*3)->fact(n*2)->fact(n*1)->fact(n*0)->n == 0=>return 1 to called func is fact(n*0)

#2.Backward Trace

#res = fact(n*6)<-fact(n*2)<-fact(n*1)<-fact(n*1)<- fact(1)<-fact(0)


res = factorial(4)
print(res)

# About factorial
# In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. The factorial of n also equals the product of n with the next smaller factorial: For example, The value of 0! is 1, according to the convention for an empty product.