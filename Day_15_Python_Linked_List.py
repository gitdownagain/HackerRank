class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        if head == None:
            head = Node(data)       # insert the data into the Node class 
        elif (head.next == None):   # if Node.next is None (nothing attached)
            head.next = Node(data)  # insert data here if there are other elements
        else:
            self.insert(head.next, data)
        return head

# The function gets called with the whole linked list. 
#     If the list is empty,
#         insert the element as the head.
#     Otherwise if there is no element after the head,
#         put the data after the head.
#     Otherwise,
#         call the function with all of the elements except for the current head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  
