# A linked list is a sequence of data structures, which are connected together via links.

# Linked List is a sequence of links which contains items. Each link contains a connection to another link. Linked list is the second most-used data structure after array. Following are the important terms to understand the concept of Linked List.

# Link − Each link of a linked list can store a data called an element.

# Next − Each link of a linked list contains a link to the next link called Next.

# LinkedList − A Linked List contains the connection link to the first link called First.

# Basic Operations
# --------------------------------------------------------------
# Following are the basic operations supported by a list.

# Insertion − Adds an element at the beginning of the list.

# Deletion − Deletes an element at the beginning of the list.

# Display − Displays the complete list.

# Search − Searches an element using the given key.

# Delete − Deletes an element using the given key.


# Types of Linked List
# ______________________________________________________________
# Following are the various types of linked list.

# Simple Linked List − Item navigation is forward only.

# Doubly Linked List − Items can be navigated forward and backward.

# Circular Linked List − Last item contains link of the first element as next and the first element has a link to the last element as previous.


# important points to be considered.
#=================================================================

# Linked List contains a link element called first.

# Each link carries a data field(s) and a link field called next.

# Each link is linked with its next link using its next link.

# Last link carries a link as null to mark the end of the list.

# Insertion Operation
# Adding a new node in linked list is a more than one step activity. We shall learn this with diagrams here. First, create a node using the same structure and find the location where it has to be inserted.
# -------------------------- worked

# Linked list is a logical datastructure not physical data structure like array or strings beacuse it doesn't present in python libaray and it is created using two classes Node and Linked list classes.

class Node: #creating a Node with data and next node reference(obj)
    def __init__(self,data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None #head stores first node reference(obj)

    def push(self,data):
        new_node = Node(data) #Created a Node with data 
        new_node.next = self.head # Next created with value None because no other node present
        self.head = new_node # Giving the Node address to Head

    def insertat(self, prev_node, data):
        if prev_node is None:
            print("Previous Node is empty")
        insert_node = Node(data) # insert Creating new node
        insert_node.next = prev_node.next # using prev_node addr pointing to next node
        prev_node.next = insert_node # giving inserting node addr to prev node to link

    def append(self,data):
        append_node = Node(data)

        if self.head is None: #Checking is any node present
            self.head = append_node# if no Node create new node if not append node
            return

        prev_node = self.head # passing the prev node address to prev_node variable
 
        while prev_node.next: # checking previous node next is none or not
            prev_node = prev_node.next # if previous node as obj in next assinging the next node obj to prev_node.

        prev_node.next = append_node# if previous node next in none! adding append node addr
        # self.head = append_node

    def deleteNode(self, key):
        #Deleting Node Takes 3 steps from linked list:
        #1. Find Node using key
        # 2. Find Previous Node and change the Node address to Deleting Node address, then the previous Node Directly point to Next Node of Deleting Node.
        # 3. Then Free up the deleting Node.


        temp = self.head #step 1: Head contains first node address
                         #step 2: Consider temp holds deleting node.

        #case 1 checking head is none.

        if temp == None:#step3: if head means temp is None no reference, No Linked list there.
            return

        #case 2 checking first node of linked list is matching or not.

        if temp is not None:
            if temp.data == key:#step 4:if head(temp) is not Nonen then match key
                self.head = temp.next#step 5: so the node(next Node) address is assigned to head
                temp = None #making node to None and garbage collector will free up memory
                return


        #case3 if given value not in first Node

        while(temp is not None):#step 6: Checks entire List until None
            if temp.data == key:# if value got it break if not.
                break
            prev = temp #step 7: getting previous Node
            temp = temp.next# step 8: getting Next node address
       

        prev.next = temp.next #step 9: assigning next node address to previous node address
        temp = None # make Deleting Node to None rest done by garbage collector.

    def del_full_list(self):
        # To del entire node just take head use it to get first Node and del that node data and using next find next node and del use loop to del all node.

        #Nodes without values only adress only left and garbage collector will collect adress.
        presentNode = self.head #step1: getting first Node obj

        while presentNode:#in list last None will point
            nextNodeObj = presentNode.next#step2:storing next node address
            del presentNode.data #step3:del current node
            presentNode = nextNodeObj# step4: assigning the prev node address to loop.

    def printlist(self):
        head = self.head #getting the address from head
        while(head):# checking head have any obj or None
            print(head.next)#printing the Node data
            head = head.next # assing next node Obj from present Node to head

if __name__ == '__main__': # checking calling from same Module or not
    llist = LinkedList()
    llist.push("Sunday")
    llist.append("Monday")
    llist.append("Tuesday")
    llist.append("Wednesday")
    llist.append("Thursday")
    llist.append("Friday")
    llist.append("Saturday")
    # llist.deleteNode("Sunday")
    llist.del_full_list()
    llist.printlist()

    # day3 = Node("Tuesday")                #INSERT PENDING*************************
    # llist.insertat(day3,"Wednesday")


