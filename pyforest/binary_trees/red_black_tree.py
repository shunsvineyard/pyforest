# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""Red-Black Tree."""

import enum

from dataclasses import dataclass
from typing import Any, Generic, NoReturn, Optional, TypeVar, Union

from pyforest.binary_trees import binary_tree


class Color(enum.Enum):
    Red = enum.auto()
    Black = enum.auto()


@dataclass
class LeafNode():
    left = None
    right = None
    parent = None
    color = Color.Black


@dataclass
class RBNode(Generic[binary_tree.KeyType]):
    key: binary_tree.KeyType
    data: Any
    left: Union["RBNode", LeafNode]
    right: Union["RBNode", LeafNode]
    parent: Union["RBNode", LeafNode]
    color: Color


class RBTree(binary_tree.BinaryTree):
    """Red-Black Tree."""

    def __init__(self, key: binary_tree.KeyType = None, data: Any = None):
        binary_tree.BinaryTree.__init__(self)
        self._NIL: LeafNode = LeafNode()
        self.root: RBNode = self._NIL
        if key and data:
            self.root = RBNode(key=key, data=data, left=self._NIL,
                               right=self._NIL, parent=self._NIL,
                               color=Color.Black)

    def _left_rotate(self, node: RBNode):

        temp = node.right
        node.right = temp.left
        if temp.left is not self._NIL:
            temp.left.parent = node
        temp.parent = node.parent

        if node.parent is self._NIL:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp

        temp.left = node
        node.parent = temp

    def _right_rotate(self, node: RBNode):
        temp = node.left
        node.left = temp.right
        if temp.right is not self._NIL:
            temp.right.parent = node
        temp.parent = node.parent

        if node.parent is self._NIL:
            self.root = temp
        elif node == node.parent.right:
            node.parent.right = temp
        else:
            node.parent.left = temp

        temp.right = node
        node.parent = temp

    def _insert_fixup(self, fixing_node: RBNode):
        while fixing_node.parent.color == Color.Red:
            if fixing_node.parent == fixing_node.parent.parent.left:
                temp = fixing_node.parent.parent.right
                if temp.color == Color.Red:
                    fixing_node.parent.color = Color.Black
                    temp.color = Color.Black
                    fixing_node.parent.parent.color = Color.Red
                    fixing_node = fixing_node.parent.parent
                else:
                    if fixing_node == fixing_node.parent.right:
                        fixing_node = fixing_node.parent
                        self._left_rotate(fixing_node)
                    fixing_node.parent.color = Color.Black
                    fixing_node.parent.parent.color = Color.Red
                    self._right_rotate(fixing_node.parent.parent)
            else:
                temp = fixing_node.parent.parent.left
                if temp.color == Color.Red:
                    fixing_node.parent.color = Color.Black
                    temp.color = Color.Black
                    fixing_node.parent.parent.color = Color.Red
                    fixing_node = fixing_node.parent.parent
                else:
                    if fixing_node == fixing_node.parent.left:
                        fixing_node = fixing_node.parent
                        self._right_rotate(fixing_node)
                    fixing_node.parent.color = Color.Black
                    fixing_node.parent.parent.color = Color.Red
                    self._left_rotate(fixing_node.parent.parent)

        self.root.color = Color.Black

    def _delete_fixup(self, fixing_node: RBNode):
        while (fixing_node is not self.root) and (fixing_node.color == Color.Black):
            if fixing_node == fixing_node.parent.left:
                sibling = fixing_node.parent.right

                # Case 1: the sibling is red.
                if sibling.color == Color.Red:
                    sibling.color == Color.Black
                    fixing_node.parent.color = Color.Red
                    self._left_rotate(fixing_node.parent)
                    sibling = fixing_node.parent.right

                # Case 2: the sibling is black and its children are black.
                if (sibling.left.color == Color.Black) and \
                   (sibling.right.color == Color.Black):
                   sibling.color = Color.Red
                   fixing_node = fixing_node.parent # new fixing node

                # Cases 3 and 4: the sibling is black and one of
                # its child is red and the other is black.
                else:
                    # Case 3: the sibling is black and its left child is red.
                    if sibling.right.color == Color.Black:
                        sibling.left.color = Color.Black
                        sibling.color = Color.Red
                        self._right_rotate(node=sibling)

                    # Case 4: the sibling is black and its right child is red.
                    sibling.color = fixing_node.parent.color
                    fixing_node.parent.color = Color.Black
                    sibling.right.color = Color.Black
                    self._left_rotate(node=fixing_node.parent)
                    fixing_node = self.root
            else:
                sibling = fixing_node.parent.left
                if sibling.color == Color.Red:
                    sibling.color == Color.Black
                    fixing_node.parent.color = Color.Red
                    self._right_rotate(node=fixing_node.parent)
                    sibling = fixing_node.parent.left
                if (sibling.right.color == Color.Black) and \
                   (sibling.left.color == Color.Black):
                   sibling.color = Color.Red
                   fixing_node = fixing_node.parent
                else:
                    if sibling.left.color == Color.Black:
                        sibling.right.color = Color.Black
                        sibling.color = Color.Red
                        self._left_rotate(node=sibling)
                    sibling.color = fixing_node.parent.color
                    fixing_node.parent.color = Color.Black
                    sibling.left.color = Color.Black
                    self._right_rotate(node=fixing_node.parent)
                    fixing_node = self.root

        fixing_node.color = Color.Black

    def _transplant(self, deleting_node: RBNode, replacing_node: RBNode):
        if deleting_node.parent == self._NIL:
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node

        replacing_node.parent = deleting_node.parent

    # Overriding abstract method
    def insert(self, key: Any, data: Any):
        node = RBNode(key=key, data=data, left=self._NIL, right=self._NIL,
                      parent=self._NIL, color=Color.Red)
        parent: RBNode = self._NIL
        temp: RBNode = self.root
        while temp is not self._NIL:
            parent = temp
            if node.key < temp.key:
                temp = temp.left
            else:
                temp = temp.right
        if parent is self._NIL:
            node.color = Color.Black
            self.root = node
        else:
            node.parent = parent

            if node.key < parent.key:
                parent.left = node
            else:
                parent.right = node

            self._insert_fixup(node)

    # Overriding abstract method
    def delete(self, key: Any) -> NoReturn:
        if self.root is None:
            return None

        deleting_node = binary_tree.BinaryTree._search(self, key=key, node=self.root)

        original_color = deleting_node.color
        temp: Union[RBNode, LeafNode] = self._NIL

        # No children or only one right child
        if deleting_node.left == self._NIL:
            temp = deleting_node.right
            self._transplant(deleting_node=deleting_node,
                             replacing_node=deleting_node.right)

        # Only one left child
        elif deleting_node.right == self._NIL:
            temp = deleting_node.left
            self._transplant(deleting_node=deleting_node,
                             replacing_node=deleting_node.left)

        # Two children
        else:
            min_node = binary_tree.BinaryTree._get_min(self, deleting_node.right)
            original_color = min_node.color
            temp = min_node.right
            # if the minimum node is the direct child of the deleting node
            if min_node.parent == deleting_node:
                temp.parent = deleting_node
            else:
                self._transplant(min_node, min_node.right)
                min_node.right = deleting_node.right
                min_node.right.parent = min_node

            self._transplant(deleting_node, min_node)
            min_node.left = deleting_node.left
            min_node.left.parent = min_node
            min_node.color = deleting_node.color

        if original_color == Color.Black:
            self._delete_fixup(fixing_node=temp)

    # Override
    def _get_min(self, node: RBNode) -> RBNode:
        """Real implementation of getting the leftmost node.

        Parameters
        ----------
        node: Node
            The root of the tree.

        Retruns
        -------
        Node
            Return the leftmost node in the tree.
        """
        current_node = node
        while current_node.left and current_node.left is not self._NIL:
            current_node = current_node.left
        return current_node

    # Override
    def get_min(self) -> Any:
        """Return the minimum key from the tree."""
        if self.root is None:
            return None
        return self._get_min(self.root).key

    # Override
    def search(self, key: Any) -> Any:
        """Search data based on the given key.

        Parameters
        ----------
        key: KeyType
            The key associated with the data.

        Returns
        -------
        Any
            The data based on the given key; None if the key not found.

        Raises
        ------
        KeyError
            If the key does not exist, `KeyError` will be thrown.
        """
        if self.root is None:
            return None

        return self._search(key=key, node=self.root).data

    # Override
    def _search(self, key: binary_tree.KeyType, node: RBNode) -> RBNode:
        """Real implementation of search.

        Parameters
        ----------
        key: KeyType
            The key of the data.
        node: Node
            The node to check if its key matches the given key.

        Retruns
        -------
        Node
            Return the node if the key matches, or the node for next recursion.

        Raises
        ------
        KeyError
            If the key does not exist, `KeyError` will be thrown.
        """

        if node is self._NIL:
            raise KeyError(f"Key {key} not found")

        if key == node.key:
            return node
        elif key < node.key:
            if node.left is not None:
                return self._search(key=key, node=node.left)
            else:
                raise KeyError(f"Key {key} not found")
        else:  # key > node.key
            if node.right is not None:
                return self._search(key=key, node=node.right)
            else:
                raise KeyError(f"Key {key} not found")

    # FIXME: test only
    def inorder(self, n):
        if n != self._NIL:
            self.inorder(n.left)
            print(n.data)
            self.inorder(n.right)


if __name__ == "__main__":
    tree = RBTree()
    tree.insert(key=23, data=23)
    tree.insert(key=4, data=4)
    tree.insert(key=30, data=30)
    tree.insert(key=11, data=11)
    tree.insert(key=7, data=7)
    tree.insert(key=34, data=34)
    tree.insert(key=20, data=20)
    tree.insert(key=24, data=24)
    tree.insert(key=22, data=22)
    tree.insert(key=15, data=15)
    tree.insert(key=1, data=1)

    tree.inorder(n=tree.root)

    tree.delete(key=11)

    tree.inorder(n=tree.root)

    # FIXME: bug in deleting a node which has two children
    #tree.delete(key=23)

    #tree.inorder(n=tree.root)
