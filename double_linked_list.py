class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, node: Node):
        """ insert node at the head of the list"""
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node


    def append(self, node: Node):
        """ insert node at the end of the list"""
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            # cursor = self.head
            # while cursor.next is not None:
            #     cursor = cursor.next
            # cursor.next = node

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

    def insert_node_after(self, node: Node, after_this: Node):
        """ insert new node after given node """
        node.next = after_this.next
        after_this.next.prev = node
        after_this.next = node
        node.prev = after_this


    def insert_node_before(self, node: Node, before_this: Node):
        node.next = before_this
        node.prev = before_this.prev
        node.prev.next = node
        before_this.prev = node



    def print_list_forward(self):
        """ prints all elements of list """
        cursor = self.head
        while cursor is not None:
            print(f"[{cursor.data}]->", end="")
            cursor = cursor.next

    def print_list_reverse(self):
        cursor = self.tail
        # handle empty list
        if cursor is None:
            return
        # handle list with 1 element
        if cursor is self.head:
            print(f"<-[{cursor.data}]",end="")
            return
        while cursor is not None:
            print(f"<-[{cursor.data}]",end="")
            cursor = cursor.prev

    def size(self):
        """ prints length of the list """
        counter = 0
        cursor = self.head
        while cursor is not None:
            cursor = cursor.next
            counter = counter + 1
        return counter

