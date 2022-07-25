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
        if self.head is None:
            new_node = Node(data)
            new_node.next = new_node
            self.head = new_node
        else:
            new_node = Node(data)   
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
                break
            temp.next = new_node
            new_node.next = self.head
             
        
        # new_node = Node(data)
        # temp = self.head
        #  #usually we assign new node next to None bur Circular list self.head it circle
        # new_node.next = self.head

        # if self.head is not None:
        #     while temp.next != self.head:
        #         temp = temp.next
        #     temp.next = new_node
        # else:
        #     new_node.next = new_node
        # self.head = new_node

    def cprintlist(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break


Clist = CircularLinkedList()
# Clist.push(10)
# Clist.push(20)
# Clist.push(30)
Clist.append(10)
Clist.append(20)
Clist.append(30)
Clist.append(40)

Clist.cprintlist()