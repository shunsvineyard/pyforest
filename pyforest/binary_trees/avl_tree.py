# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""AVL Tree."""

from dataclasses import dataclass
from typing import Any, Generic, Optional

from pyforest import tree_exceptions

from pyforest.binary_trees import binary_tree


@dataclass
class AVLNode(binary_tree.Node, Generic[binary_tree.KeyType]):
    """AVL Tree node definition."""

    left: Optional["AVLNode"] = None
    right: Optional["AVLNode"] = None
    parent: Optional["AVLNode"] = None
    height: int = 0


class AVLTree(binary_tree.BinaryTree):
    """AVL Tree."""

    def __init__(self, key: binary_tree.KeyType = None, data: Any = None):
        binary_tree.BinaryTree.__init__(self)
        if key and data:
            self.root: AVLNode = AVLNode(key=key, data=data)

    # Override
    def search(self, key: binary_tree.KeyType) -> AVLNode:
        """See :func:`~binary_tree.BinaryTree.search`."""
        current = self.root

        while current:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:  # key > current.key:
                current = current.right
        raise tree_exceptions.KeyNotFoundError(key=key)

    # Override
    def insert(self, key: binary_tree.KeyType, data: Any):
        """See :func:`~binary_tree.BinaryTree.insert`."""
        temp: Optional[AVLNode] = self.root
        parent: Optional[AVLNode] = None
        while temp:
            parent = temp
            if key == temp.key:
                raise tree_exceptions.DuplicateKeyError(key=key)
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
        while parent:
            parent.height = 1 + max(self.get_height(parent.left),
                                    self.get_height(parent.right))

            grandparent = parent.parent
            # grandparent is unbalanced
            if self._balance_factor(grandparent) <= -2 or \
               self._balance_factor(grandparent) >= 2:
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

    # Override
    def delete(self, key: binary_tree.KeyType):
        """See :func:`~binary_tree.BinaryTree.delete`."""
        deleting_node: AVLNode = self.search(key=key)

        # No children or only one right child
        if deleting_node.left is None:
            self._transplant(deleting_node=deleting_node, replacing_node=deleting_node.right)

            if deleting_node.right:
                self._delete_fixup(fixing_node=deleting_node.right)

        # Only one left child
        elif deleting_node.right is None:
            self._transplant(deleting_node=deleting_node, replacing_node=deleting_node.left)

            if deleting_node.left:
                self._delete_fixup(fixing_node=deleting_node.left)

        # Two children
        else:
            min_node = self.get_min(node=deleting_node.right)
            # The deleting node is not the direct parent of the minimum node.
            if min_node.parent != deleting_node:
                self._transplant(min_node, min_node.right)
                min_node.right = deleting_node.right
                min_node.right.parent = min_node

            self._transplant(deleting_node, min_node)
            min_node.left = deleting_node.left
            min_node.left.parent = min_node

            self._delete_fixup(min_node)

    # Override
    def get_min(self, node: Optional[AVLNode]) -> AVLNode:
        """See :func:`~binary_tree.BinaryTree.get_min`."""
        if node:
            current_node = node
        else:
            if self.root:
                current_node = self.root
            else:
                raise tree_exceptions.EmptyTreeError()

        while current_node.left:
            current_node = current_node.left
        return current_node

    # Override
    def get_max(self, node: Optional[AVLNode]) -> AVLNode:
        """See :func:`~binary_tree.BinaryTree.get_max`."""
        if node:
            current_node = node
        else:
            if self.root:
                current_node = self.root
            else:
                raise tree_exceptions.EmptyTreeError()

        if current_node:
            while current_node.right:
                current_node = current_node.right
        return current_node

    # Override
    def get_successor(self,
                      node: AVLNode) -> Optional[AVLNode]:
        """See :func:`~binary_tree.BinaryTree.get_successor`."""
        if node.right:
            return self.get_min(node=node.right)
        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    # Override
    def get_predecessor(self,
                        node: AVLNode) -> Optional[AVLNode]:
        """See :func:`~binary_tree.BinaryTree.get_predecessor`."""
        if node.left:
            return self.get_max(node=node.left)
        return node.parent

    # Override
    def get_height(self, node: Optional[AVLNode]) -> int:
        """See :func:`~binary_tree.BinaryTree.get_height`."""
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 0

        return max(self.get_height(node.left),
                   self.get_height(node.right)) + 1

    def _left_rotate(self, node: AVLNode):
        temp = node.right
        node.right = temp.left
        if temp.left:
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

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        temp.height = 1 + max(self.get_height(temp.left), self.get_height(temp.right))

    def _right_rotate(self, node: AVLNode):
        temp = node.left
        node.left = temp.right
        if temp.right:
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

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        temp.height = 1 + max(self.get_height(temp.left), self.get_height(temp.right))

    def _transplant(self, deleting_node: AVLNode, replacing_node: AVLNode):

        if deleting_node.parent is None:
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node

        if replacing_node:
            replacing_node.parent = deleting_node.parent

    def _balance_factor(self, node: Optional[AVLNode]):
        if node is None:
            return -1
        return self.get_height(node.left) - self.get_height(node.right)

    # FIXME
    def _delete_fixup(self, fixing_node: AVLNode):

        while fixing_node:
            fixing_node.height = 1 + max(self.get_height(fixing_node.left), self.get_height(fixing_node.right))

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

    print(repr(test))

    print(test.root.height)

    for item in traversal.inorder_traverse(tree=test):
        print(item)

    test.delete(20)
    test.delete(11)

    print(traversal.inorder_traverse(tree=test))
    print(traversal.preorder_traverse(tree=test))

