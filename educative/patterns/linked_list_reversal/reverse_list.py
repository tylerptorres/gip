from reverse_sublist import Node


def execute(head):
    if head is None:
        return head

    prev = None
    while head is not None:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev


if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    node = execute(head)

    while node is not None:
        print(node.value)
        node = node.next
