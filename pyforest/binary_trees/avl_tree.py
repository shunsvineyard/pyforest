# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""AVL Tree."""

from dataclasses import dataclass
from typing import Any, Generic, Optional

from pyforest.binary_trees import binary_tree


@dataclass
class AVLNode(binary_tree.Node, Generic[binary_tree.KeyType]):
    left: Optional["AVLNode"] = None
    right: Optional["AVLNode"] = None
    parent: Optional["AVLNode"] = None
    height: int = 0


class AVLTree(binary_tree.BinaryTree):
    """AVL Tree."""

    def __init__(self, key: binary_tree.KeyType = None, data: Any = None):
        binary_tree.BinaryTree.__init__(self)
        if key and data:
            self.root = AVLNode(key=key, data=data)

    def _height(self, node: Optional[AVLNode]) -> int:
        """Real implementation of getting the height of a given node.

        Parameters
        ----------
        node: Node
            The root of the tree.

        Retruns
        -------
        int
            Return the height of the given node.
        """
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 0

        return max(self._height(node.left), self._height(node.right)) + 1

    def _left_rotate(self, node: AVLNode):
        temp = node.right
        node.right = temp.left
        if temp.left is not None:
            temp.left.parent = node
        temp.parent = node.parent
        if node.parent is None:  # node is the root
            self.root = temp
        elif node == node.parent.left:  # node is the left child
            node.parent.left = temp
        else:  # node is the right child
            node.parent.right = temp

        temp.left = node
        node.parent = temp

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        temp.height = 1 + max(self._height(temp.left), self._height(temp.right))

    def _right_rotate(self, node: AVLNode):
        temp = node.left
        node.left = temp.right
        if temp.right is not None:
            temp.right.parent = node
        temp.parent = node.parent
        if node.parent is None:  # node is the root
            self.root = temp
        elif node == node.parent.right:  # node is the left child
            node.parent.right = temp
        else:  # node is the right child
            node.parent.left = temp

        temp.right = node
        node.parent = temp

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        temp.height = 1 + max(self._height(temp.left), self._height(temp.right))


    def _translate(self, deleting_node: AVLNode, replacing_node: AVLNode):
        pass

    def _balance_factor(self, node: AVLNode):
        if node is None:
            return -1
        return self._height(node.left) - self._height(node.right)

    # Overriding abstract method
    def search(self, key: binary_tree.KeyType):
        pass

    # Overriding abstract method
    def insert(self, key: binary_tree.KeyType, data: Any):

        temp = self.root
        parent: Optional[AVLNode] = None
        while temp is not None:
            parent = temp
            if key == temp.key:
                raise ValueError(f"Duplicate key {key}")
            elif key < temp.key:
                temp = temp.left
            else:
                temp = temp.right

        node = AVLNode(key=key, data=data, parent=parent)

        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        temp = node
        while parent is not None:
            parent.height = 1 + max(self._height(parent.left), self._height(parent.right))

            grandparent = parent.parent
            if self._balance_factor(grandparent) <= -2 or self._balance_factor(grandparent) >= 2:  # grandparent is unbalanced
                if parent == grandparent.left:
                    # Case 1
                    if temp == grandparent.left.left:
                        self._right_rotate(grandparent)
                    # Case 3
                    elif temp == grandparent.left.right:
                        self._left_rotate(parent)
                        self._right_rotate(grandparent)
                elif parent == grandparent.right:
                    # Case 2
                    if temp == grandparent.right.right:
                        self._left_rotate(grandparent)
                    # Case 4
                    elif temp == grandparent.right.left:
                        self._right_rotate(parent)
                        self._left_rotate(grandparent)
                break
            parent = parent.parent
            temp = temp.parent

    # Overriding abstract method
    def delete(self, key: binary_tree.KeyType):
        pass

from pyforest.binary_trees import traversal

if __name__ == "__main__":
    test = AVLTree()
    test.insert(23, "23")
    test.insert(4, "4")
    test.insert(30, "30")
    test.insert(11, "11")
    test.insert(7, "7")
    test.insert(34, "34")
    test.insert(20, "20")
    test.insert(24, "24")
    test.insert(22, "22")
    test.insert(15, "15")
    test.insert(1, "1")

    print(test.root.height)

    print(traversal.inorder_traverse(tree=test))
