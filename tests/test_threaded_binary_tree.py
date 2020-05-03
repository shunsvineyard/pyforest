"""Unit tests for the threaded binary search trees module."""

import pytest

from pyforest.binary_trees import threaded_binary_tree


def test_simple_right_threaded_case(basic_tree):
    """Test the basic opeartions of a right threaded binary search tree."""
    tree = threaded_binary_tree.RightThreadedBinaryTree()

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    assert ["1", "4", "7", "11", "15", "20", "22", "23", "24", "30", "34"] == \
           [item for item in tree.inorder_traverse()]

    assert tree.get_min() == 1
    assert tree.get_max() == 34
    assert tree.search(24) == "24"

    tree.delete(15)
    tree.delete(22)
    tree.delete(7)
    tree.delete(20)

    with pytest.raises(KeyError):
        tree.search(15)

    assert ["1", "4", "11", "23", "24", "30", "34"] == \
           [item for item in tree.inorder_traverse()]


def test_deletion_right_threaded_case(basic_tree):
    """Test the deletion of a right threaded binary search tree."""
    tree = threaded_binary_tree.RightThreadedBinaryTree()

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    # No child
    tree.delete(15)
    assert ["1", "4", "7", "11", "20", "22", "23", "24", "30", "34"] == \
           [item for item in tree.inorder_traverse()]

    # One right child
    tree.delete(20)
    assert ["1", "4", "7", "11", "22", "23", "24", "30", "34"] == \
           [item for item in tree.inorder_traverse()]

    # One left child
    tree.insert(key=17, data="17")
    tree.delete(22)
    assert ["1", "4", "7", "11", "17", "23", "24", "30", "34"] == \
           [item for item in tree.inorder_traverse()]

    # Two children
    tree.delete(11)
    assert ["1", "4", "7", "17", "23", "24", "30", "34"] == \
           [item for item in tree.inorder_traverse()]


def test_simple_left_threaded_case(basic_tree):
    """Test the basic opeartions of a left threaded binary search tree."""
    tree = threaded_binary_tree.LeftThreadedBinaryTree()

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    assert ["34", "30", "24", "23", "22", "20", "15", "11", "7", "4", "1"] == \
           [item for item in tree.outorder_traverse()]


def test_simple_double_threaded_case(basic_tree):
    """Test the basic opeartions of a double threaded binary search tree."""
    tree = threaded_binary_tree.DoubleThreadedBinaryTree()

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    assert ["34", "30", "24", "23", "22", "20", "15", "11", "7", "4", "1"] == \
           [item for item in tree.outorder_traverse()]

    assert ["1", "4", "7", "11", "15", "20", "22", "23", "24", "30", "34"] == \
           [item for item in tree.inorder_traverse()]
