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

from pyforest import tree_exceptions

from pyforest.binary_trees import binary_tree


class BinarySearchTree(binary_tree.BinaryTree):
    """Binary Search Tree (BST).

    Parameters
    ----------
    key: `KeyType`
        The key of the root when the tree is initialized.
        Default is `None`.
    data: `Any`
        The data of the root when the tree is initialized.
        Default is `None`.

    Attributes
    ----------
    root: `Optional[node]`
        The root node of the binary search tree.
    empty: `bool`
        `True` if the tree is empty; `False` otherwise.

    Methods
    -------
    search(key: `KeyType`)
        Look for a node based on the given key.
    insert(key: `KeyType`, data: `Any`)
        Insert a (key, data) pair into a binary tree.
    delete(key: `KeyType`)
        Delete a node based on the given key from the binary tree.
    get_min(node: `Optional[Node]` = `None`)
        Return the node whose key is the smallest from the given subtree.
    get_max(node: `Optional[Node]` = `None`)
        Return the node whose key is the biggest from the given subtree.
    get_successor(node: `Node`)
        Return the successor node in the in-order order.
    get_predecessor(node: `Node`)
        Return the predecessor node in the in-order order.
    get_height(node: `Optional[Node]`)
        Return the height of the given node.

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
    >>> tree.get_min().key
    1
    >>> tree.get_min().data
    '1'
    >>> tree.get_max().key
    34
    >>> tree.get_max().data
    "34"
    >>> tree.get_height(tree.root)
    4
    >>> tree.search(24).data
    `24`
    >>> tree.delete(15)
    """

    def __init__(self, key: binary_tree.KeyType = None, data: Any = None):
        binary_tree.BinaryTree.__init__(self)
        if key and data:
            self.root = binary_tree.Node(key=key, data=data)

    # Override
    def search(self, key: binary_tree.KeyType) -> binary_tree.Node:
        """See :func:`~binary_tree.BinaryTree.search`."""
        temp = self.root
        while temp:
            if key < temp.key:
                temp = temp.left
            elif key > temp.key:
                temp = temp.right
            else:  # Key found
                return temp
        raise tree_exceptions.KeyNotFoundError(key=key)

    # Override
    def insert(self, key: binary_tree.KeyType, data: Any):
        """See :func:`~binary_tree.BinaryTree.insert`."""
        new_node = binary_tree.Node(key=key, data=data)
        parent = None
        temp = self.root
        while temp:
            parent = temp
            if new_node.key == temp.key:
                raise tree_exceptions.DuplicateKeyError(key=new_node.key)
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
            deleting_node = self.search(key=key)

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
                    self.get_min(node=deleting_node.right)
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

    # Override
    def get_min(self, node: binary_tree.Node) -> binary_tree.Node:
        """Get the node whose key is the smallest from the subtree.

        Parameters
        ----------
        node: `Optional[Node]`
            The root of the subtree. If the parameter is not present,
            root will be used.

        Returns
        -------
        `Node`
            The node whose key is the smallest from the subtree of
            the given node.

        Raises
        ------
        `EmptyTreeError`
            Raised if the tree is empty.
        """
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
    def get_max(self, node: binary_tree.Node) -> binary_tree.Node:
        """Get the node whose key is the biggest from the subtree.

        Parameters
        ----------
        node: `Optional[Node]`
            The root of the subtree. If the parameter is not present,
            root will be used.

        Returns
        -------
        `Node`
            The node whose key is the biggest from the subtree of
            the given node.

        Raises
        ------
        `EmptyTreeError`
            Raised if the tree is empty.
        """
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
                      node: binary_tree.Node) -> Optional[binary_tree.Node]:
        """Get the successor node in the in-order order.

        Parameters
        ----------
        node: `Node`
            The node to get its successor.

        Returns
        -------
        `Node`
            The successor node.
        """
        if node.right:
            return self.get_min(node=node.right)
        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    # Override
    def get_predecessor(self,
                        node: binary_tree.Node) -> Optional[binary_tree.Node]:
        """Get the predecessor node in the in-order order.

        Parameters
        ----------
        node: `Node`
            The node to get its predecessor.

        Returns
        -------
        `Node`
            The predecessor node.
        """
        if node.left:
            return self.get_max(node=node.left)
        return node.parent

    # Override
    def get_height(self, node: Optional[binary_tree.Node]) -> int:
        """Get the height from the given node.

        Parameters
        ----------
        node: `Node`
            The node to get its height.

        Returns
        -------
        `int`
            The height from the given node.
        """
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 0

        return max(self.get_height(node.left),
                   self.get_height(node.right)) + 1

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
