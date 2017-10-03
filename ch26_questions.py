from ch24_linked_lists import Node


# Question 1:
class ImprovedQueuePythonList:
    """ An implementation for Queue ADT using a python list """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self, item):
        if self.is_empty():
            return None
        return self.items.pop(0)


# Question 2
class PriorityQueueLinkedList:
    """
    A priority queue linked list where:
    The list is ordered from greatest value to least
    Ensure ordered list when inserting new items
    """

    """ Insert new cargo and keep the list order """
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.is_empty():
            self.head = self.last = node
        elif self.head.cargo < cargo:
            # Make the new node the new head (greatest node)
            node.next = self.head
            self.head = node
        elif self.last.cargo >= cargo:
            # Check the last node to not waste time traversing the whole lnked list
            self.last.next = node
        else:
            # set next node to travese list and compare
            previous_node = None
            next_node = self.head
            while next_node.cargo >= cargo:
                # Keep track of the node right before the node with the lower cargo
                previous_node = next_node
                next_node = next_node.next
                if next_node == None:
                    next_node = None
            previous_node.next = node
            node.next = next_node
        self.length += 1

    def remove(self):
        """ Remove the largest item """
        # Assumes a sorted list
        if self.is_empty():
            return None
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo
