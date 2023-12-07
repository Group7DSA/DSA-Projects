class BinaryTreeNode:

    def __init__(self, key):

        self.key = key
        self.left = None
        self.right = None
        self.pre_order_number = None
        self.in_order_number = None
        self.post_order_number = None

class NumberedBinaryTree:
    def __init__(self, root=None):
        self.root = root

    def assign_numbers(self):

        self._assign_pre_order_numbers(self.root)
        self._assign_in_order_numbers(self.root)
        self._assign_post_order_numbers(self.root)
    def _assign_pre_order_numbers(self, node, count=[1]):
        if node:
            node.pre_order_number = count[0]
            count[0] += 1
            self._assign_pre_order_numbers(node.left, count)
            self._assign_pre_order_numbers(node.right, count)

    def _assign_in_order_numbers(self, node, count=[1]):
        if node:
            self._assign_in_order_numbers(node.left, count)
            node.in_order_number = count[0]
            count[0] += 1
            self._assign_in_order_numbers(node.right, count)

    def _assign_post_order_numbers(self, node, count=[1]):
        if node:
            self._assign_post_order_numbers(node.left, count)
            self._assign_post_order_numbers(node.right, count)
            node.post_order_number = count[0]
            count[0] += 1

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

numbered_tree = NumberedBinaryTree(root)

numbered_tree.assign_numbers()

print("Pre-order numbers:", [node.pre_order_number for node in [root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right]])
print("In-order numbers:", [node.in_order_number for node in [root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right]])
print("Post-order numbers:", [node.post_order_number for node in [root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right]])