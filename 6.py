# Task 6
# Write a program to check if a given linked list is a palindrome.

class Stack:
    def __init__(self):                 
        self.stack = []
    
    def push(self,data):                # Inserting Elements to stack
        self.stack.append(data)
    
    def pop(self):                      # Delete Element from stack
        a=self.stack.pop()
        return a

class Node:
    def __init__(self,e):                
        self.e = e                       # Data sub part
        self.ref = None                     

class LL:
    def __init__(self):
        self.start_node = None            # Head variable     
    
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

    def palindrome(self,a):
        st = a.start_node
        t = st
        s = Stack()
        while st!= None:                # 1,4,3,2,1 - inserting from start.
            s.push(st.e)        
            st = st.ref                 
        a.traverse_list()               # LL=1,4,3,2,1 and stack=1,4,3,2,1
        # print("Stack",s.stack)
        while t!= None:
            p = s.pop()                 # p=1(top)
            if t.e == p:                
                r = True                # Palindrome
            else:
                r = False               # Not Palindrome
                break
            t = t.ref 
        return r

x = LL()
k = LL()
n = [1,2,3,2,4,1]
for i in n:
    x.create(i)
print(k.palindrome(x))

        
    
