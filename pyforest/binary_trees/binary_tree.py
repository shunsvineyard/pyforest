# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A base class for binary trees."""

import abc

from dataclasses import dataclass
from typing import Any, Generic, Iterator, NoReturn, Optional, Tuple, TypeVar


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

# Key-Value type. Yield by traversal.
Pair = Iterator[Tuple[KeyType, Any]]


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
    def insert(self, key: Any, data: Any) -> NoReturn:
        """Insert data and its key into the binary tree."""
        pass

    @abc.abstractmethod
    def delete(self, key: Any) -> NoReturn:
        """Delete the data based on the given key."""
        pass

    def search(self, key: Any) -> Any:
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
        if self.root is None:
            return None

        return self._recursive_search(key=key, node=self.root).data

    def _recursive_search(self, key: KeyType, node: Node) -> Node:
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
                return self._recursive_search(key=key, node=node.left)
            else:
                raise KeyError(f"Key {key} not found")
        else:  # key > node.key
            if node.right is not None:
                return self._recursive_search(key=key, node=node.right)
            else:
                raise KeyError(f"Key {key} not found")

    def _iterative_search(self, key: KeyType) -> Node:
        temp = self.root
        while temp is not None:
            if key < temp.key:
                temp = temp.left
            elif key > temp.key:
                temp = temp.right
            else:  # Key found
                return temp
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

    def _get_max(self, node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def get_min(self) -> Optional[KeyType]:
        """Return the minimum key from the tree."""
        if self.root is None:
            return None
        return self._get_min(self.root).key

    def get_max(self) -> Optional[KeyType]:
        """Return the maximum key from the tree."""
        if self.root is None:
            return None
        return self._get_max(self.root).key

    def _get_successor(self, node: Node) -> Optional[Node]:
        if node.right:
            return self._get_min(node=node.right)
        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    def _get_predecessor(self, node: Node) -> Optional[Node]:
        if node.left:
            return self._get_max(node=node.left)
        return node.parent

    def _get_height(self, node: Optional[Node]) -> int:
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

        return max(self._get_height(node.left),
                   self._get_height(node.right)) + 1


# User-defined type for a binary tree.
TreeType = TypeVar("TreeType", bound=BinaryTree)
