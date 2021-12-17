class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def execute(head, p, q):
    sz = q - p
    prev = None
    current = head

    while p - 1 > 0:
        prev = head
        head = head.next
        p -= 1

    # reverse the sublist
    prev_, head_ = reverse_sub_list(prev, head, sz)

    if prev is not None:
        prev.next = prev_
    else:
        current = prev_

    head.next = head_

    return current


def reverse_sub_list(prev, head, sz):

    while sz > -1:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

        sz -= 1

    return prev, head

    """
    1 <- 2 <- 3 <- 4 - 5 -> Null
         p      

    <- 1 <- 2 <- 3 -> Null
 p
    h 

    if 
        the previous node is not none, then point that to the q node.next 
    else
        the head element is the node that will be the tail of the list 

    
    
         

    prev = None
    p -= 1

    reverse from p -> q
    p.next = q.next
    p.prev.next = q

    - Save reference to prev before p
    - reverse list from p until q
        - save reference to new head at q
        - save reference to new_head.next
    - old_prev.next = new_head
    - 


    """


if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    node = execute(head, 1, 2)

    while node is not None:
        print(node.value)
        node = node.next
