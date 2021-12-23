from TreeNode import TreeNode

# O(N) T | O(N) S
def execute(root, current_sum=0):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return current_sum + root.val

    return max(
        execute(root.left, current_sum + root.val),
        execute(root.right, current_sum + root.val),
    )


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(execute(root))
