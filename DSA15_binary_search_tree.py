# Binary Search Tree (BST)
# -------------------------------------------------------------------------

# BST INSERTION:
# ---------------

# 3 Things for insertion:

# 1. Main Tree variable 
# 2. Small values stored as LEFT child
# 3. Big values stored as RIGHT child
 
""" eg: 11 20 13 8 53 31 21 10 50 valuesssssssssssssssssssssss"""

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
1. In order Traverse   (Left, Root, Right)
2. Pre order Traverse  (Root, Left, Right)
3. Post order Traverse (Left, Right, Root)
"""
"""
How to Traverse?

* First ask it is root, if it is Appley the 3 rules for In, pre, post orders
* Check and remember every root must print Left,right,root in every root node while backtracking.
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

# Post Order

"""
1.first go for left side routes and find last value on the last route if it is left print it.

2. Then prefer right side same till end then print

3. while backtracking then only prefer root value and print it.
"""

class Node:
    #step1:Create Node with 3 variables left(node addr or obj), data(key), Right(node addr)
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key #key_data is the actual data_value in root

class BinarySearchTree:
    #step2:create root variable assign the Node into root now root contain node 3 variables
    def __init__(self, root = None):
        self.root = root 
        #root contains a node inside left, right values addr and data or key.

    def get_root(self):
        return self.root
    # step3: create insert function if root empty create Node and assign to root
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_helper(self.root, key)
    #step4: if root contain a node, check the root.key is greater or lesser than the value ur passing.

    #step5: if value is > then check the root left is empty or not, if empty create node, if not empty again recall the function using recurrsion with updated root.

    #step6: same for the value is < then do the same procedure, create new root in right side.
    def insert_helper(self, this_node, key):
        if this_node.key > key:#this_node is previously created and here key is new value.
            if this_node.left is None:#if prev.root left is empty create New root or node.
                this_node.left = Node(key)
            else:
                self.insert_helper(this_node.left, key)
        
        else:
            if this_node.right is None:
                this_node.right = Node(key)
            else:
                self.insert_helper(this_node.right, key)