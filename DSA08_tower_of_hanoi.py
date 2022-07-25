
# intro

# Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 

# Only one disk can be moved at a time.
# Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
# No disk may be placed on top of a smaller disk

  

# The pattern here is :
"""
 - Shift 'n-1' disks from 'A' to 'B', using C.
 - Shift last disk from 'A' to 'C'.
 - Shift 'n-1' disks from 'B' to 'C', using A.
 """

 

# toh(3,"A","C","B")

#be aware of tree structure and reverse back tracking.

def toh(n,f,mid,to):#check this argument positions
    if n>0:
        toh(n-1,f,to,mid)#check this argument positions
        #here n original value is not changing just minus and passing result value
        print("Move disk",n,"From",f,"bar","to",to)
        toh(n-1,mid,f,to)
toh(3,'A','B','C')