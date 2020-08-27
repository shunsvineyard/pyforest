# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A base class for binary trees.

Notes
-----
The module provides some custom types for type checking.
- `KeyType`: the key type for a tree node. The key must be comparable.

- `Paris`: an iterator of Key-Value pairs. Yield by traversal functions.

- `NodeType`: the type that a derived node class should bound to.
"""

import abc

from dataclasses import dataclass
from typing import Any, Generic, Iterator, Optional, Tuple, TypeVar


class Comparable(abc.ABC):
    """Custom defined `Comparable` type for type hint."""

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


KeyType = TypeVar("KeyType", bound=Comparable)
"""Type of a tree node key. The key must be comparable."""

Pairs = Iterator[Tuple[KeyType, Any]]
"""An iterator of Key-Value pairs. Yield by traversal functions."""


@dataclass
class Node(Generic[KeyType]):
    """Basic binary tree node definition."""

    key: KeyType
    data: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None


NodeType = TypeVar("NodeType", bound=Node)
"""Type of a tree node that a derived node class should bound to."""


class BinaryTree(abc.ABC, Generic[NodeType]):
    """An abstract base class for any types of binary trees.

    This base class defines the basic properties and methods that all types of
    binary tress should provide.

    Attributes
    ----------
    root: `Optional[NodeType]`
        The root of the tree. The default is `None`.

    Notes
    -----
    One reason to use abstract base class for all types of binary trees
    is to make sure the type of binary trees is compatable. Therefore, binary
    tree traversal can be performed on any type of binary trees.
    """

    def __init__(self):
        self.root: Optional[NodeType] = None

    def __repr__(self):
        return f"{type(self)}, root={self.root}, " \
               f"tree_height={str(self.get_height(self.root))}"

    @abc.abstractmethod
    def search(self, key: KeyType) -> NodeType:
        """Search data based on the given key.

        Parameters
        ----------
        key: `KeyType`
            The key associated with the data.

        Returns
        -------
        `NodeType`
            The found node whose key is the same as the given key.
        Note that the type of the node depends on the derived class, and
        the node type should derive from `NodeType`.

        Raises
        ------
        `KeyNotFoundError`
            Raised if the key does not exist.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def insert(self, key: KeyType, data: Any):
        """Insert data and its key into the binary tree.

        Parameters
        ----------
        key: `KeyType`
            The key associated with the data.

        data: `Any`
            The data to be inserted.

        Raises
        ------
        `DuplicateKeyError`
            Raised if the input data has existed in the tree.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, key: KeyType):
        """Delete the node based on the given key.

        Parameters
        ----------
        key: `KeyType`
            The key of the node to be deleted.

        Raises
        ------
        `KeyNotFoundError`
            Raised if the key does not exist.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_leftmost(self, node: NodeType) -> NodeType:
        """Get the leftmost node from a given subtree.

        The key of the leftmost node is the smallest key in a given subtree.

        Parameters
        ----------
        node: `NodeType`
            The root of the subtree.

        Returns
        -------
        `NodeType`
            The node whose key is the smallest from the subtree of
            the given node.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_rightmost(self, node: NodeType) -> NodeType:
        """Get the rightmost node from a given subtree.

        The key of the rightmost node is the biggest key in a given subtree.

        Parameters
        ----------
        node: `Optional[NodeType]`
            The root of the subtree.

        Returns
        -------
        `NodeType`
            The node whose key is the biggest from the subtree of
            the given node.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_successor(self, node: NodeType) -> Optional[NodeType]:
        """Get the successor node in the in-order order.

        Parameters
        ----------
        node: `NodeType`
            The node to get its successor.

        Returns
        -------
        `Optional[NodeType]`
            The successor node.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_predecessor(self, node: NodeType) -> Optional[NodeType]:
        """Get the predecessor node in the in-order order.

        Parameters
        ----------
        node: `NodeType`
            The node to get its predecessor.

        Returns
        -------
        `Optional[NodeType]`
            The predecessor node.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_height(self, node: NodeType) -> int:
        """Get the height of the given node.

        Parameters
        ----------
        node: `NodeType`
            The node to get its height.

        Returns
        -------
        `int`
            The height of the given node.
        """
        raise NotImplementedError()

    @property
    def empty(self) -> bool:
        """bool: `True` if the tree is empty; `False` otherwise.

        Notes
        -----
        The property, `empty`, is read-only.
        """
        if isinstance(self.root, Node):
            return False
        return True
