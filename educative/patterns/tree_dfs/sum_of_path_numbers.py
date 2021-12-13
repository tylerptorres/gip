from TreeNode import TreeNode


def find_paths(root, sum=0):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 10 * sum + root.val

    return find_paths(root.left, 10 * sum + root.val) + find_paths(root.right, 10 * sum + root.val)


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(find_paths(root))
