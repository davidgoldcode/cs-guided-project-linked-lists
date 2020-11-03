"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.

Example:

The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.

```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
```

*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""


class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None


def delete_node(node_to_delete):
    # Your code here
    # check if `node to delete` is the last node in the LL
    # if it is, set node to delete to None
    if node_to_delete.next is None:
        # traverse to node right before the tail so that we can change next ref
        # c hange its next ref
        # this isnt poss because we dont have access to the head
        raise Exception('This function cant delete the tail')
    else:
        # change our 'node to delete' to be its next value
        node_to_delete.value = node_to_delete.next.value
    # change our node to delete next to refer to its nexts next
        node_to_delete.next = node_to_delete.next.next


x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
