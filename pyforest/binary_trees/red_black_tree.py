# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""Red-Black Tree."""

import enum

from dataclasses import dataclass
from typing import Any, Generic, Optional, NoReturn

from pyforest.binary_trees import binary_tree


class Color(enum.Enum):
    Red = enum.auto()
    Black = enum.auto()


@dataclass
class RBNode(binary_tree.Node, Generic[binary_tree.KeyType]):
    left: Optional["RBNode"] = None
    right: Optional["RBNode"] = None
    parent: Optional["RBNode"] = None
    color: Color = Color.Black


class RBTree(binary_tree.BinaryTree):
    """Red-Black Tree."""

    def __init__(self, key: binary_tree.KeyType = None, data: Any = None):
        binary_tree.BinaryTree.__init__(self)
        self.root: Optional[RBNode] = None
        if key and data:
            self.root = RBNode(key=key, data=data)

    def _left_rotate(self, node: RBNode):

        temp = node.right
        node.right = temp.left
        if temp.left:
            temp.left.parent = node
        temp.parent = node.parent

        if node.parent is None:
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
        if temp.right:
            temp.right.parent = node
        temp.parent = node.parent

        if node.parent is None:
            self.root = temp
        elif node == node.parent.right:
            node.parent.right = temp
        else:
            node.parent.left = temp

        temp.right = node
        node.parent = temp

    def _insert_fixup(self, node: RBNode):
        pass

    # Overriding abstract method
    def search(self, key: Any) -> Any:
        pass

    # Overriding abstract method
    def insert(self, key: Any, data: Any):
        node = RBNode(key=key, data=data, color=Color.Red)
        parent: Optional[RBNode] = None
        temp: Optional[RBNode] = self.root
        while temp:
            parent = temp
            if key < temp.key:
                temp = temp.left
            else:
                temp = temp.right
        if parent is None:
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
