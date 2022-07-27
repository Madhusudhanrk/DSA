class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        
        new_node = Node(data)
        new_node.next = new_node
        self.head = new_node


    def append(self,data):
        #tip: In circular list every new node we append it's next should be point to first node.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        new_node.next = self.head
        #tip 2: design in paper first then come to code.
        if self.head is not None:
            first_node = self.head
            while first_node.next != self.head:
                first_node = first_node.next
            first_node.next = new_node
        #tip3:first implement append in single linked list then come for circular linked list.
             
        
        

    def printlist(self):
        #tip1:For print if the node end == head(first_node) then that is last node stop it
        first_node = self.head
        while True:
            print(first_node.data)
            if first_node.next != self.head:
                first_node = first_node.next
            else:
                break


Clist = CircularLinkedList()
# Clist.push(10)
# Clist.push(20)
# Clist.push(30)
Clist.append(10)
Clist.append(20)
Clist.append(30)
Clist.append(40)

Clist.printlist()