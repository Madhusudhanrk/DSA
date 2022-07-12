# calculating performance of an application 2 ways:

# 1. find time when strat and subtract the time when execution end (not so good)

# 2. Big O notation good


# Way 1:

# calculatestarttime()

# def func():
#     ....

# calculateendtime()

# check difference  =  performance of code

# pros:
#   easy to implement

# cons:
#   it based on computer or device  (low power device will be slow)
#   Based on the processing on that time (running another program same time will effect)

  

# Way 2: consiously writting code on O notation
# Time Complexity or O(n) 
# -----------------------

# In DSA we have concept of calculating the performance of a code, for that we use O of n.

# O = Stands for Counting operations or performance based on operations

# n = Stands for input given, Based on input a program many run multiple times.

# Why We need to Use DSA and O of n concept.

# => As a programmer we need to ensure whatever the code we written it should run on every computer whether it as new Apple silicon or old Intel Pentium chip it need to run.


# a = a + 1               => 2 constant operations, adding a + 1, a = a + 1 it will end.
#                         => 2 or O(1) 

# for(i = 1; i < n; i++)  => 1 constant 5n based operations, i = 1 constant based on ninput 5 operations
#     a = a + 1           => 5n + 1 or O(n)


# for(i = 1; i < n; i++)     => Outside loop 1 N and Inside loop 1 N, based on Outside loop N input 
#     a = a + 1                 inside Loop operations will change. 
#     for(j = 1; j < n; j++) => 5n + 1 and 5n + 1 or O(n square)
#         b = b + 1
               

# How program performance calculated?

# =>Best case
# =>Average case
# =>Worst case

# As a programmer we need to avoid the worst case using DSA
# 1.find the fastest growing term
# 2.Remove the coefficient(constant) with fastest growing term. WE GET O(INSIDE TERM)

# O(3),O(5),O(8)          = O(1) any way it is constant all will execute one time only

# O(3n),O(5n),O(8n)       = O(n) avoid count of operations,consider only n it only effect program.

# O(300n),O(300n + 50000) = O(n) avoid count of operations and constant ,consider n it effect program. 
                            
# O(2n square), O(10n square) = O(n square) avoid operations may depend only on n square

# 2n^2 + 2n + 3          = n^2 + n or O(n^2) avoid n compare to N^2 is small as math

# DSA Cases (best,average,worst) best -> worst below
# ---------
# Input of n and N case also is important

# O(1)                    => constant time Complexity
# O(log n)                => logarithmic time Complexity
# O(n)                    => linear time Complexity
#                            if input grows time also grows linear to run the peice of code.
#                            eg: l = [5 elemnts] , l = [50 elemnts] linearly time grows
# O(n log n)              => linear logarithmic time Complexity
# O(n ^ 2)                => quadratic time Complexity
# O(n ^ 3)                => qube time Complexity
# O(2 ^ N)                => Exponential
# O(N!)                   => Factorial

# How to calculate:
# -----------------

# * we Must read step by step in algorithm and evaluate them in Big O notation the give priority to the worst case like O(N!), O(2 ^ N), O(n ^ 3), O(n ^ 2).

# Big O notation.jpg check it for more



# O(1)                    => constant time Complexity*************************************


# def const():
#       i = 0 
#       sum = 0 
#       while i < 1000000: # it doesn't matter 1 or 1M it will work only one time no user input based work here so it is constant or O(1).
#             sum  = sum + i
#             i +=1
#       print(sum)

# const()
#COMMON WORDS =  Doctor treating only 10 persons per day with 30 min/person

# O(log n)                => logarithmic time Complexity ********************************

# log (base^n) = n  or log 2^3 = 8

# logarithmic means getting same output by powering base number with another number, eg:log 2^3 = 8.

# why we need logarithmic?
#      using logarithmic we can divide a sequence of things into small parts or instead of searching element by element we can use logarithmic based binary search.

#It will work based on n value but it won't iterate value by value either it will divide into 2^number steps which equal to n val, based on that code executed means is O(log n).

# in simple terms no need to loop entire sequence(original size) using logarthmic skipping sequence in loop.
# def log(n):
#   for i in range(n):
#         if n==0:
#               return
#         print(n)
#         n = n//2
        
# log(10)

#COMMON WORDS =  Doctor treating selected persons from n number of person's coming per day.


# O(n)                    => linear time Complexity ****************************************

#                            if input grows time also grows linear to run the peice of code.
#                            eg: l = [5 elemnts] , l = [50 elemnts] linearly time grows

# def log(n):
#       for i in range(1,n+1):
#         print(i)        
# log(10)

#COMMON WORDS =  Doctor treating people 1 by 1 of n number coming entire day each one take 30min.
#                linearly growing.


# O(n log n)              => linear logarithmic time Complexity


# it is a combination of log N and N, Here based on O(log n) inside linear loop running in time complexity O(n)

def nlogn(n):
  l = n
  while n>0:#based on outer loop O(log n)
        for i in range(1,l):# inner loop work O(n)
              print(i)
        n = n // 2

nlogn(4)

#COMMON WORDS =  Doctor treating people 1 by 1 of n number coming entire day based on appointment(divided) each one take 30min.