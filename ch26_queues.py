from ch24_linked_lists import Node


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        # A linear time function
        node = Node(cargo)
        if self.head is None:
            # If list is empty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            # Append the new node
            last.next = node
        self.length += 1

    def remove(self):
        # A constant time function
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo


class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        # A constant time function
        node = Node(cargo)
        if self.length == 0:
            # If the list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # Find the last node
            last = self.last
            # Append the new node
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        # A constant time function
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo

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

class PriorityQueue:
    """
    Similar to the other queues, although the semantic difference is
    that the item removed and returned is the one with the highest priority.
    What the priority is and how they are compared are not specified in the
    Priority Queue implementation.
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        """ Insert an item at the end of the list """
        self.items.append(item)

    def remove(self):
        """ Remove the largest item """
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item

# The Golfer class]
class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "{0:16}: {1}".format(self.name, self.score)

    def __gt__(self, other):
        return self.score < other.score  # Less is more

class PriorityQueueLinkedList:
    """
    A priority queue linked list where:
    The list is ordered from greatest value to least
    Ensure ordered list when inserting new items
    """
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
