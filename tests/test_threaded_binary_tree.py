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

    assert tree.get_min() == 1
    assert tree.get_max() == 34
    assert tree.search(24) == "24"

    tree.delete(15)
    tree.delete(22)
    tree.delete(7)
    tree.delete(20)

    with pytest.raises(KeyError):
        tree.search(15)

    output_after_deleted = ["1", "4", "11", "23", "24", "30", "34"]
    index = 0
    for data in tree.inorder_traverse():
        assert data == output_after_deleted[index]
        index += 1


def test_deletion_right_threaded_case(basic_tree):
    """Test the deletion of a right threaded binary search tree."""
    tree = threaded_binary_tree.RightThreadedBinaryTree()

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    # No child
    tree.delete(15)
    no_child_output = ["1", "4", "7", "11", "20", "22", "23", "24", "30", "34"]
    index = 0
    for data in tree.inorder_traverse():
        assert data == no_child_output[index]
        index += 1

    # One right child
    tree.delete(20)
    one_right_child_output = ["1", "4", "7", "11", "22", "23", "24", "30", "34"]
    index = 0
    for data in tree.inorder_traverse():
        assert data == one_right_child_output[index]
        index += 1

    # One left child
    tree.insert(key=17, data="17")
    tree.delete(22)
    one_left_child_output = ["1", "4", "7", "11", "17", "23", "24", "30", "34"]
    index = 0
    for data in tree.inorder_traverse():
        assert data == one_left_child_output[index]
        index += 1

    # Two children
    tree.delete(11)
    two_children_output = ["1", "4", "7", "17", "23", "24", "30", "34"]
    index = 0
    for data in tree.inorder_traverse():
        assert data == two_children_output[index]
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
