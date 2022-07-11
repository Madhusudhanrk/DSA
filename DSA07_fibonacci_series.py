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
    
# What is the Fibonacci sequence?

# The Fibonacci sequence is a set of integers (the Fibonacci numbers) that starts with a zero, followed by a one, then by another one, and then by a series of steadily increasing numbers. The sequence follows the rule that each number is equal to the sum of the preceding two numbers.

# The Fibonacci sequence begins with the following 14 integers:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 ...

# Each number, starting with the third, adheres to the prescribed formula. For example, the seventh number, 8, is preceded by 3 and 5, which add up to 8.

# The sequence can theoretically continue to infinity, using the same formula for each new number. Some resources show the Fibonacci sequence starting with a one instead of a zero, but this is fairly uncommon.