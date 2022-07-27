class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        new_node.next = None
        if self.head is None:
            self.head = new_node
        else:
            first_node = self.head
            while first_node.next != None:
                first_node = first_node.next
            first_node.next = new_node
    
    def printlist(self):
        first_node = self.head
        while True:
            print(first_node.data)
            if first_node.next != None:
                first_node = first_node.next
            else:
                break





llist = LinkedList()

llist.append(10)
llist.append(20)
llist.append(30)
llist.append(40)
llist.printlist()
