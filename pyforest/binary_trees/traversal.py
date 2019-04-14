# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

from pyforest.binary_trees import _base_tree

def inorder_traverse(node: _base_tree.BaseTree):
    """Perform In-Order traversal.
    In-order traversal traverses a tree by the order:
    left subtree, current node, right subtree (LDR)
    
    Parameters
    ----------
    node : _base_tree.BaseTree
        The root of a type of binary tree.
    """
    if node:
        inorder_traverse(node.left)
        print(node.data, end=" ")
        inorder_traverse(node.right)

def preorder_traverse(node: _base_tree.BaseTree):
    """Perform Pre-Order traversal.
    Pre-order traversal traverses a tree by the order:
    current node, left subtree, right subtree (DLR)
    
    Parameters
    ----------
    node : _base_tree.BaseTree
        The root of a type of binary tree.
    """
    if node:
        print(node.data, end=" ")
        preorder_traverse(node.left)
        preorder_traverse(node.right)

def postorder_traverse(node: _base_tree.BaseTree):
    """Perform Post-Order traversal.
    Post-order traversal traverses a tree by the order:
    left subtree, right subtree, current node (LRD)

    Parameters
    ----------
    node : _base_tree.BaseTree
        The root of a type of binary tree.
    """
    if node:
        postorder_traverse(node.left)
        postorder_traverse(node.right)
        print(node.data, end=" ")

def levelorder_traverse(root: _base_tree.BaseTree):
    """Perform Level-Order traversal.
    Level-order traversal traverses a tree:
    level by level, from left to right, starting from the root node.

    Parameters
    ----------
    root : _base_tree.BaseTree
        The root of a type of binary tree.
    """
    queue = [root]

    while len(queue) > 0:
        temp = queue.pop(0)
        print(temp.data, end=" ")

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

