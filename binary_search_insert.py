class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,data):
        if(self.data == data):
            raise Exception("Data is Duplicate")
        elif data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    