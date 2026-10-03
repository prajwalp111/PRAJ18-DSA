from copy import error


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return 

    def insert_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node 
        return

    def insert_after(self, key, data):
        new_node = Node(data)
        current_node = self.head
        if self.is_empty():
            print("List is empty. Inserting at the beginning.")
            self.head = new_node
            return
        while current_node is not None and current_node.data != key:
            current_node = current_node.next
        if current_node is None:
            error("Key not found in the list.")
        new_node.next = current_node.next
        current_node.next = new_node
        return

    def delete_begining(self):
        if self.is_empty():
            error("List is empty. Cannot delete from beginning.")
        temp = self.head
        self.head = self.head.next
        del temp

    def delete_end(self):
        if self.is_empty():
            error("List is empty. Cannot delete from end.")
        if self.head.next is None:
            temp = self.head
            self.head = None
            del temp
            return
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        temp = current_node.next
        current_node.next = None
        del temp
        return

    def delete_key(self, key):
        if self.is_empty():
            error("List is empty. Cannot delete key.")
        if self.head.data == key:
            temp = self.head
            self.head = None
            del temp
            return
        current_node = self.head
        while current_node.next is not None and current_node.next.data != key:
            current_node = current_node.next
        if current_node.next is None:
            error("Key not found in the list.")
        temp = current_node.next
        current_node.next = current_node.next.next
        del temp
        return

    def search(self, key):
        current_node = self.head
        while current_node is not None:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

    def display(self):
        if self.is_empty():
            print("list is empty.")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
        return
    

ll = LinkedList()

ll.insert_end(10)
ll.display()
ll.insert_end(20)
ll.display()
ll.insert_end(30)
ll.display()
ll.insert_begining(5)
ll.display()
ll.insert_after(20, 25)
ll.display()
ll.delete_begining()
ll.display()
ll.insert_begining(5)
ll.display()
ll.delete_end()
ll.display()
ll.delete_key(20)
ll.display()