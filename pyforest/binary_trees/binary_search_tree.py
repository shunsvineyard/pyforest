# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A Binary Search Tree (BST) module.

A BST is a binary tree with the following properties:

- The left subtree of a node contains only nodes whose keys are less
  than or equal to the node’s key
- The right subtree of a node contains only nodes whose keys are
  greater than the node’s key

Besides, BST should provide, at least, these Basic Operations:
- Search: search an element in a tree
- Insert: insert an element in a tree
- Delete: delete an element in a tree
- Traversal: traverses a tree

A BST keeps the keys in sorted order so that the operations can use
the principle of binary search. In general, the time complexity of
a BST is as the table.

+------------+------------+-----------+
| Operations | Average    | Worst     |
+============+============+===========+
| Space      | O(n)       | O(n)      |
+------------+------------+-----------+
| Search     | O(log n)   | O(n)      |
+------------+------------+-----------+
| Insert     | O(log n)   | O(n)      |
+------------+------------+-----------+
| Delete     | O(log n)   | O(n)      |
+------------+------------+-----------+
"""

from typing import Any, Optional

from pyforest.binary_trees import binary_tree


class BinarySearchTree(binary_tree.BinaryTree):
    """Binary Search Tree (BST) class.

    Attributes
    ----------
    root: node
        The root node of the binary search tree.

    Methods
    -------
    delete(key: KeyType)
        Delete data from a tree based on the key.
    get_height()
        Return the height of the tree.
    get_max()
        Return the maximum key from the tree.
    get_min()
        Return the minimum key from the tree.
    insert(key: KeyType, data: Any)
        Insert a key and data pair into a tree.
    is_balance()
        Check if the tree is balance.
    search(key: KeyType)
        Look for the key in a tree.
    size()
        Return the total number of nodes of the tree.

    Examples
    --------
    >>> from pyforest.binary_trees import binary_search_tree
    >>> tree = binary_search_tree.BinarySearchTree()
    >>> tree.insert(key=23, data="23")
    >>> tree.insert(key=4, data="4")
    >>> tree.insert(key=30, data="30")
    >>> tree.insert(key=11, data="11")
    >>> tree.insert(key=7, data="7")
    >>> tree.insert(key=34, data="34")
    >>> tree.insert(key=20, data="20")
    >>> tree.insert(key=24, data="24")
    >>> tree.insert(key=22, data="22")
    >>> tree.insert(key=15, data="15")
    >>> tree.insert(key=1, data="1")
    >>> tree.size()
    11
    >>> tree.get_min()
    1
    >>> tree.get_max()
    34
    >>> tree.get_height()
    4
    >>> tree.is_balance()
    False
    >>> tree.search(24)
    24
    >>> tree.delete(15)
    """

    def __init__(self, key: binary_tree.KeyType = None, data: Any = None):
        binary_tree.BinaryTree.__init__(self)
        if key and data:
            self.root = binary_tree.Node(key=key, data=data)

    def insert(self, key: binary_tree.KeyType, data: Any):
        """Insert data and its key into the binary tree.

        Parameters
        ----------
        key: `KeyType`
            A unique key associated with the data.

        data: Any
            The data to be inserted into the tree.

        recursive: bool
            A binary tree insertion can be implemented by either
            recursive or iterative. If True, use recursive implementation;
            False, otherwise.

        Raises
        ------
        ValueError
            If the input data has existed in the tree, `ValueError`
            will be thrown.
        """
        new_node = binary_tree.Node(key=key, data=data)
        parent = None
        temp = self.root
        while temp:
            parent = temp
            if new_node.key == temp.key:
                raise ValueError(f"Duplicate key {new_node.key}")
            elif new_node.key < temp.key:
                temp = temp.left
            else:
                temp = temp.right
        new_node.parent = parent
        # If the tree is empty
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    # Override
    def delete(self, key: binary_tree.KeyType):
        """See :func:`~binary_tree.BinaryTree.delete`."""
        if self.root:
            deleting_node = binary_tree.BinaryTree.search(self, key=key)

            # No child or only one right child
            if deleting_node.left is None:
                self._transplant(deleting_node=deleting_node,
                                 replacing_node=deleting_node.right)
            # Only one left child
            elif deleting_node.right is None:
                self._transplant(deleting_node=deleting_node,
                                 replacing_node=deleting_node.left)
            # Two children
            else:
                min_node = \
                    binary_tree.BinaryTree.get_min(self,
                                                   node=deleting_node.right)
                # the minmum node is not the direct child of the deleting node
                if min_node.parent != deleting_node:
                    self._transplant(deleting_node=min_node,
                                     replacing_node=min_node.right)
                    min_node.right = deleting_node.right
                    min_node.right.parent = min_node
                self._transplant(deleting_node=deleting_node,
                                 replacing_node=min_node)
                min_node.left = deleting_node.left
                min_node.left.parent = min_node

    def _transplant(self, deleting_node: binary_tree.Node,
                    replacing_node: Optional[binary_tree.Node]):
        if deleting_node.parent is None:
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node
        if replacing_node:
            replacing_node.parent = deleting_node.parent
