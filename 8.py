# # Task 8
# Write a program to calculate the minimal cost of connecting n ropes. You
# are given n ropes of different length, connect them into single rope with
# minimum cost. You can assume the cost of connecting two ropes is same
# as the sum of their lengths. Use heap for this problem

class heap:
    def __init__(self):
        self.a = []

    def create(self, d):
            self.a.append(d)
            self.minheap(self.a)

    def parent(self, i):
        return int((i - 1) / 2)

    def mak(self, k):
        self.a = []
        for i in k:
            self.create(i)

    def minheap(self, c):
        i = len(c) - 1
        parent = self.parent(i)
        while parent is not None:
            if c[i] >= c[parent]:
                return
            t = c[parent]
            c[parent] = c[i]
            c[i] = t
            i = parent
            parent = self.parent(i)          

    def minsum(self):
        con = 0
        tot = 0
        while len(self.a) > 1:
            for _ in range(2):
                z = self.a.pop(0)
                self.mak(self.a)
                con += z
            self.a.append(con)
            self.mak(self.a)
            tot += con
            con = 0
        print("min: ", tot)
        
h = heap()
v = [8, 4, 2, 5]
for j in v:
    h.create(j)
print(h.a)
h.minsum()
