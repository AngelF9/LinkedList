# Define a Node class: 
# this class will represent each element in the linked list.
# It will contain the data and the reference to the next node.
class Node: 
    # a node in a linked list, not the edges
    def __init__(self, data):
        self.data = data    # the data stored in this node
        self.next = None    # the next node in the list, initialized to None


# Define a LinkedList class:
# This clas will manage the nodes, keeping track of the head of the list and providing methods to manipulate the list
class LinkList:
    # a singly linked list
    def __init__(self) -> None:
        self.head = None # the first node in the list

    def append_list(self, data):
        """append a new node witht the provided data to the end of the list."""
        new_node = Node(data) # create a new node witht the given data
        if not self.head:
            # if the list is empty, set the new node as the first node
            self.head = new_node
            return
        
        # if the list is not empty, find the last node
        last_node = self.head 
        while last_node.next != None:
            # traverse the list until the last node is found, Until None...
            last_node = last_node.next
        # set the next of the last node to the new node
        last_node.next = new_node

    def display(self):
        """Display the contents of the list"""
        current_node = self.head # current_node represent an indivdual Node (1). 
        # to get access to this node we use .data or to view next node we use .next

        while current_node:
            # traverse the list and print the data of each node
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        # print none at the end to indicate the end of the list
        print("None")

    def delete(self, key):
        """Delete the first occurrence of a node with the given data"""
        current_node = self.head
        if current_node and current_node.data == key:   # if not empty and ...
            self.head = current_node.next               # set head to the next node
            current_node = None  # remove the current node 'None'
            return
        prev = None
        while current_node and current_node.data != key:
            prev = current_node  # update the previous node
            current_node = current_node.next  # move to the next node
        if current_node is None:
            return 
        # set the next of the previous node to skip the node which is to be deleted
        prev.next = current_node.next
        current_node = None

    def reverse_list(self):
        # prev is set to None because the new tail of the list (which was the head) will point to None.
        prev = None 
        current_node = self.head

        while current_node:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next
        self.head = prev

    def mergeTwoLists(self, list1, list2):
        dummy = Node(None)  # Create a dummy node for simplified handling
        tail = dummy

        while list1.head and list2.head:  # Access the 'head' of each list
            if list1.head.data < list2.head.data:
                tail.next = list1.head
                list1.head = list1.head.next  # Advance List1's head
            else:
                tail.next = list2.head
                list2.head = list2.head.next  # Advance List2's head
            tail = tail.next

        # Append any remaining nodes from either list
        tail.next = list1.head or list2.head

        return dummy.next  # Return the head of the merged list


# testing a linked list append and display
def main():
    # ... (Your existing corrected code)

    # Create linked lists
    List1 = LinkList()
    List1.append_list(1)
    List1.append_list(3)
    List1.append_list(5)

    List2 = LinkList()
    List2.append_list(2)
    List2.append_list(4)
    List2.append_list(6)

    # Print the original lists
    List1.display()  # Output: 1 -> 3 -> 5 -> None
    List2.display()  # Output: 2 -> 4 -> 6 -> None

    # Merge the lists
    List_merge = LinkList()
    merged = List_merge.mergeTwoLists(List1, List2)

    List_merge.head = merged

    # Display the merged list
    List_merge.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

    List_merge.reverse_list()
    List_merge.display()  # Output: 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> None


main()