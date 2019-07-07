# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A Binary Search Tree (BST) is a binary tree with
the following properties:

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

from pyforest.binary_trees import _base_tree

from typing import Any, NoReturn


class BinarySearchTree(_base_tree.BaseTree):
    """A Binary Search Tree (BST)

    Attributes
    ----------
    left: node
        The left node.
    right: node
        The right node.
    data: Any
        The value the node holds.

    Methods
    -------
    search(value: Any)
        Look for the value in a tree.
    insert(value: Any)
        Insert the value into a tree.
    delete(value: Any)
        Delete the value from a tree.

    Examples
    --------
    TODO: example use simple examples.
    """

    def __init__(self, key: Any = None, data: Any = None):
        _base_tree.BaseTree.__init__(self)
        if key and data:
            self.root = _base_tree.Node(key=key, data=data)
        self._size = 1 if key and data else 0

    def _insert(self, key: Any, data: Any, node: _base_tree.Node) -> NoReturn:
        """The real implementation of tree insertion.
        Parameters
        ----------
        data: int
            The data to be inserted into the tree.
        node: _Node
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
            if node.left != None:
                self._insert(key=key, data=data, node=node.left)
            else:
                node.left = _base_tree.Node(key=key, data=data)
                node.left.parent = node
        elif key > node.key:
            if node.right != None:
                self._insert(key=key, data=data, node=node.right)
            else:
                node.right = _base_tree.Node(key=key, data=data)
                node.right.parent = node

    def _search(self, key: Any, node: _base_tree.Node) -> _base_tree.Node:
        """
        """
        if key == node.key:
            return node
        elif key < node.key:
            if node.left != None:
                return self._search(key=key, node=node.left)
            else:
                raise KeyError(f"Key {key} not found")
        elif key > node.key:
            if node.right != None:
                return self._search(key=key, node=node.right)
            else:
                raise KeyError(f"Key {key} not found")

    def _get_min(self, node: _base_tree.Node) -> _base_tree.Node:
        """
        """
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node

    def _height(self, node:_base_tree.Node) -> int:
        """
        """
        if node is None:
            return 0
        
        return max(self._height(node.left), self._height(node.right)) + 1

    def _is_balance(self, node: _base_tree.Node) -> bool:
        """
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
    def search(self, key: Any) -> Any:
        """
        """
        if self._size == 0:
            return None

        return self._search(key=key, node=self.root).data

    # Overriding abstract method
    def insert(self, key: Any, data: Any) -> NoReturn:
        """Insert an item into a binary tree.

        Parameters
        ----------
        data: int
            The data to be inserted into the tree.

        Raises
        ------
        ValueError
            If the input data has existed in the tree, `ValueError`
            will be thrown.
        """

        if self._size == 0:
            self.root = _base_tree.Node(key=key, data=data)
        else:
            try:
                self._insert(key=key, data=data, node=self.root)
            except:
                raise
        self._size += 1

    # Overriding abstract method
    def delete(self, key: Any) -> NoReturn:
        """
        """
        if self._size != 0:
            deleting_node = self._search(key=key, node=self.root)

            # No children
            if deleting_node.left == None and deleting_node.right == None:
                if deleting_node.parent.left == deleting_node:
                    deleting_node.parent.left = None
                else:
                    deleting_node.parent.right = None
                del(deleting_node)

            # Two children
            elif deleting_node.left and deleting_node.right:
                # Find the min node on the right sub-tree
                candidate = self._get_min(node=deleting_node.right)
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
                # One child (left)
                if deleting_node.left and deleting_node.right == None:

                    deleting_node.left.parent = deleting_node.parent

                    if deleting_node.parent.left == deleting_node:
                        deleting_node.parent.left = deleting_node.left
                    else:
                        deleting_node.parent.right = deleting_node.left
                # One child (right)
                else:
                    deleting_node.right.parent = deleting_node.parent

                    if deleting_node.parent.left == deleting_node:
                        deleting_node.parent.left = deleting_node.right
                    else:
                        deleting_node.parent.right = deleting_node.right

                del(deleting_node)
            self._size -= 1

        # If the tree is empty, do nothing

    def get_min(self) -> Any:
        """

        Returns
        -------
        """
        if self._size == 0:
            return None
        return self._get_min(self.root).key

    def get_max(self) -> Any:
        """
        """
        if self._size == 0:
            return None

        node = self.root

        while node.right is not None:
            node = node.right

        return node.key

    def get_height(self) -> int:
        """
        """
        return self._height(self.root)

    def is_balance(self) -> bool:
        """
        """
        if self._size == 0:
            return True

        return self._is_balance(node=self.root)

    def size(self) -> int:
        """
        """
        return self._size