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

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None
    
    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head  = new_node
    
    def insertat(self, prev_node, new_value):
        if prev_node is Node:
            print("Previous Node is empty")
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def append(self, new_value):
        new_value = Node(new_value)

        if self.head is None:
            self.head = new_value
            return

        last = self.head
        while(last.next):
            last  = last.next
        
        last.next = new_value

    def printlist(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next

if __name__ == '__main__':
    Llist = LinkedList()
    Llist.append(10)
    Llist.push(20)

    Llist.printlist()




