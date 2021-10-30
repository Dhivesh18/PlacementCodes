class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(l):
    p=""
    while l.next is not None:        
        p+=str(l.data)
        l = l.next
    p+=str(l.data)
    print(int(p,2))

def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)           
    if head is None:     
        head = new_node
        return head
    n = head                       
    while n.next is not None:        
        n = n.next
    n.next = new_node
    return head 

llist_count = int(input())
llist = SinglyLinkedList()
for _ in range(llist_count):
    llist_item = int(input())
    llist_head = insertNodeAtTail(llist.head, llist_item)
    llist.head = llist_head
print_singly_linked_list(llist.head)

