#HEAP TREE 
"""
1.Heap tree is like binary tree but doesn't mantain lower value should be this or upper value this side.

2.Heap tree only follow one rule First insert Root Node, Then insert left and right, always follow LEFT -> RIGHT node insertion.

3.Heap use two types of tree methods Min and Max

4.Min method tree roots are always smaller than it's leaf nodes, Max is opposite Max always follows tree root should be bigger than it's leaf nodes.
Industry prefer: MAX

"""
#Insertion In Heap Tree

"""
1.Create A Node with ROOT,LEFT,RIGHT first insert a number to root then left,right if root node is smaller compared to left or right node just swap for bigger values as we following MAX method.

"""

#Deletion In Heap Tree

"""
Step 1 − Remove root node.
Step 2 − Move the last element of last level to root.
Step 3 − Compare the value of this child node with its parent.
Step 4 − If value of parent is less than child, then swap them.
Step 5 − Repeat step 3 & 4 until Heap property holds.
"""