
from TreeNode import TreeNode


def find_path(root, sum=0, current_path=[]):
    if root is None:
        return 0, []

    if root.left is None and root.right is None:
        return sum + root.val, current_path + [root.val]

    left_sum, left_path = find_path(root.left, sum + root.val, current_path + [root.val])
    right_sum, right_path = find_path(root.right, sum + root.val, current_path + [root.val])

    return (left_sum, left_path) if left_sum >= right_sum else (right_sum, right_path)


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(find_path(root)[1])
