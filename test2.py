class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        temp = self.head
         
        new_node.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        new_node.next = self.head
        
        if self.head is not None:
            first_node = self.head
            while first_node.next != self.head:
                first_node = first_node.next
            first_node.next = new_node
    
    def printlist(self):
        first_node = self.head
        while True:
            print(first_node.data)
            if first_node.next != self.head:
                first_node = first_node.next
            else:
                break





llist = LinkedList()

llist.push(10)
llist.push(20)
llist.push(40)
llist.push(70)

llist.printlist()
