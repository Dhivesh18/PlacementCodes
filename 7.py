# Task 7
# Write a program to reverse a linked list.

class Stack:
    def __init__(self):                  
        self.stack = []
    
    def push(self,data):                 # Inserting Elements to stack
        self.stack.append(data)
    
    def pop(self):                       # Delete Element from stack
        a = self.stack.pop()
        return a

class Node:                              
    def __init__(self,e):                 # Data sub part
        self.e = e
        self.ref = None

class LL:
    def __init__(self):                   
        self.start_node = None

    def create(self,d):             # Interface to add data to last of LL
        new_node = Node(d)            # Create a node
        if self.start_node is None:     # Checking if the ll is empty
            self.start_node = new_node
            return
        n = self.start_node             # Temp variable to hold the starting address
        while n.ref is not None:        # This check if the current node is last node␣,→or not
            n = n.ref
        n.ref = new_node
        
    def traverse_list(self):
        if self.start_node is None:       # List is empty or not
            print("List has no element")
            return
        else:
            n = self.start_node           # Temp variable
            b = []
            while n is not None:
                b.append(n.e)
                n = n.ref
            print(b)

    def reverse(self,a):
        st = a.start_node
        t = st
        s = Stack()
        q = Stack()
        while st!= None:                # 5,4,3,2,1 - inserting from start.
            s.push(st.e)        
            st = st.ref                 
        a.traverse_list()               # LL = 5,4,3,2,1 and s.stack = 5,4,3,2,1
        while t!= None:                 # Reverse 
            p = s.pop()                 
            q.push(p)
            t = t.ref                   
        print(q.stack)                  # q.stack = 1,2,3,4,5
           
l = LL()
r = LL()
u = [1,2,3]
for i in u:
    l.create(i)
r.reverse(l)

