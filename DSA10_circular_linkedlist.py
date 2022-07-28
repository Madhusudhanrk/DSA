class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    first_node = None #it's scope is for one object if u call from other object it will be none.
    def __init__(self):
        self.head = None

    def push(self, data):
        #my method
        global first_node
        new_node = Node(data)

        if self.head == None:
    #tip1: have separate control over first node push any time changing its next value.
          print("In Push")
          self.head = new_node
          new_node.next = self.head
          first_node = self.head
          return
#tip2: using Head assign previous node address to new node.
#tip3: write down in paper and solve in paper, write sudo code then write in editor.
        new_node.next = self.head
        self.head = new_node
        first_node.next = self.head

        #Hitesh method --------
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
             
        
    def delete_node(self,key):
        if self.head is not None:
            curr_node = self.head
# step1: check the key is matched with first node if matched.
#step2: if key matched then check if list have 
#only One Node---------
#make head to none
#free up the node

# more than one node-------------
#  if more than one node:
# * must change the head to 2nd node
# * relase the node memory.
# * and change the last node point to new head.
            if self.head.data == key:#checking first node matches the key
                if self.head == self.head.next:#Only if single node present and key matched
                    self.head.data = None
                    self.head.next = None
                    self.head = None
                    return
                else:#First Node matched multiple nodes present
                    present_node = self.head
                    #this while ensures that the last node will not point to deleted first_node
                    while True:
                        present_node = present_node.next
                        if present_node.next == self.head:
                            present_node.next = self.head.next
                            break
                    curr_node = None #releasing memory of first node
                    next_node = self.head.next#this 3 line head changed to next node
                    self.head = None
                    self.head = next_node
                    return
            else:
# step3:if first node not matched loop through every node by having prev_node info if node found then node next value to prev_node.next and free up memory for current node.
                while True: #this loop ensures find node and delete node except 1st node.
                    prev_node = curr_node
                    curr_node = curr_node.next
                    if curr_node.data == key:
                        prev_node.next = curr_node.next
                        curr_node = None
                        break
# step4:if node not present return msg not found.
                    else:
                        if curr_node.next == self.head:
                            print("Node Not Found!")
                            return

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
Clist.push(100)
Clist.push(202)
Clist.push(330)
Clist.append(10)
Clist.append(20)
Clist.append(30)
Clist.append(40)

Clist.printlist()