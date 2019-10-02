# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""Red-Black Tree."""

import enum

from dataclasses import dataclass
from typing import Optional

from pyforest.binary_trees import binary_tree


class Color(enum.Enum):
    Red = enum.auto()
    Black = enum.auto()


@dataclass
class RBNode(binary_tree.Node):
    left: Optional["RBNode"] = None
    right: Optional["RBNode"] = None
    color: Color = Color.Black


class RBTree(binary_tree.BinaryTree):
    """Red-Black Tree."""

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
