# Copyright © 2020 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

from pyforest.binary_trees import binary_tree
from pyforest.binary_trees import traversal


def verify_bst_properties(tree: binary_tree.BinaryTree) -> bool:

    # FIXME: WIP
    in_order_result = [item for item in traversal.inorder_traverse(tree=tree)]

    for index in range(len(in_order_result) - 1):
        if in_order_result[index] > in_order_result[index + 1]:
            return False
    return True


def check_balance(tree: binary_tree.BinaryTree) -> bool:
    if tree.root is None:
        return True
    return _is_balance(tree=tree, node=tree.root)


def _is_balance(tree: binary_tree.BinaryTree, node: binary_tree.Node) -> bool:
    left_hight = tree.get_height(node.left)
    right_height = tree.get_height(node.right)

    if (abs(left_hight - right_height) > 1):
        return False

    if node.left:
        if not _is_balance(tree, node=node.left):
            return False
    if node.right:
        if not _is_balance(tree, node=node.right):
            return False

    return True
