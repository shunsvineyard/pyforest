# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""Binary tree traversal.

Routines
--------
inorder_traverse(tree: _base_tree.BaseTree) -> NoReturn
    Perform in-order traversal.

preorder_traverse(tree: _base_tree.BaseTree) -> NoReturn
    Perform pre-order traversal.

postorder_traverse(tree: _base_tree.BaseTree) -> NoReturn
    Perform post-order traversal.

levelorder_traverse(tree: _base_tree.BaseTree) -> NoReturn
    Perform level order traversal.
"""

from typing import NoReturn

from pyforest.binary_trees import _base_tree

def _inorder_traverse(node: _base_tree.Node, output: list) -> NoReturn:
    """Perform In-Order traversal.

    Parameters
    ----------
    node : _base_tree.Node
        The root of the binary tree.
    """
    if node:
        _inorder_traverse(node.left)
        print(node.data, end=" ")
        output.append(node.data)
        _inorder_traverse(node.right)

def _preorder_traverse(node: _base_tree.Node, output: list) -> NoReturn:
    """Perform Pre-Order traversal.

    Parameters
    ----------
    node : _base_tree.Node
        The root of the binary tree.
    """
    if node:
        print(node.data, end=" ")
        output.append(node.data)
        _preorder_traverse(node.left)
        _preorder_traverse(node.right)

def _postorder_traverse(node: _base_tree.Node, output: list) -> NoReturn:
    """Perform Post-Order traversal.

    Parameters
    ----------
    node : _base_tree.Node
        The root of the binary tree.
    """
    if node:
        _postorder_traverse(node.left)
        _postorder_traverse(node.right)
        print(node.data, end=" ")
        output.append(node.data)

def inorder_traverse(tree: _base_tree.BaseTree) -> list:
    """Perform In-Order traversal.
    In-order traversal traverses a tree by the order:
    left subtree, current node, right subtree (LDR)
    
    Parameters
    ----------
    tree : _base_tree.BaseTree
        A type of binary tree.
    """
    output = list()
    _inorder_traverse(node=tree.root, output=output)
    return output

def preorder_traverse(tree: _base_tree.BaseTree) -> list:
    """Perform Pre-Order traversal.
    Pre-order traversal traverses a tree by the order:
    current node, left subtree, right subtree (DLR)
    
    Parameters
    ----------
    tree : _base_tree.BaseTree
        A type of binary tree.
    """
    output = list()
    _preorder_traverse(node=tree.root, output=output)
    return output

def postorder_traverse(tree: _base_tree.BaseTree) -> list:
    """Perform Post-Order traversal.
    Post-order traversal traverses a tree by the order:
    left subtree, right subtree, current node (LRD)

    Parameters
    ----------
    tree : _base_tree.BaseTree
        A type of binary tree.
    """
    output = list()
    _postorder_traverse(node=tree.root, output=output)
    return output

def levelorder_traverse(tree: _base_tree.BaseTree) -> list:
    """Perform Level-Order traversal.
    Level-order traversal traverses a tree:
    level by level, from left to right, starting from the root node.

    Parameters
    ----------
    root : _base_tree.BaseTree
        The root of a type of binary tree.
    """
    queue = [tree.root]
    output = list()

    while len(queue) > 0:
        temp = queue.pop(0)
        print(temp.data, end=" ")
        output.append(temp.data)
        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

    return output
