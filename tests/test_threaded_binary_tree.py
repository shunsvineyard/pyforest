"""Unit tests for the threaded binary search trees module."""

import pytest

from pyforest.binary_trees import threaded_binary_tree


def test_simple_right_threaded_case(basic_tree):
    """Test the basic opeartions of a right threaded binary search tree."""
    tree = threaded_binary_tree.RightThreadedBinaryTree()

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    output = ["1", "4", "7", "11", "15", "20", "22", "23", "24", "30", "34"]
    index = 0
    for data in tree.inorder_traverse():
        assert data == output[index]
        index += 1

def test_simple_left_threaded_case(basic_tree):
    """Test the basic opeartions of a left threaded binary search tree."""
    tree = threaded_binary_tree.LeftThreadedBinaryTree()

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    output = ["34", "30", "24", "23", "22", "20", "15", "11", "7", "4", "1"]
    index = 0
    for data in tree.outorder_traverse():
        assert data == output[index]
        index += 1

def test_simple_double_threaded_case(basic_tree):
    """Test the basic opeartions of a double threaded binary search tree."""
    tree = threaded_binary_tree.DoubleThreadedBinaryTree()

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    outorder_output = ["34", "30", "24", "23", "22", "20", "15", "11", "7", "4", "1"]
    index = 0
    for data in tree.outorder_traverse():
        assert data == outorder_output[index]
        index += 1

    inorder_output = ["1", "4", "7", "11", "15", "20", "22", "23", "24", "30", "34"]
    index = 0
    for data in tree.inorder_traverse():
        assert data == inorder_output[index]
        index += 1
