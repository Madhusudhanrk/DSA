#HEAP TREE 

#heap is used to store data in storage in the form of array using heap tree structure.
"""
1.Heap tree is like binary tree but doesn't mantain lower value should be this or upper value this side.

2.Heap tree only follow one rule First insert Root Node, Then insert left and right, always follow LEFT -> RIGHT node insertion.

3.Heap use two types of tree methods Min and Max

4.Min method tree roots are always smaller than it's leaf nodes, Max is opposite Max always follows tree root should be bigger than it's leaf nodes.
Industry prefer: MAX

"""
#Insertion In Heap Tree

"""
1.Create A Node with ROOT,LEFT,RIGHT first insert a number to root then left,right if root node is smaller compared to left or right node just swap for bigger values as we following MAX method.

2.It follow complete binary tree rule what it means?
    The leaf node must assign the value to left first if only having one value, if two values present each go one side.

3.In heap root node arrange based on child nodes 

"""

# # Python program for implementation of heap Sort 
  
# # To heapify subtree rooted at index i. 
# # n is size of heap 
# def heapify(arr, n, i): 
#     largest = i # Initialize largest as root 
#     l = 2 * i + 1  # left = 2*i + 1 
#     r = 2 * i + 2  # right = 2*i + 2 
    
#     # See if left child of root exists and is 
#     # greater than root 
#     if l < n and arr[i] < arr[l]: 
#         largest = l 
  
#     # See if right child of root exists and is 
#     # greater than root 
#     if r < n and arr[largest] < arr[r]: 
#         largest = r 
  
#     # Change root, if needed 
#     if largest != i: 
#         arr[i],arr[largest] = arr[largest],arr[i] # swap 
        
#         # Heapify the root. 
#         heapify(arr, n, largest) 
  
# # The main function to sort an array of given size 
# def heapSort(arr): 
#     n = len(arr) 
  
#     # Build a maxheap. 
#     # Since last parent will be at ((n//2)-1) we can start at that location. 
#     for i in range(n // 2 - 1, -1, -1): 
#         heapify(arr, n, i) 
  
#     # One by one extract elements 
#     for i in range(n-1, 0, -1): 
#         arr[i], arr[0] = arr[0], arr[i] # swap 
#         heapify(arr, i, 0) 
  
# # Driver code to test above 
# arr = [ 12, 11, 13, 5, 6, 7] 

# heapSort(arr) 
# n = len(arr) 

# print("Sorted array is") 
# for i in range(n): 
#     print (arr[i]) 


#Deletion In Heap Tree
 
#MIN based Heap tree

class MinHeap:
    def __init__(self,capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.size = 0

    #Helper Methods

    #To get index of parent, left and right child indexs based on param index from array--------------------------------------------------------------------

#using the formula it get index of the parent, but we need to give the child index
    def getParentIndex(self,index):
        return (index-1)//2
#if we give parent index it will give left child index, even it in right branch if u give parent index if that parent has left node it will give the index.
    def getLeftChildIndex(self,index):
        return (2*index)+1
#getting right child index same.
    def getRightChildIndex(self,index):
        return (2*index)+2
    
    #To check the given index has parent, left, right Nodes --------------------------------------------------------------------
#checking has parent if only one root node means getParentIndex() will return -1
    def hasParent(self,index):
        return self.getParentIndex(index) >= 0
#if we give parent index it will compare
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) >= self.size

    def hasRightChild(self,index):
        return self.getRightChildIndex(index) >= self.size
    
    #To return the value of the given index --------------------------------------------------------------------
#if we send child index based on that it return the value of the parent value.
    def parentValue(self,index):
        return self.storage[self.getParentIndex(index)]
#same give parent index return get left child value.
    def leftChildValue(self,index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChildValue(self,index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    #This method used to ReHeapify our tree----------------------------------- 
    def swap(self,index1,index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

#Insert Method in Iterative ----------------------------

    # def insert(self,data):
    #     if self.isFull():
    #         return print("Heap is Full")
    #     self.storage[self.size] = data
    #     #every time value inserted size++ to get actual values count in tree
    #     self.size += 1 
    #     #heapify means based on MIN or Max choosen values inserted as per rules or construcing heap tree structure.
    #     self.heapifyUp()

    # def heapifyUp(self):
    #     #index decreased by one beacuse just to compare prev value with it.
    #     index = self.size - 1
    #     #Here checking given index node has parent
    #     #if parent present parent node > child node means just swap
    #     while (self.hasParent(index) and self.parentValue(index) > self.storage[index]):
    #         self.swap(self.getParentIndex(index),index)
    #     #after swapping getting swaped node parent index by using the parent index and present swapped value comparing and if not matched to MIN heap again swap until the tree comes to MIN Heap Structure.
    #         index = self.getParentIndex(index)

# insert method in Recursive
  
    def insert(self,data):
        if self.isFull():
            return print("Heap is Full")
        self.storage[self.size] = data
        self.size += 1 
        self.heapifyUp(self.size - 1)#newly inserted data index
        #if this executed completely entire stack will pop.

    def heapifyUp(self,index):      
        if self.hasParent(index) and self.parentValue(index) > self.storage[index]:
            self.swap(self.getParentIndex(index),index)
            self.heapifyUp(self.getParentIndex(index))
            #this code recalls same func check whether need to heapify tree or not.
        #rules:
        #just compare child and parent node based on Min heap if need to swap do it and after swapped check the parent node has parent then compare to it also till the tree heapify.

#Pop Method in Recursive----------------------------------------------

    def removeMin(self):
        data = self.storage[0]#storing first root element.
        self.storage[0] = self.storage[self.size - 1]
        #re-write first node using last node of the tree
        self.storage[self.size - 1] = None
        #making last node None
        self.size -= 1 #decreaded size
        self.heapifyDown(0)
        return data

    def heapifyDown(self,index):
        smallest = index#consider it is smallest as of now
        #step2:checking root node has left child if has root node is smaller than left node, if small left node is smallest
        if self.hasLeftChild(smallest) and self.storage[smallest] > self.leftChildValue(smallest):
            smallest = self.getLeftChildIndex(smallest)
        #step3:comparing left child and right child who is smaller and their index will store in smaller variable.
        if self.hasRightChild(smallest) and self.storage[smallest] > self.rightChildValue(smallest):
            smallest = self.getRightChildIndex(smallest)
        #step4:after here the branch will be divided to right or left branch all swapping will be done one side only either left or right
        #step5: the smallest value is not updated means smallest == index
        if smallest != index:  
            self.swap(smallest,index)
            self.heapifyDown(smallest)#here index is modified by smallest

    def heap_traverse(self):
        for i in min_heap.storage:
            print(i)

min_heap = MinHeap(8)

#heap insert Input
arr = [10,21,90,50,20,22,23,1]
for i in arr:
    min_heap.insert(i)

#heap pop -> just removes top element
# min_heap.removeMin()
# min_heap.removeMin()

#heap traverse
min_heap.heap_traverse()

# Use of heap tree
#--------------------------------------------------------

#used to find instant smallest or largest value based on MIN and Max heap.

#used to priority the task and make shedules also based on Min and Max heap.