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

from typing import Any, List, NoReturn, Tuple

from pyforest.binary_trees import _base_tree


def _inorder_traverse(node: _base_tree.Node, output: List[Tuple[Any, Any]]):
    """Perform In-Order traversal.

    Parameters
    ----------
    node : _base_tree.Node
        The root of the binary tree.

    output : list(tuple())
        The result of the traversal. This is an output parameter.
    """
    if node:
        _inorder_traverse(node.left, output)
        output.append((node.key, node.data))
        _inorder_traverse(node.right, output)


def _inorder_traverse_non_recursive(
        root: _base_tree.Node) -> List[Tuple[Any, Any]]:
    return []


def _outorder_traverse(node: _base_tree.Node, output: List[Tuple[Any, Any]]):
    """Perform Output-Order traversal.

    Parameters
    ----------
    node : _base_tree.Node
        The root of the binary tree.

    output : list(tuple())
        The result of the traversal. This is an output parameter.
    """
    if node:
        _outorder_traverse(node.right, output)
        output.append((node.key, node.data))
        _outorder_traverse(node.left, output)


def _outorder_traverse_non_recursive(
        root: _base_tree.Node) -> List[Tuple[Any, Any]]:
    return []


def _preorder_traverse(node: _base_tree.Node, output: List[Tuple[Any, Any]]):
    """Perform Pre-Order traversal.

    Parameters
    ----------
    node : _base_tree.Node
        The root of the binary tree.

    output : list(tuple())
        The result of the traversal. This is an output parameter.
    """
    if node:
        output.append((node.key, node.data))
        _preorder_traverse(node.left, output)
        _preorder_traverse(node.right, output)


def _preorder_traverse_non_recursive(
        root: _base_tree.Node) -> List[Tuple[Any, Any]]:
    return []


def _postorder_traverse(node: _base_tree.Node, output: List[Tuple[Any, Any]]):
    """Perform Post-Order traversal.

    Parameters
    ----------
    node : _base_tree.Node
        The root of the binary tree.

    output : list(tuple())
        The result of the traversal. This is an output parameter.
    """
    if node:
        _postorder_traverse(node.left, output)
        _postorder_traverse(node.right, output)
        output.append((node.key, node.data))


def _postorder_traverse_non_recursive(
        root: _base_tree.Node) -> List[Tuple[Any, Any]]:
    pass


def inorder_traverse(tree: _base_tree.BaseTree,
                     recursive: bool = True) -> List[Tuple[Any, Any]]:
    """Perform In-Order traversal.

    In-order traversal traverses a tree by the order:
    left subtree, current node, right subtree (LDR)

    Parameters
    ----------
    tree : _base_tree.BaseTree
        A type of binary tree.
    """
    if recursive:
        output: List[Tuple[Any, Any]] = []
        _inorder_traverse(node=tree.root, output=output)
        return output

    return _inorder_traverse_non_recursive(root=tree.root)


def outorder_traverse(tree: _base_tree.BaseTree,
                      recursive: bool = True) -> List[Tuple[Any, Any]]:
    """Perform Out-Order traversal.

    Out-order traversal traverses a tree by the order:
    right subtree, current node, left subtree (RNL)

    Parameters
    ----------
    tree : _base_tree.BaseTree
        A type of binary tree.
    """
    if recursive:
        output: List[Tuple[Any, Any]] = []
        _outorder_traverse(node=tree.root, output=output)
        return output

    return _outorder_traverse_non_recursive(root=tree.root)


def preorder_traverse(tree: _base_tree.BaseTree,
                      recursive: bool = True) -> List[Tuple[Any, Any]]:
    """Perform Pre-Order traversal.

    Pre-order traversal traverses a tree by the order:
    current node, left subtree, right subtree (DLR)

    Parameters
    ----------
    tree : _base_tree.BaseTree
        A type of binary tree.
    """
    if recursive:
        output: List[Tuple[Any, Any]] = []
        _preorder_traverse(node=tree.root, output=output)
        return output

    return _preorder_traverse_non_recursive(root=tree.root)


def postorder_traverse(tree: _base_tree.BaseTree,
                       recursive: bool = True) -> List[Tuple[Any, Any]]:
    """Perform Post-Order traversal.
    Post-order traversal traverses a tree by the order:
    left subtree, right subtree, current node (LRD)

    Parameters
    ----------
    tree : _base_tree.BaseTree
        A type of binary tree.
    """
    if recursive:
        output: List[Tuple[Any, Any]] = []
        _postorder_traverse(node=tree.root, output=output)
        return output

    return _postorder_traverse_non_recursive(root=tree.root)


def levelorder_traverse(tree: _base_tree.BaseTree) -> List[Tuple[Any, Any]]:
    """Perform Level-Order traversal.

    Level-order traversal traverses a tree:
    level by level, from left to right, starting from the root node.

    Parameters
    ----------
    root : _base_tree.BaseTree
        The root of a type of binary tree.
    """
    queue = [tree.root]
    output = []

    while len(queue) > 0:
        temp = queue.pop(0)
        output.append((temp.key, temp.data))
        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

    return output
