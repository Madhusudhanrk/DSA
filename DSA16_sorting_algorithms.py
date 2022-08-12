from array import *

    
 
class Sort:

# Selection sort
# Pick 1st value then compare every value in array find small one and swap both and move to 2nd value then do it again, continue this till end of array.

    #step1:We need to pick every value in array with index
    #step2:just compare every value with arrow value find smallest one and swap both
    #step3:Arrow_value is shift from 0 to end array index.
    def selection_sort(self,arr):
        # 10 , 6 , 1, 4, 5
        for i in range(len(arr)):
            minimum_val_pos = i #we assume it is minimum value
            for j in range(i+1,len(arr)):
#what we assumed min_pos is greater than its next value then update min_pos by min_val index
                if arr[minimum_val_pos] > arr[j]:
                    minimum_val_pos = j
            arr[minimum_val_pos],arr[i] = arr[i],arr[minimum_val_pos]
#here just swapping the min value with the old minimum_assumed .
        self.sorted_values(arr)

#bubble sort
#compare element 1 by 1 if one is big than another swap this way at end u get big value all of them.

#so now the big value is at least so don't need to check till end so -1 index and check all values again.

#just compare current index and it's next index if current index bigger swap if not increase index numbers 

#tip: one loop is to swap values based on value size it is inner loop
    # one loop is to decrease the comparision indexes when bigger values moved to last it is outer loop.


    def bubble_sort(self,arr):
        # 10 , 6 , 1, 4, 5
        one_index = 1
        while len(arr) - one_index:
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1],arr[i]
            
            one_index = one_index + 1
        self.sorted_values(arr)    

#Insertion Sort
# step1: we are comparing from index 1(key or i) with index 0 value if index 1 smaller swap.
# step2: then increase index(key) by one and compare if index(key) < from key-1 do it till end like key is 2 means k<1,k<0 index if key is smaller than any other value swap, this way smaller value will be inserted in their place.
    def insertion_sort(self,arr):
        # 7 3 5 4 2
        for i in range(1,len(arr)):
            key = i
            j = i - 1#verifying j is less than i by one index.
            while j>=0:#conforming j no outgo by index )
                if arr[key] < arr[j]:
#checking if the key value is smaller than it's previous value
                   arr[key],arr[j] = arr[j],arr[key]
                   key = key - 1#after swap key is reduced and ready to it's next previous value.
                j = j - 1#one index decreased because key need to be compared till index 0                      
        self.sorted_values(arr)

    def sorted_values(self,data):
        for i in data:
            print(i,end=" ")


sort = Sort()
arr = array("i",[10 , 16 , 1, 4, 5])
# sort.selection_sort(arr)
# sort.bubble_sort(arr)
sort.insertion_sort(arr)
