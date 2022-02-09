# Task 5
# Write a program to rearrange the elements of a given queue of integers 
# of even length by interleaving the first half of the queue with the 
# second half of the queue.

class List:                    
    def __init__(self):
        self.items = []
        self.queue = []
        self.front = self.rear = 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        a = self.items.pop()
        return a

    def Enqueue(self, data):
        self.queue.append(data)
        self.rear += 1

    def Dequeue(self):
        if (self.front == self.rear):
            print("Queue is empty")
        else:                                # Pop the front element from list
            x = self.queue.pop(0)
            self.rear -= 1

    def Display(self):
        if (self.front == self.rear):
            print("\nQueue is Empty")
        for i in self.queue:                # use a for loop to print all the element in queue
            print(i, "<--", end='')

    def interleave(self):
        a=len(self.queue)
        h=List()
        mid = int(a/2)
        for i in range(0,mid):              # put first half elements into the queue: 6 7 8 9 10 
            h.push(q.queue[self.front])     # stack: 5(T) 4 3 2 1 
            q.Dequeue()
        for i in range(0,mid):              # enqueue back the stack elements, queue: 6 7 8 9 10 5 4 3 2 1
            z = h.pop()
            q.Enqueue(z)
        for i in range(0,mid):              # dequeue the first half elements of queue and enqueue them back 
            e = q.queue[self.front]         # queue: 5 4 3 2 1 6 7 8 9 10
            q.Dequeue()
            q.Enqueue(e)
        for i in range(0,mid):              # Again put the first half elements into the stack queue: 6 7 8 9 10 
            h.push(q.queue[self.front])     # stack: 1(T) 2 3 4 5
            q.Dequeue()
        for i in range(0,mid):              # interleave the elements of queue and stack. 
            w = h.pop()
            q.Enqueue(w)
            e = q.queue[self.front]
            q.Dequeue()
            q.Enqueue(e)                    # Queue: 1 6 2 7 3 8 4 9 5 10
        q.Display()

q = List()
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    q.Enqueue(i)
q.interleave()
