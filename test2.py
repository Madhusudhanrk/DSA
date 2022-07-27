class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    first_node = None
    def __init__(self):
        self.head = None

    def push(self,data):
        # new_node = Node(data)
        # temp = self.head

        # new_node.next = self.head

        # if self.head is not None:
        #     while temp.next != self.head:
        #         temp = temp.next
        #     temp.next = new_node
        # else:
        #     new_node.next = new_node
        # self.head = new_node

        # My Method
        global first_node
        new_node = Node(data)

        if self.head == None:
          self.head = new_node
          new_node.next = self.head
          first_node = self.head
          return

        new_node.next = self.head
        self.head = new_node
        first_node.next = self.head
        
         

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
llist1 = LinkedList()

llist.push(90)
llist.push(120)
llist.push(40)
llist.push(80)
llist1.push(40)
llist1.push(1000)

# llist.append(800)
# llist.append(1200)
# llist.append(400)
# llist.append(700)
# llist.append(400)
# llist.append(10000)

llist.printlist()
llist1.printlist()
