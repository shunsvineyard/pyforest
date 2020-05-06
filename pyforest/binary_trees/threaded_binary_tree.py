# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""Threaded Binary Tree module.

Threaded binary tree is a binary search tree variant that optimize traversal
in a particular order by making all right child of leaf nodes pointer to
their in-order successor of the node (if it exists). There are two types
of threaded binary tree:
- Single Threaded
- Double Threaded
"""

from dataclasses import dataclass
from typing import Any, Generic, Optional

from pyforest.binary_trees import binary_tree


@dataclass
class SingleThreadNode(binary_tree.Node, Generic[binary_tree.KeyType]):
    left: Optional["SingleThreadNode"] = None
    right: Optional["SingleThreadNode"] = None
    parent: Optional["SingleThreadNode"] = None
    isThread: bool = False


@dataclass
class DoubleThreadNode(binary_tree.Node, Generic[binary_tree.KeyType]):
    left: Optional["DoubleThreadNode"] = None
    right: Optional["DoubleThreadNode"] = None
    parent: Optional["DoubleThreadNode"] = None
    leftThread: bool = False
    rightThread: bool = False


class RightThreadedBinaryTree(binary_tree.BinaryTree):
    """Threaded Binary Tree."""

    def __init__(self, key: binary_tree.KeyType = None, data: Any = None):
        binary_tree.BinaryTree.__init__(self)
        if key and data:
            self.root: Optional[SingleThreadNode] = \
                SingleThreadNode(key=key, data=data)

    # Override
    def insert(self, key: Any, data: Any):
        """See :func:`~binary_tree.BinaryTree.insert`."""
        node = SingleThreadNode(key=key, data=data)
        if self.root is None:
            self.root = node
        else:

            temp = self.root

            while temp:
                # Move to left subtree
                if node.key < temp.key:
                    if temp.left:
                        temp = temp.left
                        continue
                    else:
                        temp.left = node
                        node.right = temp
                        node.isThread = True
                        node.parent = temp
                        break
                # Move to right subtree
                elif node.key > temp.key:
                    if temp.isThread is False and temp.right:
                        temp = temp.right
                        continue
                    else:
                        node.right = temp.right
                        temp.right = node
                        node.isThread = temp.isThread
                        temp.isThread = False
                        node.parent = temp
                        break
                else:
                    raise ValueError("Duplicate key")

    # Override
    def delete(self, key: binary_tree.KeyType):
        """See :func:`~binary_tree.BinaryTree.delete`."""
        if self.root:
            deleting_node = self._recursive_search(key=key, node=self.root)

            # The deleting node has no child
            if deleting_node.left is None and deleting_node.isThread:
                self._transplant(deleting_node=deleting_node,
                                 replacing_node=None)

            # The deleting node has only one right child
            elif deleting_node.left is None and deleting_node.isThread is False:
                self._transplant(deleting_node=deleting_node,
                                 replacing_node=deleting_node.right)

            # The deleting node has only one left child,
            elif deleting_node.left and deleting_node.isThread:
                predecessor = \
                    binary_tree.BinaryTree._get_predecessor(self,
                                                            node=deleting_node)
                if predecessor:
                    predecessor.right = deleting_node.right
                self._transplant(deleting_node=deleting_node,
                                 replacing_node=deleting_node.left)

            # The deleting node has two children
            else:
                predecessor = \
                    binary_tree.BinaryTree._get_predecessor(self,
                                                            node=deleting_node)

                min_node: SingleThreadNode = \
                    binary_tree.BinaryTree._get_min(self,
                                                    node=deleting_node.right)

                # the minmum node is not the direct child of the deleting node
                if min_node.parent != deleting_node:
                    if min_node.isThread:
                        self._transplant(deleting_node=min_node,
                                         replacing_node=None)
                    else:
                        self._transplant(deleting_node=min_node,
                                         replacing_node=min_node.right)
                    min_node.right = deleting_node.right
                    min_node.right.parent = min_node
                    #min_node.isThread = False

                self._transplant(deleting_node=deleting_node,
                                 replacing_node=min_node)
                min_node.left = deleting_node.left
                min_node.left.parent = min_node
                if predecessor:
                    predecessor.right = min_node

    def inorder_traverse(self) -> binary_tree.Pairs:
        current = self._get_leftmost(node=self.root)
        while current:
            yield (current.key, current.data)

            if current.isThread:
                current = current.right
            else:
                current = self._get_leftmost(current.right)

    def preorder_traverse(self) -> binary_tree.Pairs:
        current = self.root
        while current:
            yield (current.key, current.data)

            if current.isThread:
                current = current.right.right
            else:
                current = current.left

    # Override
    def _get_successor(self,
                       node: SingleThreadNode) -> Optional[SingleThreadNode]:
        if node.isThread:
            return node.right
        else:
            return self._get_leftmost(node=node.right)

    # Override
    def _recursive_search(self, key: binary_tree.KeyType,
                          node: SingleThreadNode) -> SingleThreadNode:
        if key == node.key:
            return node
        elif key < node.key:
            if node.left:
                return self._recursive_search(key=key, node=node.left)
            else:
                raise KeyError(f"Key {key} not found")
        else:  # key > node.key
            if node.right and node.isThread is False:
                return self._recursive_search(key=key, node=node.right)
            else:
                raise KeyError(f"Key {key} not found")

    # Override
    def _iterative_search(self, key: binary_tree.KeyType) -> SingleThreadNode:
        current = self.root

        while current and current.isThread is False:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:  # key > current.key
                if current.isThread is False:
                    current = current.right
        raise KeyError(f"Key {key} not found")

    # Override
    def _get_max(self, node: SingleThreadNode) -> SingleThreadNode:
        current_node = node
        while current_node.isThread is False and current_node.right:
            current_node = current_node.right
        return current_node

    def _get_leftmost(self, node: Optional[SingleThreadNode]):

        if node is None:
            return None

        while node.left:
            node = node.left
        return node

    def _transplant(self, deleting_node: SingleThreadNode,
                    replacing_node: Optional[SingleThreadNode]):
        if deleting_node.parent is None:
            self.root = replacing_node
            if self.root:
                self.root.isThread = False
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
            if replacing_node:
                if replacing_node.isThread:
                    replacing_node.right = deleting_node.parent
        else:  # deleting_node == deleting_node.parent.right
            deleting_node.parent.right = replacing_node
            if replacing_node:
                if replacing_node.isThread:
                    if replacing_node == deleting_node.left:
                        replacing_node.right = deleting_node.right
            else:  # replacing_node is None
                deleting_node.parent.right = deleting_node.right
                deleting_node.parent.isThread = True

        if replacing_node:
            replacing_node.parent = deleting_node.parent


class LeftThreadedBinaryTree(binary_tree.BinaryTree):
    """Threaded Binary Tree."""

    def __init__(self, key: binary_tree.KeyType = None, data: Any = None):
        binary_tree.BinaryTree.__init__(self)
        if key and data:
            self.root: SingleThreadNode = SingleThreadNode(key=key, data=data)

    # Override
    def insert(self, key: Any, data: Any):

        node = SingleThreadNode(key=key, data=data)
        if self.root is None:
            self.root = node
        else:

            temp = self.root

            while temp:
                # Move to right subtree
                if node.key > temp.key:
                    if temp.right:
                        temp = temp.right
                        continue
                    else:
                        temp.right = node
                        node.left = temp
                        node.isThread = True
                        node.parent = temp
                        break
                # Move to left subtree
                elif node.key < temp.key:
                    if temp.isThread is False and temp.left:
                        temp = temp.left
                        continue
                    else:
                        node.left = temp.left
                        temp.left = node
                        temp.isThread = False
                        node.isThread = True
                        node.parent = temp
                        break
                else:
                    raise ValueError("Duplicate key")

    # Override
    def delete(self, value):
        pass

    def outorder_traverse(self) -> binary_tree.Pairs:

        current = self._get_rightmost(node=self.root)
        while current:
            yield (current.key, current.data)

            if current.isThread:
                current = current.left
            else:
                current = self._get_rightmost(current.left)

    # Override
    def _get_predecessor(self,
                         node: SingleThreadNode) -> Optional[SingleThreadNode]:
        if node.isThread:
            return node.left
        else:
            return self._get_rightmost(node=node.right)

    def _get_rightmost(self, node: Optional[SingleThreadNode]):

        if node is None:
            return None

        while node.right:
            node = node.right
        return node


class DoubleThreadedBinaryTree(binary_tree.BinaryTree):
    """Threaded Binary Tree."""

    def __init__(self, key: binary_tree.KeyType = None, data: Any = None):
        binary_tree.BinaryTree.__init__(self)
        if key and data:
            self.root: DoubleThreadNode = DoubleThreadNode(key=key, data=data)

    # Override
    def insert(self, key: Any, data: Any):
        node = DoubleThreadNode(key=key, data=data)
        if self.root is None:
            self.root = node
        else:

            temp = self.root

            while temp:
                # Move to left subtree
                if node.key < temp.key:
                    if temp.leftThread is False and temp.left:
                        temp = temp.left
                        continue
                    else:
                        node.left = temp.left
                        temp.left = node
                        node.right = temp
                        temp.leftThread = False
                        node.leftThread = True
                        node.rightThread = True
                        node.parent = temp
                        break
                # Move to right subtree
                elif node.key > temp.key:
                    if temp.rightThread is False and temp.right:
                        temp = temp.right
                        continue
                    else:
                        node.right = temp.right
                        temp.right = node
                        node.left = temp
                        temp.rightThread = False
                        node.leftThread = True
                        node.rightThread = True
                        node.parent = temp
                        break
                else:
                    raise ValueError("Duplicate key")

    # Override
    def delete(self, value):
        pass

    def inorder_traverse(self) -> binary_tree.Pairs:

        current = self._get_leftmost(node=self.root)
        while current:
            yield (current.key, current.data)

            if current.rightThread:
                current = current.right
            else:
                current = self._get_leftmost(current.right)

    def outorder_traverse(self) -> binary_tree.Pairs:

        current = self._get_rightmost(node=self.root)
        while current:
            yield (current.key, current.data)

            if current.leftThread:
                current = current.left
            else:
                current = self._get_rightmost(current.left)

    def _get_leftmost(self, node: DoubleThreadNode):

        if node is None:
            return None

        while node.leftThread is False:
            node = node.left
        return node

    def _get_rightmost(self, node: DoubleThreadNode):

        if node is None:
            return None

        while node.rightThread is False:
            node = node.right
        return node




if __name__ == "__main__":

    test = RightThreadedBinaryTree()
    test.insert(23, "23")
    test.insert(4, "4")
    test.insert(30, "30")
    test.insert(11, "11")
    test.insert(7, "7")
    test.insert(34, "34")
    test.insert(20, "20")
    test.insert(24, "24")
    test.insert(22, "22")
    test.insert(15, "15")
    test.insert(1, "1")

    for item in test.preorder_traverse():
        print(item)

    #test.delete(11)
    #test.delete(30)
    #test.delete(4)
    #test.delete(15)
    #test.delete(22)
    #test.delete(11)
    #test.delete(20)

    #for item in test.inorder_traverse():
    #    print(item)

    """
    test = LeftThreadedBinaryTree()
    test.insert(23, "23")
    test.insert(4, "4")
    test.insert(30, "30")
    test.insert(11, "11")
    test.insert(7, "7")
    test.insert(34, "34")
    test.insert(20, "20")
    test.insert(24, "24")
    test.insert(22, "22")
    test.insert(15, "15")
    test.insert(1, "1")

    for item in test.outorder_traverse():
        print(item)

    test = DoubleThreadedBinaryTree()
    test.insert(23, "23")
    test.insert(4, "4")
    test.insert(30, "30")
    test.insert(11, "11")
    test.insert(7, "7")
    test.insert(34, "34")
    test.insert(20, "20")
    test.insert(24, "24")
    test.insert(22, "22")
    test.insert(15, "15")
    test.insert(1, "1")

    for item in test.outorder_traverse():
        print(item)

    for item in test.inorder_traverse():
        print(item)
    """