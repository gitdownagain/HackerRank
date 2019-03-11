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

# Each time you add to mylist, you're passing the whole list.
#     IF the list is empty (head == None),
#         insert the element as the head.
#     ELIF there is no element after the head (head.next == None),
#         put the data after the head.
#     ELSE,
#         recursively call the function with all of the elements except for the current head
# You traverse the list until you get to the point here head.next == None and you can add data.

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  
