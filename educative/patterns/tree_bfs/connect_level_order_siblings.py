from TreeNode import TreeNode
from collections import deque

# O(N)  T & S
def execute(root):
    queue = deque([root])

    while queue:
        queue_size = len(queue)

        for i in range(queue_size):
            current = queue.popleft()

            if i >= queue_size - 1:
                current.next = None
            else:
                current.next = queue[0]

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    execute(root)
