# class Node: 
#     def __init__(self,data):
#         self.left = None
#         self.right = None
#         self.data = data
    
#     def insert(self,data):
#         if(self.data == data):
#             raise Exception("Data is Duplicate")
#         elif data < self.data:
#             if self.left:
#                 self.left.insert(data)
#             else:
#                 self.left = Node(data)
#         else:
#             if self.right:
#                 self.right.insert(data)
#             else:
#                 self.right = Node(data)

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self,data):
#         if self.root:
#             self.root.insert(data)
#         else:
#             self.root = Node(data)

    
# BST = BST()
# values = [10,5,20,15,30,5,40,25,60]
# for i in values:
#     BST.insert(i)


class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self,root = None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_helper(key,self.root)

    def insert_helper(self,key,parent_node):
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


