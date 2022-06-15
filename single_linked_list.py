class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, node: Node):
        """ insert node at the head of the list"""
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append(self, node: Node):
        """ insert node at the end of the list"""
        if self.head is None:
            self.head = node
        else:
            cursor = self.head
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = node

    def delete_head(self):
        """ deletes node at head of list """
        if self.head is None:
            return
        else:
            self.head = self.head.next

    def delete_tail(self):
        """ deletes last node """
        cursor = self.head
        previous_cursor = self.head
        while cursor.next is not None:
            previous_cursor = cursor
            cursor = cursor.next
        # print(cursor.data)
        previous_cursor.next = None
        return cursor
        # print(f"previous cursor is {previous_cursor.data}")

    def find_node(self, data):
        """ finds node corresponding to given data """
        if self.head is None:
            print("list is empty")
            return None
        cursor = self.head
        while cursor.data is not data and cursor.next is not None:
            cursor = cursor.next
        if cursor.next is None:
            return None
        else:
            return cursor

    def insert_node(self, node: Node, after_this: Node):
        """ insert new node after given node """
        node.next = after_this.next
        after_this.next = node

    def print_list(self):
        """ prints all elements of list """
        cursor = self.head
        while cursor is not None:
            print(f"[{cursor.data}]->", end="")
            cursor = cursor.next

    def size(self):
        """ prints length of the list """
        counter = 0
        cursor = self.head
        while cursor is not None:
            cursor = cursor.next
            counter = counter+1
        return counter




link_list = LinkedList()
link_list.insert_head(Node(0))
link_list.insert_head(Node(1))
link_list.insert_head(Node(2))
link_list.append(Node(3))
link_list.print_list()

print("")
link_list.insert_node(Node(5), link_list.find_node(0))
link_list.print_list()