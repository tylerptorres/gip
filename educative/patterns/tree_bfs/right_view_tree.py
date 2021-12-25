from TreeNode import TreeNode
from collections import deque


def execute(root):
    queue = deque([root])
    result = []

    while queue:
        sz = len(queue)

        for i in range(sz):
            current = queue.popleft()

            if i == sz - 1:
                result.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

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
