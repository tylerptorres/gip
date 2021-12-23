from TreeNode import TreeNode


def execute(root):
    # terminal cases
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return min(execute(root.left), execute(root.right)) + 1

    # fail : root is none, return 0
    # success : root is leaf, return 1


if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)

    print(execute(root))
