# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A base class for binary trees."""

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


# User-defined type for a tree node key. The key must be comparable.
KeyType = TypeVar("KeyType", bound=Comparable)

# An iterator of Key-Value pairs. Yield by traversal functions.
Pairs = Iterator[Tuple[KeyType, Any]]


@dataclass
class Node(Generic[KeyType]):
    """Basic binary tree node definition."""

    key: KeyType
    data: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None


NodeType = TypeVar("NodeType", bound=Node)


class BinaryTree(abc.ABC, Generic[NodeType]):
    """An abstract base class for any types of binary trees.

    This base class defines the basic properties and methods that all types of
    binary tress should provide.

    Attributes
    ----------
    root: `Optional[Node]`
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
        `Node`
            The node based on the given key.

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
    def get_min(self, node: Optional[NodeType] = None) -> NodeType:
        """Get the node whose key is the smallest from the subtree.

        Parameters
        ----------
        node: `Optional[NodeType]`
            The root of the subtree. If the parameter is not present,
            root will be used.

        Returns
        -------
        `NodeType`
            The node whose key is the smallest from the subtree of
            the given node.

        Raises
        ------
        `EmptyTreeError`
            Raised if the tree is empty.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_max(self, node: Optional[NodeType] = None) -> NodeType:
        """Get the node whose key is the biggest from the subtree.

        Parameters
        ----------
        node: `Optional[NodeType]`
            The root of the subtree. If the parameter is not present,
            root will be used.

        Returns
        -------
        `NodeType`
            The node whose key is the biggest from the subtree of
            the given node.

        Raises
        ------
        `EmptyTreeError`
            Raised if the tree is empty.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_successor(self, node: NodeType) -> Optional[NodeType]:
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
        raise NotImplementedError()

    @abc.abstractmethod
    def get_predecessor(self, node: NodeType) -> Optional[NodeType]:
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
        raise NotImplementedError()

    @abc.abstractmethod
    def get_height(self, node: Optional[NodeType]) -> int:
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


# User-defined type for a binary tree.
TreeType = TypeVar("TreeType", bound=BinaryTree)
