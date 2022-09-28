# Binary Search Tree (BST)
# -------------------------------------------------------------------------

# Use of Binary search tree is to store and perform the given values in sorted way it is very efficient and quick to sort given values for sorting related tasks it is useful.

# Difference Between Binary search Tree vs Binary search:
# -------------------------------------------------------

# Binary search is an Algorithm works for finding a value in sequence like arrays but it takes sorted sequence input.

# Binary search tree is a Data Structure it is used to store values in sorted format getting, setting values are very efficient in BST it uses tree structure for this.

# Binary tree is sibling of BST both takes two nodes only under root node but binary tree not organized it don't share any rules like smaller value go left like.

# BST INSERTION:
# ---------------

# 3 Things for insertion:

# 1. Main Tree variable 
# 2. Small values stored as LEFT child
# 3. Big values stored as RIGHT child
# 4. Equal values ignored or throw an exception.
 
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



class Node:#step1:Create a node with value and left,right sides
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self,root = None):
        self.root = root

    #step2:create a root variable and assign the root node obj to it and crate a method to get that root node.
    def get_root(self):
        return self.root

    #step3:create a insert Method to check whether this is the first node or already having nodes in tree.
    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_helper(key,self.root)

    #step4:Creat helper method for inserting node if has some nodes in tree
    def insert_helper(self,key,parent_node):
    #step5:In helper method check from root node if the inserting value is lesser or greater than root value.

    #step6:Based on the comparision go for left or right and check if that side has any node if it there repeat same process above did just compare go one side, if has node just compare go one side till end of tree and insert it do it for every inserting value.
        if key < parent_node.key:
            if parent_node.left is None:
                parent_node.left = Node(key)
            else:
                self.insert_helper(key,parent_node.left)
        else:
            if parent_node.right is None:
                parent_node.right = Node(key)
            else:
                self.insert_helper(key,parent_node.right)



    def find_inorder_successor(self, this_node):
        myval = this_node
        while myval.left is not None:
            myval = myval.left
        return myval
    
    def delete_node(self, this_node, key):
        #this_node = root node while method starting
        #key       = use deleting node
    #S1:Getting Root node and deleting value passed to this_node and key and checking is not empty.

        #step1:checking the key and node is None or not
        if key is None: return False
        if this_node is None:
            print("This_node is None")
        
        #step2:checking the node in left side or right side and keep on digging until finding the node, if it is mathced (store the node in this_node) and go for else condition.
        if key < this_node.key:
            this_node.left = self.delete_node(this_node.left, key)
            #Note this_node.left and right is used for storing the return node in recursion process after deleting it is used to maintain structure of the tree.
        elif key > this_node.key:
            this_node.right = self.delete_node(this_node.right, key)
        # Note:Here passing entire node obj and same key value, the recursion keep on digging until key is not greater or lesser it becomes equal this_node contain deleting node.

        else:

            #case with no child or 1 child
            #Note: if left and right both is none means it return this_node.right or left eventually it is None default check with Node class.
            if this_node.left is None:
                temp = this_node.right
                this_node = None
                return temp
            elif this_node.right is None:
                temp = this_node.left
                this_node = None
                return temp

            #case with 2 child  

            temp = self.find_inorder_successor(this_node.right)
            #Finding successor and replacing successor value down with deleting node key.
            this_node.key = temp.key
            #Here down delete_node takes node right as parameter becuse we used successor so tree should re_arrange right side and successor key passed as parameter.
            this_node.right = self.delete_node(this_node.right, temp.key)
            #using this two parameters it's keep on digging until finding successor and just based on it is left or right side it's parent node side assigned to None.
            #Note:this_node.right used to remap the right side of this_node if we use in order predeccessor use this_node.left.
        return this_node

    def search(self,this_node,key):
        if this_node is None:#this code verifies  root_node is not empty
            print("Provide root node")
            return False
        if key is None:#this code verifies key is not empty
            print("Provide search key")
            return False   
        #if key matched to the current or this node key val return True
        if key == this_node.key:
            return True
        #this code ensures to keep on digging till end of the tree to find the search value in every node.

        #How it does using Recursion just take root_node.key and compare search key is smaller or bigger based on that go for one side and again recall the search funtion using present node by passing as parameter using recurssion.
        if key < this_node.key:
            self.search(this_node.left,key)
        elif key > this_node.key:
            self.search(this_node.right,key)
        else:#if not found
            print("Key Not Present")
    #This 3 types is used for taking values from tree in different ways developer need to consider which type should be used to work efficiently

    #Inorder name itself says how tree inserted way that traverse LEFT,ROOT,RIGHT
    def inorder(self,this_node):
        if this_node:
            self.inorder(this_node.left)
            print(this_node.key,", ",end="")
            self.inorder(this_node.right)
    #Preorder is used to first consider Roots then go for left and right side values.
    #It gives Root value at first and Biggest value at last.
    def preorder(self,this_node):
        if this_node:
            print(this_node.key,", ",end="")
            self.preorder(this_node.left)
            self.preorder(this_node.right)   
    #Postorder is used to first consider Leafs then go For Root
    #It gives Smallest value first then give Root at last
    def postorder(self,this_node):
        if this_node:
            self.postorder(this_node.left)
            self.postorder(this_node.right)
            print(this_node.key,", ",end="")

bst = BinarySearchTree()

my_list = [40,30,50,25,31,35,45,60,20,26,33,37,43,46,55,51,65]

for i in my_list:
    bst.insert(i)
root_node = bst.get_root()
# print(root_node.key)
bst.delete_node(root_node,30)
bst.inorder(root_node)
# bst.preorder(root_node)
# bst.postorder(root_node)