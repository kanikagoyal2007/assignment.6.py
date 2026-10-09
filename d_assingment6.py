from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)

        return root

    def level_order(self, root):
        if root is None:
            print("Tree is empty")
            return

        queue = deque([root])
        level = 0

        while queue:
            size = len(queue)
            print(f"Level {level}:", end=" ")

            for _ in range(size):
                node = queue.popleft()
                print(node.data, end=" ")

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            print()
            level += 1

    def height(self, root):
        if root is None:
            return 0

        return 1 + max(
            self.height(root.left),
            self.height(root.right)
        )

    def leaf_nodes(self, root):
        if root is None:
            return

        if root.left is None and root.right is None:
            print(root.data, end=" ")
            return

        self.leaf_nodes(root.left)
        self.leaf_nodes(root.right)

    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append(root.data)
            self.inorder(root.right, result)

    def build_balanced(self, values):
        if not values:
            return None

        mid = len(values) // 2
        root = Node(values[mid])

        root.left = self.build_balanced(values[:mid])
        root.right = self.build_balanced(values[mid + 1:])

        return root


# Main program
tree = BST()

n = int(input("Enter number of employee IDs: "))
print("Enter employee IDs:")

for i in range(n):
    employee_id = int(input())
    tree.insert(employee_id)

print("\nOriginal BST (Level-wise):")
tree.level_order(tree.root)

print("\nHeight of Original BST:",
      tree.height(tree.root))

print("Leaf Nodes of Original BST:", end=" ")
tree.leaf_nodes(tree.root)
print()

# Create a new balanced BST
values = []
tree.inorder(tree.root, values)

new_tree = BST()
new_tree.root = new_tree.build_balanced(values)

print("\nNew Balanced BST (Level-wise):")
tree.level_order(new_tree.root)

print("\nHeight of New BST:",
      tree.height(new_tree.root))

print("Leaf Nodes of New BST:", end=" ")
tree.leaf_nodes(new_tree.root)
print()