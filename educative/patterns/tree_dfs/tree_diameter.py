class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:
    def __init__(self):
        self.treeDiameter = 0

    # O(N) T | O(N) S
    def find_diameter(self, root):
        self.treeDiameter = self.find_tree_diameter(root)
        return self.treeDiameter[0]

    def find_tree_diameter(self, root):
        # (max_tree_diameter, max_depth_from_current)
        if root is None:
            return 0, 0

        left_diameter, max_depth_from_left = self.find_tree_diameter(root.left)
        right_diameter, max_depth_from_right = self.find_tree_diameter(root.right)

        current_diameter = max_depth_from_left + max_depth_from_right + 1
        current_max_depth = 1 + max(max_depth_from_left, max_depth_from_right)

        return max(current_diameter, left_diameter, right_diameter), current_max_depth


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()
