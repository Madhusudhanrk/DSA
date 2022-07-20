
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = None

    def push(self,new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head  = new_node

    def append(self,new_value):
        append_node =  Node(new_value)

        if self.head is None:
            self.head = append_node
            return

        last_node = self.head
        while(last_node.next): # prev_node next is None means
            last_node  = last_node.next #storing prev_node next value in last

        last_node.next = append_node

        
    def printlist(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next


Llist = LinkedList()

Llist.push(20)
Llist.append(10)

Llist.printlist()
        