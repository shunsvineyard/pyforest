# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""Red-Black Tree."""

import enum

from dataclasses import dataclass
from typing import Any, Generic, Optional, Union

from pyforest import tree_exceptions

from pyforest.binary_trees import binary_tree


class Color(enum.Enum):
    """Color definition for Red-Black Tree."""

    Red = enum.auto()
    Black = enum.auto()


@dataclass
class LeafNode:
    """Definition Red-Black Tree Leaf node whose color is always black."""

    left = None
    right = None
    parent = None
    color = Color.Black


@dataclass
class RBNode(Generic[binary_tree.KeyType]):
    """Red-Black Tree non-leaf node definition."""

    key: binary_tree.KeyType
    data: Any
    left: Union["RBNode", LeafNode]
    right: Union["RBNode", LeafNode]
    parent: Union["RBNode", LeafNode]
    color: Color


class RBTree(binary_tree.BinaryTree):
    """Red-Black Tree.

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
    root: `Union[RBNode, LeafNode]`
        The root node of the right threaded binary search tree.
    empty: `bool`
        `True` if the tree is `LeafNode`; `False` otherwise.

    Methods
    -------
    search(key: `KeyType`)
        Look for a node based on the given key.
    insert(key: `KeyType`, data: `Any`)
        Insert a (key, data) pair into the tree.
    delete(key: `KeyType`)
        Delete a node based on the given key from the tree.
    inorder_traverse()
        Perform In-order traversal.
    preorder_traverse()
        Perform Pre-order traversal.
    postorder_traverse()
        Perform Post-order traversal.
    get_min(node: `Optional[RBNode]` = `None`)
        Return the node whose key is the smallest from the given subtree.
    get_max(node: `Optional[RBNode]` = `None`)
        Return the node whose key is the biggest from the given subtree.
    get_successor(node: `RBNode`)
        Return the successor node in the in-order order.
    get_predecessor(node: `RBNode`)
        Return the predecessor node in the in-order order.
    get_height(node: `Optional[RBNode]`)
        Return the height of the given node.

    Examples
    --------
    >>> from pyforest.binary_trees import red_black_tree
    >>> tree = red_black_tree.RBTree()
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
    >>> [item for item in tree.inorder_traverse()]
    [(1, '1'), (4, '4'), (7, '7'), (11, '11'), (15, '15'), (20, '20'),
     (22, '22'), (23, '23'), (24, '24'), (30, '30'), (34, '34')]
    >>> [item for item in tree.preorder_traverse()]
    [(1, '1'), (4, '4'), (7, '7'), (11, '11'), (15, '15'), (20, '20'),
     (22, '22'), (23, '23'), (24, '24'), (30, '30'), (34, '34')]
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
        self._NIL: LeafNode = LeafNode()
        self.root: Union[RBNode, LeafNode] = self._NIL
        if key and data:
            self.root = RBNode(key=key, data=data, left=self._NIL,
                               right=self._NIL, parent=self._NIL,
                               color=Color.Black)

    # Override
    def search(self, key: binary_tree.KeyType) -> RBNode:
        """Look for a node by a given key.

        See Also
        --------
        :py:meth:`pyforest.binary_trees.binary_tree.BinaryTree.search`.
        """
        temp: Union[RBNode, LeafNode] = self.root
        while isinstance(temp, RBNode):
            if key < temp.key:
                temp = temp.left
            elif key > temp.key:
                temp = temp.right
            else:  # Key found
                return temp
        raise tree_exceptions.KeyNotFoundError(key=key)

    # Override
    def insert(self, key: binary_tree.KeyType, data: Any):
        """Insert a (key, data) pair into the Red-Black tree.

        See Also
        --------
        :py:meth:`pyforest.binary_trees.binary_tree.BinaryTree.insert`.
        """
        node = RBNode(key=key, data=data, left=self._NIL, right=self._NIL,
                      parent=self._NIL, color=Color.Red)
        parent: Union[RBNode, LeafNode] = self._NIL
        temp: Union[RBNode, LeafNode] = self.root
        while isinstance(temp, RBNode):
            parent = temp
            if node.key < temp.key:
                temp = temp.left
            else:
                temp = temp.right
        if isinstance(parent, LeafNode):
            node.color = Color.Black
            self.root = node
        else:
            node.parent = parent

            if node.key < parent.key:
                parent.left = node
            else:
                parent.right = node

            self._insert_fixup(node)

    # Override
    def delete(self, key: binary_tree.KeyType):
        """Delete the node by the given key.

        See Also
        --------
        :py:meth:`pyforest.binary_trees.binary_tree.BinaryTree.delete`.
        """
        deleting_node: RBNode = self.search(key=key)

        original_color = deleting_node.color
        temp: Union[RBNode, LeafNode] = self._NIL

        # No children or only one right child
        if isinstance(deleting_node.left, LeafNode):
            temp = deleting_node.right
            self._transplant(deleting_node=deleting_node,
                             replacing_node=deleting_node.right)

        # Only one left child
        elif isinstance(deleting_node.right, LeafNode):
            temp = deleting_node.left
            self._transplant(deleting_node=deleting_node,
                             replacing_node=deleting_node.left)

        # Two children
        else:
            min_node: RBNode = self.get_min(deleting_node.right)
            original_color = min_node.color
            temp = min_node.right
            # if the minimum node is the direct child of the deleting node
            if min_node.parent == deleting_node:
                temp.parent = min_node
            else:
                self._transplant(min_node, min_node.right)
                min_node.right = deleting_node.right
                min_node.right.parent = min_node

            self._transplant(deleting_node, min_node)
            min_node.left = deleting_node.left
            min_node.left.parent = min_node
            min_node.color = deleting_node.color

        if original_color == Color.Black:
            self._delete_fixup(fixing_node=temp)

    # Override
    def get_min(self, node: Optional[RBNode] = None) -> RBNode:
        """Return the node which has the smallest key from the subtree.

        See Also
        --------
        :py:meth:`pyforest.binary_trees.binary_tree.BinaryTree.get_min`.
        """
        if node:
            current_node = node
        else:
            if isinstance(self.root, RBNode):
                current_node = self.root
            else:
                raise tree_exceptions.EmptyTreeError()

        while isinstance(current_node.left, RBNode):
            current_node = current_node.left
        return current_node

    # Override
    def get_max(self, node: Optional[RBNode] = None) -> RBNode:
        """Return the node which has the biggest key from the subtree.

        See Also
        --------
        :py:meth:`pyforest.binary_trees.binary_tree.BinaryTree.get_max`.
        """
        if node:
            current_node = node
        else:
            if isinstance(self.root, RBNode):
                current_node = self.root
            else:
                raise tree_exceptions.EmptyTreeError()

        while isinstance(current_node.right, RBNode):
            current_node = current_node.right
        return current_node

    # Override
    def get_successor(self, node: RBNode) -> Union[RBNode, LeafNode]:
        """Return the successor node in the in-order order.

        See Also
        --------
        :py:meth:`pyforest.binary_trees.binary_tree.BinaryTree.get_successor`.
        """
        if isinstance(node.right, RBNode):
            return self.get_min(node=node.right)
        parent = node.parent
        while isinstance(parent, RBNode) and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    # Override
    def get_predecessor(self, node: RBNode) -> Union[RBNode, LeafNode]:
        """Return the predecessor node in the in-order order.

        See Also
        --------
        :py:meth:`pyforest.binary_trees.binary_tree.BinaryTree.get_predecessor`.
        """
        if isinstance(node.left, RBNode):
            return self.get_max(node=node.left)
        return node.parent

    # Override
    def get_height(self, node: Union[None, LeafNode, RBNode]) -> int:
        """Return the height of the given node.

        See Also
        --------
        :py:meth:`pyforest.binary_trees.binary_tree.BinaryTree.get_height`.
        """
        if node is None:
            return 0

        if isinstance(node.left, LeafNode) and \
           isinstance(node.right, LeafNode):
            return 0

        return max(self.get_height(node.left),
                   self.get_height(node.right)) + 1

    def inorder_traverse(self) -> binary_tree.Pairs:
        """Perform In-Order traversal.

        In-order traversal traverses a tree by the order:
        left subtree, current node, right subtree (LDR)

        Yields
        ------
        `Pairs`
            The next (key, data) pair in the in-order traversal.

        Examples
        --------
        >>> from pyforest.binary_trees import red_black_tree
        >>> tree = red_black_tree.RBTree()
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
        >>> [item for item in tree.preorder_traverse()]
        [(1, '1'), (4, '4'), (7, '7'), (11, '11'), (15, '15'), (20, '20'),
        (22, '22'), (23, '23'), (24, '24'), (30, '30'), (34, '34')]
        """
        return self._inorder_traverse(node=self.root)

    def preorder_traverse(self) -> binary_tree.Pairs:
        """Perform Pre-Order traversal.

        Pre-order traversal traverses a tree by the order:
        current node, left subtree, right subtree (DLR)

        Yields
        ------
        `Pairs`
            The next (key, data) pair in the pre-order traversal.

        Examples
        --------
        >>> from pyforest.binary_trees import red_black_tree
        >>> tree = red_black_tree.RBTree()
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
        >>> [item for item in tree.preorder_traverse()]
        [(20, "20"), (7, "7"), (4, "4"), (1, "1"), (11, "11"), (15, "15"),
        (23, "23"), (22, "22"), (30, "30"), (24, "24"), (34, "34")]
        """
        return self._preorder_traverse(node=self.root)

    def postorder_traverse(self) -> binary_tree.Pairs:
        """Perform Post-Order traversal.

        Post-order traversal traverses a tree by the order:
        left subtree, right subtree, current node (LRD)

        Yields
        ------
        `Pairs`
            The next (key, data) pair in the post-order traversal.

        Examples
        --------
        >>> from pyforest.binary_trees import red_black_tree
        >>> tree = red_black_tree.RBTree()
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
        >>> [item for item in tree.postorder_traverse()]
        [(1, "1"), (4, "4"), (15, "15"), (11, "11"), (7, "7"), (22, "22"),
        (24, "24"), (34, "34"), (30, "30"), (23, "23"), (20, "20")]
        """
        return self._postorder_traverse(node=self.root)

    def _left_rotate(self, node: Union[RBNode, LeafNode]):
        temp = node.right
        node.right = temp.left
        if isinstance(temp.left, RBNode):
            temp.left.parent = node
        temp.parent = node.parent

        if isinstance(node.parent, LeafNode):
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp

        temp.left = node
        node.parent = temp

    def _right_rotate(self, node: Union[RBNode, LeafNode]):
        temp = node.left
        node.left = temp.right
        if isinstance(temp.right, RBNode):
            temp.right.parent = node
        temp.parent = node.parent

        if isinstance(node.parent, LeafNode):
            self.root = temp
        elif node == node.parent.right:
            node.parent.right = temp
        else:
            node.parent.left = temp

        temp.right = node
        node.parent = temp

    def _insert_fixup(self, fixing_node: RBNode):
        while fixing_node.parent.color == Color.Red:
            if fixing_node.parent == fixing_node.parent.parent.left:
                temp = fixing_node.parent.parent.right
                if temp.color == Color.Red:
                    fixing_node.parent.color = Color.Black
                    temp.color = Color.Black
                    fixing_node.parent.parent.color = Color.Red
                    fixing_node = fixing_node.parent.parent
                else:
                    if fixing_node == fixing_node.parent.right:
                        fixing_node = fixing_node.parent
                        self._left_rotate(fixing_node)
                    fixing_node.parent.color = Color.Black
                    fixing_node.parent.parent.color = Color.Red
                    self._right_rotate(fixing_node.parent.parent)
            else:
                temp = fixing_node.parent.parent.left
                if temp.color == Color.Red:
                    fixing_node.parent.color = Color.Black
                    temp.color = Color.Black
                    fixing_node.parent.parent.color = Color.Red
                    fixing_node = fixing_node.parent.parent
                else:
                    if fixing_node == fixing_node.parent.left:
                        fixing_node = fixing_node.parent
                        self._right_rotate(fixing_node)
                    fixing_node.parent.color = Color.Black
                    fixing_node.parent.parent.color = Color.Red
                    self._left_rotate(fixing_node.parent.parent)

        self.root.color = Color.Black

    def _delete_fixup(self, fixing_node: RBNode):
        while (fixing_node is not self.root) and \
              (fixing_node.color == Color.Black):
            if fixing_node == fixing_node.parent.left:
                sibling = fixing_node.parent.right

                # Case 1: the sibling is red.
                if sibling.color == Color.Red:
                    sibling.color == Color.Black
                    fixing_node.parent.color = Color.Red
                    self._left_rotate(fixing_node.parent)
                    sibling = fixing_node.parent.right

                # Case 2: the sibling is black and its children are black.
                if (sibling.left.color == Color.Black) and \
                   (sibling.right.color == Color.Black):
                   sibling.color = Color.Red
                   fixing_node = fixing_node.parent # new fixing node

                # Cases 3 and 4: the sibling is black and one of
                # its child is red and the other is black.
                else:
                    # Case 3: the sibling is black and its left child is red.
                    if sibling.right.color == Color.Black:
                        sibling.left.color = Color.Black
                        sibling.color = Color.Red
                        self._right_rotate(node=sibling)

                    # Case 4: the sibling is black and its right child is red.
                    sibling.color = fixing_node.parent.color
                    fixing_node.parent.color = Color.Black
                    sibling.right.color = Color.Black
                    self._left_rotate(node=fixing_node.parent)
                    fixing_node = self.root
            else:
                sibling = fixing_node.parent.left
                if sibling.color == Color.Red:
                    sibling.color == Color.Black
                    fixing_node.parent.color = Color.Red
                    self._right_rotate(node=fixing_node.parent)
                    sibling = fixing_node.parent.left
                if (sibling.right.color == Color.Black) and \
                   (sibling.left.color == Color.Black):
                   sibling.color = Color.Red
                   fixing_node = fixing_node.parent
                else:
                    if sibling.left.color == Color.Black:
                        sibling.right.color = Color.Black
                        sibling.color = Color.Red
                        self._left_rotate(node=sibling)
                    sibling.color = fixing_node.parent.color
                    fixing_node.parent.color = Color.Black
                    sibling.left.color = Color.Black
                    self._right_rotate(node=fixing_node.parent)
                    fixing_node = self.root

        fixing_node.color = Color.Black

    def _transplant(self, deleting_node: RBNode,
                    replacing_node: Union[RBNode, LeafNode]):
        if isinstance(deleting_node.parent, LeafNode):
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node

        replacing_node.parent = deleting_node.parent

    def _inorder_traverse(self, node: Union[RBNode, LeafNode]):
        if isinstance(node, RBNode):
            yield from self._inorder_traverse(node.left)
            yield (node.key, node.data)
            yield from self._inorder_traverse(node.right)

    def _preorder_traverse(self, node: Union[RBNode, LeafNode]):
        if isinstance(node, RBNode):
            yield (node.key, node.data)
            yield from self._preorder_traverse(node.left)
            yield from self._preorder_traverse(node.right)

    def _postorder_traverse(self, node: Union[RBNode, LeafNode]):
        if isinstance(node, RBNode):
            yield from self._postorder_traverse(node.left)
            yield from self._postorder_traverse(node.right)
            yield (node.key, node.data)
