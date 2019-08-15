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

from pyforest.binary_trees import base_tree

from pyforest.binary_trees import traversal

from typing import Any, Generic, NoReturn, Optional

import dataclasses


@dataclasses.dataclass
class Node(Generic[base_tree.KeyType]):
    """Basic tree node class.

    Attributes
    ----------
    key: KeyType
        A key can be anything that is comparable.

    data: Any
        The data that the node contains.

    parent: Any
        The parant of the node.

    left: node
        The left child of the node.

    right: node
        The right child of the node.
    """

    key: base_tree.KeyType
    data: Any
    parent: Optional["Node"]
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BinarySearchTree(base_tree.BaseTree):
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

    def __init__(self, key: base_tree.KeyType = None, data: Any = None):
        base_tree.TreeType.__init__(self)
        if key and data:
            self.root = Node(key=key, data=data, parent=None)
        self._size = 1 if key and data else 0

    def _insert(self, key: base_tree.KeyType, data: Any, node: Node):
        """Real implementation of tree insertion.

        Parameters
        ----------
        key: KeyType
            The key of the data.
        data: Any
            The data to be inserted into the tree.
        node: Node
            The parent node of the input data.

        Raises
        ------
        ValueError
            If the input data has existed in the tree, `ValueError`
            will be thrown.
        """
        if key == node.key:
            raise ValueError("Duplicate key")
        elif key < node.key:
            if node.left is not None:
                self._insert(key=key, data=data, node=node.left)
            else:
                node.left = Node(key=key, data=data, parent=node)
        else:  # key > node.key
            if node.right is not None:
                self._insert(key=key, data=data, node=node.right)
            else:
                node.right = Node(key=key, data=data, parent=node)

    def _search(self, key: base_tree.KeyType, node: Node) -> Node:
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

    def _get_min(self, node: Node) -> Node:
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
        while current_node.left:
            current_node = current_node.left
        return current_node

    def _height(self, node: Optional[Node]) -> int:
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

    def _is_balance(self, node: Node) -> bool:
        """Real implementation of checking if a tree is balance.

        Parameters
        ----------
        node: Node
            The root of the tree.

        Retruns
        -------
        bool
            Return True if the tree is balance; False otherwise.
        """
        left_hight = self._height(node.left)
        right_height = self._height(node.right)

        if (abs(left_hight - right_height) > 1):
            return False

        if node.left:
            if not self._is_balance(node=node.left):
                return False
        if node.right:
            if not self._is_balance(node=node.right):
                return False

        return True

    # Overriding abstract method
    def search(self, key: base_tree.KeyType) -> Any:
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
        if self._size == 0:
            return None

        return self._search(key=key, node=self.root).data

    # Overriding abstract method
    def insert(self, key: base_tree.KeyType, data: Any):
        """Insert data and its key into the binary tree.

        Parameters
        ----------
        key: KeyType
            A unique key associated with the data.

        data: Any
            The data to be inserted into the tree.

        Raises
        ------
        ValueError
            If the input data has existed in the tree, `ValueError`
            will be thrown.
        """
        if self._size == 0:
            self.root = Node(key=key, data=data, parent=None)
        else:
            self._insert(key=key, data=data, node=self.root)

        self._size += 1

    # Overriding abstract method
    def delete(self, key: base_tree.KeyType):
        """Delete the data based on the given key.

        Parameters
        ----------
        key: KeyType
            The key associated with the data.
        """
        if self._size != 0:
            deleting_node: Node = self._search(key=key, node=self.root)

            if deleting_node.parent is None:
                raise ValueError("Node's parent cannot be None")

            # No children
            if deleting_node.left is None and deleting_node.right is None:
                if deleting_node.parent.left == deleting_node:
                    deleting_node.parent.left = None
                else:
                    deleting_node.parent.right = None
                del(deleting_node)

            # Two children
            elif deleting_node.left and deleting_node.right:
                # Find the min node on the right sub-tree
                candidate = self._get_min(node=deleting_node.right)

                if candidate.parent is None:
                    raise ValueError("Node's parent cannot be None")

                # Copy the candidate to the deleting node
                deleting_node.key = candidate.key
                deleting_node.data = candidate.data
                # Delete the candidate
                if candidate.parent.left == candidate:
                    candidate.parent.left = None
                else:
                    candidate.parent.right = None

                del(candidate)

            # One child
            else:

                if deleting_node.parent is None:
                    raise ValueError("Node's parent cannot be None")

                # One child (left)
                if deleting_node.left and deleting_node.right is None:

                    deleting_node.left.parent = deleting_node.parent

                    if deleting_node.parent.left == deleting_node:
                        deleting_node.parent.left = deleting_node.left
                    else:
                        deleting_node.parent.right = deleting_node.left
                # One child (right)
                elif deleting_node.right and deleting_node.left is None:
                    deleting_node.right.parent = deleting_node.parent

                    if deleting_node.parent.left == deleting_node:
                        deleting_node.parent.left = deleting_node.right
                    else:
                        deleting_node.parent.right = deleting_node.right
                # Should never happen
                else:
                    raise RuntimeError("Fatal error")

                del(deleting_node)
            self._size -= 1

        # If the tree is empty, do nothing

    def get_min(self) -> Any:
        """Return the minimum key from the tree."""
        if self._size == 0:
            return None
        return self._get_min(self.root).key

    def get_max(self) -> Any:
        """Return the maximum key from the tree."""
        if self._size == 0:
            return None

        node = self.root

        while node.right is not None:
            node = node.right

        return node.key

    def get_height(self) -> int:
        """Return the height of the tree."""
        return self._height(self.root)

    def is_balance(self) -> bool:
        """Check if the tree is balance.

        Returns
        -------
        bool
            True is the tree is balance; False otherwise.
        """
        if self._size == 0:
            return True

        return self._is_balance(node=self.root)

    def size(self) -> int:
        """Return the total number of nodes of the tree."""
        return self._size


def is_valid_binary_search_tree(tree: base_tree.TreeType):
    """Check if a binary tree is a valid BST.

    Parameters
    ----------
    tree : base_tree.TreeType
        A type of binary tree.

    Returns
    -------
    bool
        True is the tree is a BST; False otherwise.

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
    >>> binary_search_tree.is_valid_binary_search_tree(tree)
    True
    """
    in_order_result = traversal.inorder_traverse(tree=tree)

    for index in range(len(in_order_result) - 1):
        if in_order_result[index] > in_order_result[index + 1]:
            return False
    return True
