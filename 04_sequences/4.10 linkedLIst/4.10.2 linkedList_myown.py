# create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        else:
            new_node.next = self.head 
            self.head = new_node

    # Method to add a node at any idnex 
    # Indexing starts from 0 
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head 
        position = 0 
        
        if index == position:
            self.insertAtBegin(new_node)

        else:
            while (current_node != None and position+1 < index):
                position += 1
                current_node = current_node.next 

            if current_node != None:
                new_node.next = current_node.next 
                current_node.next = new_node

            else:
                print("index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 

        current_node = self.head
        while current_node.next:
            current_node = current_node.next 

        current_node.next = new_node

    def updateNode(self, val, index):
        
        if not self.head:
            print("the Linklist is empty")

        else:
            position = 0
            current_node = self.head 

            while current_node and position != index:
                position += 1
                current_node = current_node.next 

            if current_node:
                current_node.data = val 
            else:
                print("Index not present")

    def remove_first_node(self):
        
        if self.head:
            current_node = self.head

        self.head = self.head.next

    def remove_last_node(self):

        if self.head:
            current_node = self.head 

            while current_node.next and current_node.next.next:
                current_node = current_node.next 

            current_node.next = None 

    def remove_at_index(self, index):

        if self.head:
            current_node = self.head 
            position = 0

            if position == index:
                self.remove_first_node()

            while current_node and position+1 != index:
                position += 1
                current_node = current_node.next 

            if current_node:
                current_node.next = current_node.next.next
            else:
                print("index not present")

    def remove_node(self, data):
        current_node = self.head 

        while (current_node and current_node.next.data != data):
            current_node = current_node.next 

        if not current_node:
            return 
        
        else:
            current_node.next = current_node.next.next 


    def sizeOfLL(self):

        if not self.head:
            return 0 
        
        else:
            current_node = self.head
            position = 0 
            while current_node: 
                position += 1
                current_node = current_node.next 

            return position
        
    def printLL(self):
        current_node = self.head 
        while (current_node):
            print(current_node.data)
            current_node = current_node.next


def main():
    llist = LinkedList()
 
    # add nodes to the linked list
    llist.insertAtEnd('a')
    llist.insertAtEnd('b')
    llist.insertAtBegin('c')
    llist.insertAtEnd('d')
    llist.insertAtIndex('g', 2)
    llist.insertAtIndex('h', 5)
    llist.remove_at_index(5)
 
    # print the linked list
    print("Node Data")
    llist.printLL()

if __name__ == "__main__":
    main()
