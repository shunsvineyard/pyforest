# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""Red-Black Tree."""

import enum

from dataclasses import dataclass
from typing import Any, Generic, NoReturn, Optional, Union

from pyforest.binary_trees import binary_tree


class Color(enum.Enum):
    Red = enum.auto()
    Black = enum.auto()


@dataclass
class LeafNode:
    left = None
    right = None
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

    def _insert_fixup(self, node: RBNode):
        while node.parent.color == Color.Red:
            if node.parent == node.parent.parent.left:
                temp = node.parent.parent.right
                if temp.color == Color.Red:
                    node.parent.color = Color.Black
                    temp.color = Color.Black
                    node.parent.parent.color = Color.Red
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = Color.Black
                    node.parent.parent.color = Color.Red
                    self._right_rotate(node.parent.parent)
            else:
                temp = node.parent.parent.left
                if temp.color == Color.Red:
                    node.parent.color = Color.Black
                    temp.color = Color.Black
                    node.parent.parent.color = Color.Red
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = Color.Black
                    node.parent.parent.color = Color.Red
                    self._left_rotate(node.parent.parent)

        self.root.color = Color.Black

    # Overriding abstract method
    def search(self, key: Any) -> Any:
        pass

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
        pass
