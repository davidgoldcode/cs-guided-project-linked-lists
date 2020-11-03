class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.value}'


def find_length(head):
    counter = 0
    current = head

    while current is not None:
        counter += 1
        current = current.next

    return current


def find_middle(head):
    # figure out length of the linked list
    len = find_length(head)
    # figure out the midpoint
    midpoint = len // 2
    # traverse from the head to the middle
    current = head

    while midpoint != 0:
        current = current.next
        midpoint -= 1
    return current.value


root = Node(3)
root.next = Node(4)
root.next.next = Node(5)
root.next.next.next = Node(6)
root.next.next.next.next = Node(7)

root.find_middle()  # should return the Node with value 5
