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

    def _transplant(self, deleting_node: AVLNode, replacing_node: AVLNode):

        if deleting_node.parent is None:
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node

        if replacing_node is not None:
            replacing_node.parent = deleting_node.parent

    def _balance_factor(self, node: AVLNode):
        if node is None:
            return -1
        return self._height(node.left) - self._height(node.right)

    # FIXME
    def _delete_fixup(self, fixing_node: AVLNode):

        while fixing_node is not None:
            fixing_node.height = 1 + max(self._height(fixing_node.left), self._height(fixing_node.right))

            # Case the grandparent is unbalanced
            if (self._balance_factor(fixing_node) <= -2) or (self._balance_factor(fixing_node) >= 2):
                temp = fixing_node

                y = None
                if temp.left.height > temp.right.height:
                    y = temp.left
                else:
                    y = temp.right

                z = None
                if y.left.height > y.right.height:
                    z = y.left
                elif y.left.height < y.right.height:
                    z = y.right
                else:
                    if y == temp.left:
                        z = y.left
                    else:
                        z = y.right

                if y == temp.left:
                    # Case 1
                    if z == temp.left.left:
                        self._right_rotate(temp)
                    # Case 3
                    elif z == temp.left.right:
                        self._left_rotate(y)
                        self._right_rotate(temp)

                elif y == temp.right:
                    # Case 2
                    if z == temp.right.right:
                        self._left_rotate(temp)
                    # Case 4
                    elif z == temp.right.left:
                        self._right_rotate(y)
                        self._left_rotate(temp)

            fixing_node = fixing_node.parent

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
            # grandparent is unbalanced
            if self._balance_factor(grandparent) <= -2 or self._balance_factor(grandparent) >= 2:
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
        if self.root is None:
            return

        deleting_node = binary_tree.BinaryTree._search(self, key=key, node=self.root)

        # No children or only one right child
        if deleting_node.left is None:
            self._transplant(deleting_node=deleting_node, replacing_node=deleting_node.right)

            if deleting_node.right is not None:
                self._delete_fixup(fixing_node=deleting_node.right)

        # Only one left child
        elif deleting_node.right is None:
            self._transplant(deleting_node=deleting_node, replacing_node=deleting_node.left)

            if deleting_node.left is not None:
                self._delete_fixup(fixing_node=deleting_node.left)

        # Two children
        else:
            min_node = binary_tree.BinaryTree._get_min(self, node=deleting_node.right)
            # The deleting node is not the direct parent of the minimum node.
            if min_node.parent != deleting_node:
                self._transplant(min_node, min_node.right)
                min_node.right = deleting_node.right
                min_node.right.parent = min_node

            self._transplant(deleting_node, min_node)
            min_node.left = deleting_node.left
            min_node.left.parent = min_node

            self._delete_fixup(min_node)


"""
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

    test.delete(20)
    test.delete(11)

    print(traversal.inorder_traverse(tree=test))
    #print(traversal.preorder_traverse(tree=test))
"""
