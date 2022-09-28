class Node:

    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearch:

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_helper(self.root,key)

    def insert_helper(self,parent_node,key):
        if key < parent_node.key:
            if parent_node.left is None:
                parent_node.left = Node(key)
            else:
                self.insert_helper(parent_node.left,key)
        else:
            if pare