"""Unit tests for the AVL tree module."""

import pytest

from pyforest.binary_trees import avl_tree
from pyforest.binary_trees import traversal


def test_simple_case(basic_tree):
    """Test the basic operation of a AVL tree."""
    tree = avl_tree.AVLTree()

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    assert tree.get_min() == 1
    assert tree.search(24) == "24"

    tree.delete(15)

    with pytest.raises(KeyError):
        tree.search(15)
