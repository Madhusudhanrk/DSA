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
        
        #Hitesh Mehod - find patterns complete in less lines
        new_node.next = self.head  

        #write down in paper and check any similarity values for fill next in node using any already defined variables like in this case head
        #head holds newly created node here matches with every new node next.
#pro tip: write down on paper find any pattern in next and prev posistions finish in less lines.
        if self.head is not None:
            self.head.prev = new_node
            #here head.prev starting from 2nd node use newly creating node to assign.

        self.head = new_node


        # My Method
        # if self.head is None:
        #     new_node.prev = None
        #     new_node.next = None
        #     self.head = new_node
        # else:
        #     prev_node = self.head
        #     new_node.next = prev_node
        #     prev_node.prev = new_node
        #     new_node.prev = None
        #     self.head = new_node

        
    
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

    def insertAfter(self,prev_node,data)  :
        if prev_node and data:#if they contain data it will enter
            new_node = Node(data)
            new_node.next = prev_node.next
            new_node.prev = prev_node
            prev_node.next = new_node
            if prev_node.next is not None:#if prev node is last node no need to check last node next.
                new_node.next.prev = new_node
            return

    def add_to_last(self,data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = None
            new_node.prev = None
            self.head = new_node
        else:
            first_node = self.head
            while first_node.next:
                first_node = first_node.next
            last_node = first_node
            last_node.next = new_node
            new_node.prev = last_node
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
dlist.add_to_last(100)

# dlist.push(10)
# dlist.push(20)
# dlist.push(30)
# dlist.push(40)
# dlist.push(50)

dlist.printlist()