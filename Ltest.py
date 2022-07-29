class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self,data):
        new_node = Node(data)
        # new_node.next = None
        # if self.head is None:
        #     self.head = new_node
        # else:
        #     first_node = self.head
        #     while first_node.next != None:
        #         first_node = first_node.next
        #     first_node.next = new_node

        if self.head is None:
            new_node.next = None
            self.head = new_node
        else:
            prev_node = self.head
            while prev_node.next:
                prev_node = prev_node.next
            prev_node.next = new_node
            new_node.next = None


    def delete_node(self,key):
        if self.head is not None:
            curr_node = self.head

            if self.head.data == key:
                if self.head == self.head.next:#Only if single node present
                    self.head.data = None
                    self.head.next = None
                    self.head = None
                else:
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
            if first_node.next != None:
                first_node = first_node.next
            else:
                break
        
        # head = self.head #getting the address from head
        # while(head):# checking head have any obj or None
        #     print(head.data)#printing the Node data
        #     head = head.next # assing next node Obj from present Node to head




llist = LinkedList()

llist.append(10)
llist.append(20)
llist.append(30)
llist.append(40)

# llist.push(10)
# llist.push(20)
# llist.push(30)
# llist.push(50)

# llist.delete_node(90)
llist.printlist()
