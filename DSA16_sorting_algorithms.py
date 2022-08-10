from array import *

# Selection sort
 
class Sort:
    def selection_sort(self,arr):
        # 10 , 6 , 1, 4, 5
        for i in range(len(arr)):
            arrow_at = i
            for j in range(len(arr)):
                if arr[arrow_at] < arr[j]:
                    arr[arrow_at],arr[j] = arr[j],arr[arrow_at]
        self.sorted_values(arr)

    def sorted_values(self,data):
        for i in data:
            print(i,end=" ")


sort = Sort()
arr = array("i",[11, 10, 2, 22, 6, 1, 4, 5])
sort.selection_sort(arr)
# sort.sorted_values()