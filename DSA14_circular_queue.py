# 34, 45, 46, 67, 78, 89, 23, 34
# 0,  1,  2,  3,  4,  5,  6,  7
#     R   F

# INSERTION if queue FULLY filled in this case 7 index filled it again start from 0 index and start override the values from 0.

# DELETION In circular linked list there is no Shifting values if 0 index deleted The Front will shift to 1st index if 1st deleted FRONT move to 2nd index go on till end.

# 4 cases in circular queue
# ---------------------------
# why -1 start becuse front won't stay in 0 it also shift so 0 also had some value
# if front == -1 and rear == -1 means -> QUEUE is empty.

# if front == queue means -> all values deleted in queue

# if front == queue + 1 means -> QUEUE IS FULL

# if rear == size - 1 -> QUEUE is full






#((self.rear + 1) % self.size == self.front)

# 2 % 8 == 2
# 2 == 2

class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)] #based on user size creating list with None
        #because List cannot be created without any input assigning None = size.
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        #case 1 : if queue is full
        if((self.rear + 1) % self.size == self.front):
            print("Queue is full")
            return
        #case 2: if No value in queue inserting first value.
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        #case 3: some values present needed to enqueue(append)
        else:
            self.rear = (self.rear + 1) % self.size#this line ensures giving index number until reaching end of the index if size == rear - 1, it overwrite from 0 index.
            self.queue[self.rear] = data#here data assigning 

    def dequeue(self):
        #case1: checking queue is empty or not.
        if self.front == -1:
            print("Queue is already empty")
            return

        elif self.front == self.rear:
            #case2: only one value present in queue
            popval = self.queue[self.front]#just taking the single value and making F and R to orginal positions
            self.front = -1
            self.rear = -1
            return popval
        else:
            #case 3: if had multiple values this code
            popval = self.queue[self.front]#taking the value from queue.
            self.front = (self.front + 1) % self.size#this shifts front to next index
            #this code gives next next index number until size and front equals if it front again become 0 index
            return popval

    def printqueue(self):
        for i in range(0,self.size):
            if self.queue[i] is not None:
                print(self.queue[i])
            length = i
        print("Queue Lenght:",length + 1)

cq = CircularQueue(5)
cq.enqueue(190)
cq.enqueue(290)
cq.enqueue(390)

cq.printqueue()