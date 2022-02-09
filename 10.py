# # Task 10
# Implement a class for BST with the interfaces for adding elements,
# deleting elements, traversals(3 DFS ),search for the minimum and
# maximum, creating a bst from a given array and size of the bst.
 
class Binary_Search_Tree:

    def __init__(self, data):
        self.data = data
        self.Left_child = None
        self.Right_child = None

    def Add_Node(self, data):
        if data == self.data:
            return 
        if data < self.data:
            if self.Left_child:
                self.Left_child.Add_Node(data)
            else:
                self.Left_child = Binary_Search_Tree(data)
        else:
            if self.Right_child:
                self.Right_child.Add_Node(data)
            else:
                self.Right_child = Binary_Search_Tree(data)

    def In_Order_Traversal(self):
        elements = []
        if self.Left_child:
            elements += self.Left_child.In_Order_Traversal()
        elements.append(self.data)
        if self.Right_child:
            elements += self.Right_child.In_Order_Traversal()
        return elements

    def Post_Order_Traversal(self):
        elements = []
        if self.Left_child:
            elements += self.Left_child.Post_Order_Traversal()
        if self.Right_child:
            elements += self.Right_child.Post_Order_Traversal()
        elements.append(self.data)
        return elements

    def Pre_Order_Traversal(self):
        elements = [self.data]
        if self.Left_child:
            elements += self.Left_child.Pre_Order_Traversal()
        if self.Right_child:
            elements += self.Right_child.Pre_Order_Traversal()
        return elements
        
    def Find_Maximum_Node(self):
        if self.Right_child is None:
            return self.data
        return self.Right_child.Find_Maximum_Node()

    def Find_Minimum_Node(self):
        if self.Left_child is None:
            return self.data
        return self.Left_child.Find_Minimum_Node()

def Build_Tree(elements):
    root = Binary_Search_Tree(elements[0])
    for i in range(1,len(elements)):
        root.Add_Node(elements[i])
    return root

root=Build_Tree([10,99,1,55,26])
print(root.Find_Maximum_Node())
print(root.Find_Minimum_Node())
print(root.In_Order_Traversal())
print(root.Post_Order_Traversal())
print(root.Pre_Order_Traversal())
