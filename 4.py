# Task 4
# Write a program to check if a queue can be sorted into another queue using
# a stack (using push/pop, enqueue/dequeue operations only.) 

import copy

class List:
    def __init__(self):
        self.stack = []
        self.queue = []
        self.front = self.rear = 0
         
    def push(self, d):
        self.stack.append(d)

    def pop(self):
        a = self.stack.pop()
        return a

    def Enqueue(self, d):
        self.queue.append(d)
        self.rear += 1

    def Dequeue(self):
        x = self.queue.pop(0)
        self.rear -= 1
        return x

    def Display(self):
        for i in self.queue:            # use a for loop to print all the element in queue
            print(i, "<--", end='')
        print("\r")
    
    def size(self):
        c = len(self.stack)
        return c
    
    def qsort(self):  
        sorted_queue = List()
        while self.rear > 0:
            if self.queue[self.front]>self.queue[self.front-1]:
                i = self.Dequeue()
                self.push(i)
            elif self.queue[self.front]<self.queue[self.front-1]:
                i = self.Dequeue()
                sorted_queue.Enqueue(i)
            else:
                i = self.Dequeue()
                sorted_queue.Enqueue(i)              
        l = self.size()
        for i in range(0,l):
            u = self.pop()
            sorted_queue.Enqueue(u)
        return sorted_queue.queue

    def check(self,b,t):
        if  b == t:
            print("Can be sorted")
        else:
            print("Cannot be sorted")

a = List()
arr = [5,1,2,6,3]
temp = copy.deepcopy(arr)
for i in arr:
    a.Enqueue(i)
temp.sort()
a.Display()
r = a.qsort()
a.check(r,temp)


