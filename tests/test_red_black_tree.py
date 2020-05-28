"""Unit tests for the red black tree module."""

import pytest

from pyforest import tree_exceptions

from pyforest.binary_trees import red_black_tree


def test_simple_case(basic_tree):
    """Test the basic operations of a red black tree."""
    tree = red_black_tree.RBTree()

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    assert tree.get_min() == 1
    assert tree.search(24) == "24"

    tree.delete(15)

    with pytest.raises(tree_exceptions.KeyNotFoundError):
        tree.search(15)


def test_deletion(basic_tree):
    """Test the deletion of a red black tree."""
    tree = red_black_tree.RBTree()

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    # No child
    tree.delete(15)
    assert [item for item in tree.inorder_traverse()] == [
        (1, "1"), (4, "4"), (7, "7"), (11, "11"), (20, "20"),
        (22, "22"), (23, "23"), (24, "24"), (30, "30"), (34, "34")
    ]

    # One right child
    tree.delete(20)
    assert [item for item in tree.inorder_traverse()] == [
        (1, "1"), (4, "4"), (7, "7"), (11, "11"), (22, "22"),
        (23, "23"), (24, "24"), (30, "30"), (34, "34")
    ]

    # One left child
    tree.insert(key=17, data="17")
    tree.delete(22)
    assert [item for item in tree.inorder_traverse()] == [
        (1, "1"), (4, "4"), (7, "7"), (11, "11"), (17, "17"),
        (23, "23"), (24, "24"), (30, "30"), (34, "34")
    ]

    # Two children
    tree.delete(11)
    assert [item for item in tree.inorder_traverse()] == [
        (1, "1"), (4, "4"), (7, "7"), (17, "17"),
        (23, "23"), (24, "24"), (30, "30"), (34, "34")
    ]
