# Binary Search Tree (BST)
# -------------------------------------------------------------------------

# BST INSERTION:
# ---------------

# 3 Things for insertion:

# 1. Main Tree variable 
# 2. Small values stored as LEFT child
# 3. Big values stored as RIGHT child
 
# eg: 11 20 13 8 53 31 21 10 50

# 11 is main tree root
# now 20 > 11 now 20 becomes right child to 11
# now 13 > 11, 20 > 11 now 13 becomes left child to 20
# now 8 < 11 now 8 becomes right child to 11

# Further tree design check with Notes


# BST DELETION:
# ---------------

# 1. Only one value -> Delete it 
# 2. Only one side child and this child also has child.
    # eg: 11 child is 6 and 6 child is 9 delete 6 and assign 9 to main root.
# 3. if root has multiple childs and childs as multiple childs.
    # Two concepts here used
    # 1. In order predecessor
    # 2. In order successor

    # IP: It goes on left side from root in tree here 11 left side, then find the biggest value among  all and assign the value to root value 11 = finded big value.

    # IS: opposite to IP right side child of root value and find small one update to root and delete all values in right root.

#BST Read(Traverse):
# BST 3 types
"""
1. In order Traverse  (Left, Root, Right)
2. Pre order Traverse (Root, Left, Right)
3. Post order Traverse
"""

# IN order:

"""
Only 3 Rules:(Left, Root, Right)

First start from Main Root

1.Go Left from Main root and check it is root if it is then check it has left value.
2.Go For left first print it, then print it's root
3.Go For Right from root if it has print it.

This cycles finishes then reveret back to previous (use recurssion)
"""

#Pre order:

"""
1.Check it is root print it
2.Go for left if it has print it, then revert back root is already printed.
3.Go for right it has print it, if doesn't revert to root
"""