"""Unit tests for the traversal module."""

from pyforest.binary_trees import binary_search_tree
from pyforest.binary_trees import red_black_tree
from pyforest.binary_trees import traversal


def test_binary_search_tree_traversal(basic_tree):
    """Test binary search tree traversal."""
    tree = binary_search_tree.BinarySearchTree()

    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    assert traversal.levelorder_traverse(tree) == [
        (23, "23"), (4, "4"), (30, "30"), (1, "1"), (11, "11"), (24, "24"),
        (34, "34"), (7, "7"), (20, "20"), (15, "15"), (22, "22")
    ]

    assert traversal.postorder_traverse(tree) == [
        (1, "1"), (7, "7"), (15, "15"), (22, "22"), (20, "20"), (11, "11"),
        (4, "4"), (24, "24"), (34, "34"), (30, "30"), (23, "23")
    ]

    assert traversal.postorder_traverse(tree, recursive=False) == [
        (1, "1"), (7, "7"), (15, "15"), (22, "22"), (20, "20"), (11, "11"),
        (4, "4"), (24, "24"), (34, "34"), (30, "30"), (23, "23")
    ]

    assert traversal.preorder_traverse(tree) == [
        (23, "23"), (4, "4"), (1, "1"), (11, "11"), (7, "7"), (20, "20"),
        (15, "15"), (22, "22"), (30, "30"), (24, "24"), (34, "34")
    ]

    assert traversal.preorder_traverse(tree, recursive=False) == [
        (23, "23"), (4, "4"), (1, "1"), (11, "11"), (7, "7"), (20, "20"),
        (15, "15"), (22, "22"), (30, "30"), (24, "24"), (34, "34")
    ]

    assert traversal.inorder_traverse(tree) == [
        (1, "1"), (4, "4"), (7, "7"), (11, "11"), (15, "15"), (20, "20"),
        (22, "22"), (23, "23"), (24, "24"), (30, "30"), (34, "34")
    ]

    assert traversal.inorder_traverse(tree, recursive=False) == [
        (1, "1"), (4, "4"), (7, "7"), (11, "11"), (15, "15"), (20, "20"),
        (22, "22"), (23, "23"), (24, "24"), (30, "30"), (34, "34")
    ]

    assert traversal.outorder_traverse(tree) == [
        (34, "34"), (30, "30"), (24, "24"), (23, "23"), (22, "22"),
        (20, "20"), (15, "15"), (11, "11"), (7, "7"), (4, "4"), (1, "1")
    ]

    assert traversal.outorder_traverse(tree, recursive=False) == [
        (34, "34"), (30, "30"), (24, "24"), (23, "23"), (22, "22"),
        (20, "20"), (15, "15"), (11, "11"), (7, "7"), (4, "4"), (1, "1")
    ]


def test_red_black_tree_traversal(basic_tree):
    """Test red black tree traversal."""
    tree = red_black_tree.RBTree()

    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    # FIXME: LeafNode
    """
    assert traversal.levelorder_traverse(tree) == [
        (20, "20"), (7, "7"), (23, "23"), (4, "4"), (11, "11"), (22, "22"),
        (30, "30"), (1, "1"), (15, "15"), (24, "24"), (34, "34")
    ]
    """
