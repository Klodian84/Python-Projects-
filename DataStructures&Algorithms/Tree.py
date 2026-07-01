class TreeNode:

    def __init__(self, data, left=None, right=None):
        # Correct the mistakes
        self.data = None
        self.left_child = None
        self.right_child = None


node1 = TreeNode("B")
node2 = TreeNode("C")
# Correct the mistake
root_node = TreeNode(node1, node2, "A")