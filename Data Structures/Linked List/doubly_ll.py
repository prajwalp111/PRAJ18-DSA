class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is self.tail is None

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        new_node.right = self.head
        self.head.left = new_node
        self.head = new_node
        return

    def insert_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        new_node.left = self.tail
        self.tail.right = new_node
        self.tail = new_node
        return

    def insert_after(self, key, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        current = self.head
        while current is not None and current.data != key:
            current = current.right
        if current is None:
            print(f"Key {key} not found in the list.")
            return
        new_node.right = current.right
        new_node.left = current
        if current.right is not None:
            current.right.left = new_node
        current.right = new_node
        return

    def delete_beginning(self):
        if self.is_empty():
            print("List is empty. Cannot delete.")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        temp = self.head
        self.head = self.head.right
        self.head.left = None
        del temp
        return

    def delete_end(self):
        if self.is_empty():
            print("List is empty. Cannot delete.")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        temp = self.tail
        self.tail = self.tail.left
        self.tail.right = None
        del temp
        return

    def delete_node(self, key):
        if self.is_empty():
            print("List is empty. Cannot delete.")
            return
        current = self.head
        while current is not None and current.data != key:
            current = current.right
        if current is None:
            print(f"Key {key} not found in the list.")
            return
        if current == self.head:
            self.delete_beginning()
            return
        if current == self.tail:
            self.delete_end()
            return
        current.left.right = current.right
        current.right.left = current.left
        del current
        return

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.right
        return False    

    def display(self):
        if self.is_empty():
            print("List is empty.")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.right
        print("None")
        return

ll = DoublyLinkedList()


ll.insert_end(10)
ll.display()
ll.insert_end(20)
ll.display()
ll.insert_end(30)
ll.display()
ll.insert_beginning(5)
ll.display()
ll.insert_after(20, 25)
ll.display()
ll.delete_beginning()
ll.display()
ll.insert_beginning(5)
ll.display()
ll.delete_end()
ll.display()
ll.delete_node(20)
ll.display()