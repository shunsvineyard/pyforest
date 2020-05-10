# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""Binary tree traversal.

Routines
--------
inorder_traverse(tree: base_tree.TreeType) -> NoReturn
    Perform in-order traversal.

preorder_traverse(tree: base_tree.TreeType) -> NoReturn
    Perform pre-order traversal.

postorder_traverse(tree: base_tree.TreeType) -> NoReturn
    Perform post-order traversal.

levelorder_traverse(tree: base_tree.TreeType) -> NoReturn
    Perform level order traversal.
"""

from typing import Optional

from pyforest.binary_trees import binary_tree


# Alias for the base node type.
NodeType = Optional[binary_tree.Node]


def _inorder_traverse(node: NodeType) -> binary_tree.Pairs:
    """Perform In-Order traversal.

    Parameters
    ----------
    node : NodeType
        The root of the binary tree.
    """
    if node:
        yield from _inorder_traverse(node.left)
        yield (node.key, node.data)
        yield from _inorder_traverse(node.right)


def _inorder_traverse_non_recursive(root: NodeType) -> binary_tree.Pairs:
    """Perform In-Order traversal without recursive.

    Parameters
    ----------
    root : NodeType
        The root of the binary tree.

    Returns
    -------
    List(Tuple())
        The result of the traversal.
    """

    if root is None:
        raise StopIteration

    stack = []
    if root.right:
        stack.append(root.right)
        stack.append(root)

    current = root.left

    while True:

        if current:
            if current.right:
                stack.append(current.right)
                stack.append(current)
                current = current.left
                continue
            stack.append(current)
            current = None

        else:  # current is None

            if len(stack) > 0:
                current = stack.pop()

                if current.right is None:
                    yield (current.key, current.data)
                    current = None
                    continue
                else:  # current.right is not None
                    if len(stack) > 0:
                        if current.right == stack[-1]:
                            yield (current.key, current.data)
                            current = None
                            continue
                        else:  # current.right != stack[-1]:
                            # This case means there are more nodes on the right
                            # Keep the current and go back to add them.
                            continue

            else:  # stack is empty
                break


def _outorder_traverse(node: NodeType) -> binary_tree.Pairs:
    """Perform Output-Order traversal.

    Parameters
    ----------
    node : NodeType
        The root of the binary tree.
    """
    if node:
        yield from _outorder_traverse(node.right)
        yield (node.key, node.data)
        yield from _outorder_traverse(node.left)


def _outorder_traverse_non_recursive(root: NodeType) -> binary_tree.Pairs:
    """Perform Out-Order traversal without recursive.

    Parameters
    ----------
    root : NodeType
        The root of the binary tree.

    Returns
    -------
    List(Tuple())
        The result of the traversal.
    """
    if root is None:
        raise StopIteration

    stack = []
    if root.left:
        stack.append(root.left)
        stack.append(root)

    current = root.right

    while True:

        if current:
            if current.left:
                stack.append(current.left)
                stack.append(current)
                current = current.right
                continue
            stack.append(current)
            current = None

        else:  # current is None

            if len(stack) > 0:
                current = stack.pop()

                if current.left is None:
                    yield (current.key, current.data)
                    current = None
                    continue
                else:  # current.right is not None
                    if len(stack) > 0:
                        if current.left == stack[-1]:
                            yield (current.key, current.data)
                            current = None
                            continue
                        else:  # current.right != stack[-1]:
                            # This case means there are more nodes on the right
                            # Keep the current and go back to add them.
                            continue

            else:  # stack is empty
                break


def _preorder_traverse(node: NodeType) -> binary_tree.Pairs:
    """Perform Pre-Order traversal.

    Parameters
    ----------
    node : NodeType
        The root of the binary tree.
    """
    if node:
        yield (node.key, node.data)
        yield from _preorder_traverse(node.left)
        yield from _preorder_traverse(node.right)


def _preorder_traverse_non_recursive(root: NodeType) -> binary_tree.Pairs:
    """Perform Pre-Order traversal without recursive.

    Parameters
    ----------
    root : NodeType
        The root of the binary tree.

    Returns
    -------
    List(Tuple())
        The result of the traversal.
    """
    if root is None:
        raise StopIteration

    stack = [root]

    while len(stack) > 0:
        temp = stack.pop()
        yield (temp.key, temp.data)

        # Because stack is FILO, insert right child before left child.
        if temp.right:
            stack.append(temp.right)

        if temp.left:
            stack.append(temp.left)


def _postorder_traverse(node: NodeType) -> binary_tree.Pairs:
    """Perform Post-Order traversal.

    Parameters
    ----------
    node : NodeType
        The root of the binary tree.

    output : List(Tuple())
        The result of the traversal. This is an output parameter.
    """
    if node:
        yield from _postorder_traverse(node.left)
        yield from _postorder_traverse(node.right)
        yield (node.key, node.data)


def _postorder_traverse_non_recursive(root: NodeType) -> binary_tree.Pairs:
    """Perform Post-Order traversal without recursive.

    Parameters
    ----------
    root : NodeType
        The root of the binary tree.

    Returns
    -------
    List(Tuple())
        The result of the traversal.
    """
    if root is None:
        raise StopIteration

    stack = []
    if root.right:
        stack.append(root.right)

    stack.append(root)
    current = root.left

    while True:

        if current:
            if current.right:
                stack.append(current.right)
                stack.append(current)
                current = current.left
                continue
            else:  # current.right is None
                yield (current.key, current.data)
                current = None

        else:  # current is None
            if len(stack) > 0:
                current = stack.pop()

                if current.right is None:
                    yield (current.key, current.data)
                    current = None
                else:  # current.right is not None
                    if len(stack) > 0:
                        if current.right != stack[-1]:
                            yield (current.key, current.data)
                            current = None
                        else:  # current.right == stack[-1]
                            temp = stack.pop()
                            stack.append(current)
                            current = temp

                    else:  # stack is empty
                        yield (current.key, current.data)
                        break


def inorder_traverse(tree: binary_tree.TreeType,
                     recursive: bool = True) -> binary_tree.Pairs:
    """Perform In-Order traversal.

    In-order traversal traverses a tree by the order:
    left subtree, current node, right subtree (LDR)

    Parameters
    ----------
    tree : binary_tree.TreeType
        A type of binary tree.

    Examples
    --------
    >>> from pyforest.binary_trees import binary_search_tree
    >>> from pyforest.binary_trees import traversal
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
    >>> traversal.inorder_traverse(tree)
    [(1, '1'), (4, '4'), (7, '7'), (11, '11'), (15, '15'), (20, '20'),
     (22, '22'), (23, '23'), (24, '24'), (30, '30'), (34, '34')]
    >>> traversal.inorder_traverse(tree, recursive=False)
    [(1, '1'), (4, '4'), (7, '7'), (11, '11'), (15, '15'), (20, '20'),
     (22, '22'), (23, '23'), (24, '24'), (30, '30'), (34, '34')]
    """
    if recursive:
        return _inorder_traverse(node=tree.root)

    return _inorder_traverse_non_recursive(root=tree.root)


def outorder_traverse(tree: binary_tree.TreeType,
                      recursive: bool = True) -> binary_tree.Pairs:
    """Perform Out-Order traversal.

    Out-order traversal traverses a tree by the order:
    right subtree, current node, left subtree (RNL)

    Parameters
    ----------
    tree : base_tree.TreeType
        A type of binary tree.

    Examples
    --------
    >>> from pyforest.binary_trees import binary_search_tree
    >>> from pyforest.binary_trees import traversal
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
    >>> traversal.outorder_traverse(tree)
    [(34, '34'), (30, '30'), (24, '24'), (23, '23'), (22, '22'), (20, '20'),
     (15, '15'), (11, '11'), (7, '7'), (4, '4'), (1, '1')]
    >>> traversal.outorder_traverse(tree, recursive=False)
    [(34, '34'), (30, '30'), (24, '24'), (23, '23'), (22, '22'), (20, '20'),
     (15, '15'), (11, '11'), (7, '7'), (4, '4'), (1, '1')]
    """
    if recursive:
        return _outorder_traverse(node=tree.root)

    return _outorder_traverse_non_recursive(root=tree.root)


def preorder_traverse(tree: binary_tree.TreeType,
                      recursive: bool = True) -> binary_tree.Pairs:
    """Perform Pre-Order traversal.

    Pre-order traversal traverses a tree by the order:
    current node, left subtree, right subtree (DLR)

    Parameters
    ----------
    tree : base_tree.TreeType
        A type of binary tree.

    Examples
    --------
    >>> from pyforest.binary_trees import binary_search_tree
    >>> from pyforest.binary_trees import traversal
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
    >>> traversal.preorder_traverse(tree)
    [(23, '23'), (4, '4'), (1, '1'), (11, '11'), (7, '7'), (20, '20'),
     (15, '15'), (22, '22'), (30, '30'), (24, '24'), (34, '34')]
    >>> traversal.preorder_traverse(tree, recursive=False)
    [(23, '23'), (4, '4'), (1, '1'), (11, '11'), (7, '7'), (20, '20'),
     (15, '15'), (22, '22'), (30, '30'), (24, '24'), (34, '34')]
    """
    if recursive:
        return _preorder_traverse(node=tree.root)

    return _preorder_traverse_non_recursive(root=tree.root)


def postorder_traverse(tree: binary_tree.TreeType,
                       recursive: bool = True) -> binary_tree.Pairs:
    """Perform Post-Order traversal.

    Post-order traversal traverses a tree by the order:
    left subtree, right subtree, current node (LRD)

    Parameters
    ----------
    tree : binary_tree.TreeType
        A type of binary tree.

    Examples
    --------
    >>> from pyforest.binary_trees import binary_search_tree
    >>> from pyforest.binary_trees import traversal
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
    >>> traversal.postorder_traverse(tree)
    [(1, '1'), (7, '7'), (15, '15'), (22, '22'), (20, '20'), (11, '11'),
     (4, '4'), (24, '24'), (34, '34'), (30, '30'), (23, '23')]
    >>> traversal.postorder_traverse(tree, recursive=False)
    [(1, '1'), (7, '7'), (15, '15'), (22, '22'), (20, '20'), (11, '11'),
     (4, '4'), (24, '24'), (34, '34'), (30, '30'), (23, '23')]
    """
    if recursive:
        return _postorder_traverse(node=tree.root)

    return _postorder_traverse_non_recursive(root=tree.root)


# FIXME: level order can be used for n-binary (n > 2). Should move it.
def levelorder_traverse(tree: binary_tree.TreeType) -> binary_tree.Pairs:
    """Perform Level-Order traversal.

    Level-order traversal traverses a tree:
    level by level, from left to right, starting from the root node.

    Parameters
    ----------
    tree : binary_tree.TreeType
        A type of binary tree.

    Examples
    --------
    >>> from pyforest.binary_trees import binary_search_tree
    >>> from pyforest.binary_trees import traversal
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
    >>> traversal.levelorder_traverse(tree)
    [(23, '23'), (4, '4'), (30, '30'), (1, '1'), (11, '11'), (24, '24'),
     (34, '34'), (7, '7'), (20, '20'), (15, '15'), (22, '22')]
    """
    queue = [tree.root]

    while len(queue) > 0:
        temp = queue.pop(0)
        if temp:
            yield (temp.key, temp.data)
            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)
