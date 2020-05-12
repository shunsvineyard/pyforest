# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A base class for binary trees."""

import abc

from dataclasses import dataclass
from typing import Any, Generic, Iterator, Optional, Tuple, TypeVar


class Comparable(abc.ABC):
    @abc.abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass

    @abc.abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass

    def __gt__(self, other) -> bool:
        return (not self < other) and self != other

    def __le__(self, other) -> bool:
        return self < other or self == other

    def __ge__(self, other) -> bool:
        return (not self < other)


# User-defined type for a tree node key. The key must be comparable.
KeyType = TypeVar("KeyType", bound=Comparable)

# An iterator of Key-Value pairs. Yield by traversal functions.
Pairs = Iterator[Tuple[KeyType, Any]]


@dataclass
class Node(Generic[KeyType]):
    """The `Node` class defines the basic binary tree node."""

    key: KeyType
    data: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None


class BinaryTree(abc.ABC):
    """An abstract base class for any types of binary trees.

    This base class defines the basic properties and methods that all types of
    binary tress should provide.

    Methods
    -------
    search(value: Any)
        Search a binary tree for a specific value.

    insert(value: Any)
        Insert a value into a binary tree.

    delete(value: Any)
        Delete a value from a binary treeW.

    Note: One reason to use abstract base class for all types of binary trees
    is to make sure the type of binary trees is compatable. Therefore, binary
    tree traversal can be performed on any type of binary trees.
    """

    def __init__(self):
        self.root: Optional[Node] = None

    @abc.abstractmethod
    def insert(self, key: Any, data: Any):
        """Insert data and its key into the binary tree.

        Parameters
        ----------
        key: `KeyType`
            A unique key associated with the data.

        data: Any
            The data to be inserted into the tree.

        Raises
        ------
        ValueError
            If the input data has existed in the tree, `ValueError`
            will be thrown.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, key: Any):
        """Delete the data based on the given key.

        Parameters
        ----------
        key: KeyType
            The key associated with the data.
        """
        raise NotImplementedError

    def search(self, key: Any) -> Node:
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
        temp = self.root
        while temp:
            if key < temp.key:
                temp = temp.left
            elif key > temp.key:
                temp = temp.right
            else:  # Key found
                return temp
        raise KeyError(f"Key {key} not found")

    def get_min(self, node: Node) -> Node:
        """Get the node whose key is the smallest from the subtree.

        Parameters
        ----------
        node: Node
            The root of the subtree.

        Returns
        -------
        Node
            The node whose key is the smallest from the subtree of
            the given node.
        """
        if node is None:
            raise KeyError(f"{node} does not have min node")
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node

    def get_max(self, node: Node) -> Optional[Node]:
        """Get the node whose key is the biggest from the subtree.

        Parameters
        ----------
        node: Node
            The root of the subtree.

        Returns
        -------
        Node
            The node whose key is the biggest from the subtree of
            the given node.
        """
        current_node = node
        if current_node:
            while current_node.right:
                current_node = current_node.right
        return current_node

    def get_successor(self, node: Node) -> Optional[Node]:
        """Get the successor node in the in-order order.

        Parameters
        ----------
        node: Node
            The node to get its successor.

        Returns
        -------
        Node
            The successor node.
        """
        if node.right:
            return self.get_min(node=node.right)
        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    def get_predecessor(self, node: Node) -> Optional[Node]:
        """Get the predecessor node in the in-order order.

        Parameters
        ----------
        node: Node
            The node to get its predecessor.

        Returns
        -------
        Node
            The predecessor node.
        """
        if node.left:
            return self.get_max(node=node.left)
        return node.parent

    def get_height(self, node: Optional[Node]) -> int:
        """Get the height from the given node.

        Parameters
        ----------
        node: Node
            The node to get its height.

        Returns
        -------
        int
            The height from the given node.
        """
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 0

        return max(self.get_height(node.left),
                   self.get_height(node.right)) + 1

    @property
    def empty(self) -> bool:
        """Return if the tree is empty.

        Returns
        -------
        bool
            True if the tree is empty; False otherwise.
        """
        if self.root:
            return False
        return True


# User-defined type for a binary tree.
TreeType = TypeVar("TreeType", bound=BinaryTree)
