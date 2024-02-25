class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def append_list(self, data):
        new_node = Node(data)
        if not self.head: # if ther is no head (empty list)
            self.head = new_node
            return
        
        # if list is not empty look for last node and then enter new data
        last_node = self.head
        while last_node.next != None: # This line checks if the next attribute of an object referred to by last_node is not None or does not evaluate to False.
            last_node = last_node.next
        # set the next of the last node to the new node
        last_node.next = new_node

    def display(self):
        curr = self.head
        while curr: # when 'curr = None' ----> it is also False
            print(curr.data, end=" ---> ")
            curr = curr.next
        print("None")

    def delete(self, key):
        curr = self.head
        # if the node to delete is the first element  
        if curr and curr.data == key:
            self.head = curr.next # set the head to the following element 
            curr = None # remove the node 
            return      
        
        # if the node to delete is somewhere other then the first element 
        # we should keep track of the previous element 
        prev = None
        while curr and curr.next != key: # loop while we have not reached the end of the list and we have found the node to delete
            prev = curr # update the previous node
            curr = curr.next # move to the next node
            # loop will stop when node to delete has been found or we have reach the end 'None'
        if curr is None:
            return 
        #                                                                  /----------------\
        # we have found a node to delete                        prev.next  curr        curr.next
        prev.next = curr.next # we are skipping over curr   1 ------------x (4) ----------> 3
        curr = None # we can delete the 'node to be deleted' now

    def reverse_list(self):
        prev = None
        curr = self.head

        while curr: # while curr does not equal to None
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


node = LinkList()
node.append_list(9)
node.append_list(12)
node.append_list(5)
node.append_list(4)
node.display()
node.reverse_list()
node.display()
print("END")