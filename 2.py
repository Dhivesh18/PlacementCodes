# Task 2
# # Polynomial addition using Linked list.
# Use a linked list to represent a polynomial.
# Implement a function that adds the coefficient of same variable powers.
# A Polynomial has mainly two fields. exponent and coefficient

class Node:
    def __init__(self,c,p):            
        self.co = c                     # Data sub part
        self.ord = p
        self.ref = None
class LL:
    def __init__(self):
        self.start_node = None          # Head variable
    
    def create_1(self, x,y):            # Interface for adding data to LL (insert at start)
        new_node = Node(x,y)            # Node are entity ..create a node ..
        new_node.ref = self.start_node  # Copy address of current head/first node to new node ref
        self.start_node = new_node      # Makes newly created node as head
    
    def create_2(self,r,t):             # Interface to add data to last of LL
        new_node = Node(r,t)            # Create a node
        if self.start_node is None:     # Checking if the ll is empty
            self.start_node = new_node
            return
        n = self.start_node             # Temp variable to hold the starting address
        while n.ref is not None:        # This check if the current node is last node␣,→or not
            n = n.ref
        n.ref = new_node

    def traverse_list(self):
        if self.start_node is None:     # List is empty or not
            print("List has no element")
            return
        else: 
            n = self.start_node         # Temp variable
            b = []
            while n is not None:
                b.append((n.co,n.ord))
                n = n.ref
            print(b) 

    def addition(self, x, y):           
        a = x.start_node
        b = y.start_node
        m = max(a.ord, b.ord)
        for _ in range(m + 1):
            if a.ord == b.ord:
                temp = a.co + b.co
                self.create_2(temp, a.ord)
                a = a.ref
                b = b.ref
        self.traverse_list()
        
def inp(n):
    print("Order of the equation is ",n)
    for i in range(n+1):
        print("Enter the Coefficient of Order ",i)
        g = int(input())
        d.create_1(g,i)
    for i in range(n+1):
        print("Enter the Coefficient of Order ",i)
        k = int(input())
        f.create_1(k,i)

d = LL()
f = LL()
v = LL()
k1 = int(input("Enter the Order for first Equation"))
k2 = int(input("Enter the Order for 2nd Equation"))
if k1==k2:
    inp(k1)
elif k1>k2:
    inp(k1)
elif k2>k1:
    inp(k2)
d.traverse_list()
f.traverse_list()
v.addition(d,f)




