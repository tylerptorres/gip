from TreeNode import TreeNode
from collections import deque


# O(N) T & S
def execute(root):

    result = []
    queue = deque([root])

    while queue:
        sz = len(queue)
        level = deque()

        for _ in range(sz):
            current = queue.popleft()
            # appending to the level queue, our level
            if len(result) % 2 == 0:
                level.append(current.val)
            else:
                level.appendleft(current.val)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        result.append(list(level))  # O(N)

    return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(execute(root))
