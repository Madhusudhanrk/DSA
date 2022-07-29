class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        #tip: push works on little bit mess work on paper then focus on the solution in paper.
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            new_node.next = None
            self.head = new_node
        else:
            prev_node = self.head
            new_node.next = prev_node
            prev_node.prev = new_node
            new_node.prev = None
            self.head = new_node
    
    def append(self,data):
        #tip:always keep prev node reference
        new_node = Node(data)
        if self.head is None:#tip2:separate first node and give different aproach to it.
            new_node.prev = None
            new_node.next = None
            self.head = new_node
        else:
            prev_node = self.head
            while prev_node.next:#tip3:consider every node obj by changing position.
                prev_node = prev_node.next
            prev_node.next = new_node

            new_node.prev = prev_node
            new_node.next = None
       
    def printlist(self):
        first_node = self.head
        print(first_node.data)
        while first_node.next:
            first_node = first_node.next
            print(first_node.data)


dlist = DLinkedList()
# dlist.append(10)
# dlist.append(20)
# dlist.append(30)
# dlist.append(40)
# dlist.append(50)

dlist.push(10)
dlist.push(20)
dlist.push(30)
dlist.push(40)
dlist.push(50)

dlist.printlist()