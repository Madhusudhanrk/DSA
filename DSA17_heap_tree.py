#HEAP TREE 
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
 
#min heap tree

class MinHeap:
    def __init__(self,capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    #Helper Methods

    #To get index of parent, left and right child indexs based on param index from array--------------------------------------------------------------------

    def getParentIndex(self,index):
        return (index-1)//2

    def getLeftChildIndex(self,index):
        return (2*index)+1

    def getLeftChildIndex(self,index):
        return (2*index)+2
    
    #To check the given index has parent, left, right Nodes --------------------------------------------------------------------

    def hasParent(self,index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) >= self.size

    def hasRightChild(self,index):
        return self.getRightChildIndex(index) >= self.size
    
    #To return the value of the given index --------------------------------------------------------------------

    def parent(self,index):
        return self.storage[self.getParentIndex(index)]

    def leftChild(self,index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self,index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    #This method used to ReHeapify our tree----------------------------------- 
    def swap(self,index1,index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

        
