#Queue name it self says First In First Out (FIFO)

#Enqueue for Insertion

#Dequeuq for Deletion

# In queue Insertion from rear and deletion from front
# Front = deletion 
# Rear  = Insertion
# index   0   1  2  3  4 
# list = [10,20,30,40,50]
#         F            R
#initially Front and Rear is O, when the values inserted the rear will move from 0 to 1 and 2 till length of the list

# but Front won't move from O because the values deleted from Front and next values will shift their indexes.\

# Eg: Ticket Counter is Front and Line is Rear, Counter stay in place, Line will Reduce.



#3 cases for implementing queue in python

#worst Case
#----------

# cars = []
# cars.append("car1")
# cars.append("car2")
# cars.append("car3")
# print(cars)#['car1', 'car2', 'car3']

# cars.pop(0)# o/p:car1 worked but every time it delete one value every value must change index it is very resource consuming.

# Best case 1st type
#----------

# from collections import deque

# numbers = deque()
# numbers.append("car1")
# numbers.append("car2")
# numbers.append("car3")
# # print(numbers) deque(['car1', 'car2', 'car3'])

# print(numbers.popleft()) #car1 it does not shift values just pop from left side
# # IndexError: pop from an empty deque / If all Flushed again poping it error.

# Best Case 2nd type
#-------------------

from queue import Queue

cars = Queue()
cars.put("car1")
cars.put("car2")
cars.put("car3")

# print(cars.put)# it only have Queue obj <queue.Queue object at 0x0000027E56417D60>

print(cars.get()) #o/p: car1 it work purely based on class and obj u used in linked list

#if all values got it display empty if next value called not shows error
#to show error call special method to show error