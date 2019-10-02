# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""Threaded Binary Tree module.

Threaded binary tree is a binary search tree variant that optimize traversal
in a particular order by making all right child of leaf nodes pointer to
their in-order successor of the node (if it exists). There are two types
of threaded binary tree:
- Single Threaded
- Double Threaded
"""

from dataclasses import dataclass
from typing import Optional

from pyforest.binary_trees import binary_tree


@dataclass
class SingleThreadNode(binary_tree.Node):
    left: Optional["SingleThreadNode"] = None
    right: Optional["SingleThreadNode"] = None
    isThread: bool = False


@dataclass
class DoubleThreadNode(binary_tree.Node):
    left: Optional["DoubleThreadNode"] = None
    right: Optional["DoubleThreadNode"] = None
    leftThread: bool = False
    rightThread: bool = False


class SingleThreadedBinaryTree(binary_tree.BinaryTree):
    """Threaded Binary Tree."""

    def __init__(self):
        self._left = None
        self._right = None
        self._data = None

    # Overriding abstract method
    def search(self, value):
        pass

    # Overriding abstract method
    def insert(self, value):
        pass

    # Overriding abstract method
    def delete(self, value):
        pass

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def data(self):
        return self._data


class DoubleThreadedBinaryTree(binary_tree.BinaryTree):
    """Threaded Binary Tree."""

    def __init__(self):
        self._left = None
        self._right = None
        self._data = None

    # Overriding abstract method
    def search(self, value):
        pass

    # Overriding abstract method
    def insert(self, value):
        pass

    # Overriding abstract method
    def delete(self, value):
        pass

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def data(self):
        return self._data