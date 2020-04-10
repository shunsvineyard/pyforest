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
    height: int = 1


class AVLTree(binary_tree.BinaryTree):
    """AVL Tree."""

    def __init__(self, key: binary_tree.KeyType = None, data: Any = None):
        binary_tree.BinaryTree.__init__(self)
        if key and data:
            self.root = AVLNode(key=key, data=data)

    # Overriding abstract method
    def search(self, value):
        pass

    # Overriding abstract method
    def insert(self, value):
        pass

    # Overriding abstract method
    def delete(self, value):
        pass
