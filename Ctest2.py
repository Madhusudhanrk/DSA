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


    def node_count(self):
        first_node = self.head
        self.count = 1
        while(first_node.next is not self.head):
            self.count += 1
            first_node = first_node.next
        print(self.count)
        return self.count

    def to_circular(self,head):
        start = head

        while head.next != None:
            head = head.next

        head = start
        return start

    def delete_node(self,key):
        if self.head is not None:
            curr_node = self.head
# step1: check the key is matched with first node if matched.
#step2: if key matched then check if list have 
# more than one node-------------
#  if more than one node:
# * must change the head to 2nd node
# * relase the node memory
# * and change the last node point to new head.
            if self.head.data == key:
                if self.head == self.head.next:#Only if single node present and key matched
                    self.head.data = None
                    self.head.next = None
                    self.head = None
                    return
                else:#First Node matched multiple nodes present
                    present_node = self.head
                    while True:
                        present_node = present_node.next
                        if present_node.next == self.head:
                            present_node.next = self.head.next
                            break
                    curr_node = None #releasing memory of first node
                    next_node = self.head.next
                    self.head = None
                    self.head = next_node
                    return
            else:
                while True:
                    prev_node = curr_node
                    curr_node = curr_node.next
                    if curr_node.data == key:
                        prev_node.next = curr_node.next
                        curr_node = None
                        break
                    else:
                        if curr_node.next == self.head:
                            print("Node Not Found!")
                            return
    
    
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

# llist.push(90)
# llist.push(120)
# llist.push(40)
# llist.push(80)


llist.append(100)
llist.append(200)
llist.append(300)
llist.append(400)
llist.append(500)
llist.append(600)

# llist.delete_node(80)

llist.printlist()
llist.node_count()
