class Node:
    def __init__(self,c):            
        self.co = c                     # Data sub part
        self.ref = None
class LL:
    def __init__(self):
        self.start_node = None          # Head variable
    
    def create_1(self, x):            # Interface for adding data to LL (insert at start)
        new_node = Node(x)            # Node are entity ..create a node ..
        new_node.ref = self.start_node  # Copy address of current head/first node to new node ref
        self.start_node = new_node      # Makes newly created node as head
    
    def create_2(self,r):             # Interface to add data to last of LL
        new_node = Node(r)            # Create a node
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
                b.append(n.co)
                n = n.ref
            print(b) 

    def delete(self,x,u,n):
        a=x.start_node
        for _ in range(n+1):
            print(a.co)
            if a.co != u:
                self.create_2(a.co)
            a=a.ref
        self.traverse_list()
           
def inp(n):
    for _ in range(n+1):
        g = int(input("Enter a number"))
        d.create_1(g)

d = LL()
f=LL()
k = int(input("Enter the number size"))
inp(k)
d.traverse_list()
z=int(input("Enter a number to delete from node"))
f.delete(d,z,k)
