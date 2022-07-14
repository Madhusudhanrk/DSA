
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

def toh(n,from_bar,to_bar,aux_bar):
    if n == 1:
        print("Move disk 1 From",from_bar,"to bar",to_bar,"bar")
        return
    toh(n-1,from_bar,aux_bar,to_bar)
    print("Move disk",n,"From",from_bar,"bar","to",to_bar,"bar")
    toh(n-1,aux_bar,to_bar,from_bar)

toh(2,"A","C","B")


 