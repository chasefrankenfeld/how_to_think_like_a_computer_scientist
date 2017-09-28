class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=" ")


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_backward(self):
        print("[", end= " ")
        if self.head is not None:
            self.head.print_backward()
        print("]")

    def add_first(self, cargo):
        node = Node(cargo)
        nl
        self.head = node
        self.length += 1


# Version 1 using print
def print_list(node):
    print("[", end = "")
    while node is not None:
        print(node, end="")
        node = node.next
        if node is not None:
            print(", ", end="")
    print("]")

# Version 2 - using a string
# def print_list(node):
#     s = "["
#     while node:
#         s += str(node)
#         node = node.next
#         if node:
#             s += ", "
#     s += "]"
#     print(s)

def print_backward(list):
    if list is None:
        return
    print_backward(list.next)
    print(list, end=" ")

def remove_second(list):
    if list is None: return
    first = list
    try:
        second = list.next
        # Make the first node refer to the third
        first.next = second.next
        # Separate the second node from the rest of the list
        second.next = None
        return second
    except AttributeError:
        if list:
            return "Is a singleton"
        return "Is an empty list"

def print_backward_nicely(list):
    print("[", end=" ")
    print_backward(list)
    print("]")
