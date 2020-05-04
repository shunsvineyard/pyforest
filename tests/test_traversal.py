"""Unit tests for the traversal module."""

from pyforest.binary_trees import avl_tree
from pyforest.binary_trees import binary_search_tree
from pyforest.binary_trees import red_black_tree
from pyforest.binary_trees import traversal


def test_binary_search_tree_traversal(basic_tree):
    """Test binary search tree traversal."""
    tree = binary_search_tree.BinarySearchTree()

    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    assert [item for item in traversal.postorder_traverse(tree)] == [
        (1, "1"), (7, "7"), (15, "15"), (22, "22"), (20, "20"), (11, "11"),
        (4, "4"), (24, "24"), (34, "34"), (30, "30"), (23, "23")
    ]

    assert [item for item in traversal.postorder_traverse(tree, False)] == [
        (1, "1"), (7, "7"), (15, "15"), (22, "22"), (20, "20"), (11, "11"),
        (4, "4"), (24, "24"), (34, "34"), (30, "30"), (23, "23")
    ]

    assert [item for item in traversal.preorder_traverse(tree)] == [
        (23, "23"), (4, "4"), (1, "1"), (11, "11"), (7, "7"), (20, "20"),
        (15, "15"), (22, "22"), (30, "30"), (24, "24"), (34, "34")
    ]

    assert [item for item in traversal.preorder_traverse(tree, False)] == [
        (23, "23"), (4, "4"), (1, "1"), (11, "11"), (7, "7"), (20, "20"),
        (15, "15"), (22, "22"), (30, "30"), (24, "24"), (34, "34")
    ]

    assert [item for item in traversal.inorder_traverse(tree)] == [
        (1, "1"), (4, "4"), (7, "7"), (11, "11"), (15, "15"), (20, "20"),
        (22, "22"), (23, "23"), (24, "24"), (30, "30"), (34, "34")
    ]

    assert [item for item in traversal.inorder_traverse(tree, False)] == [
        (1, "1"), (4, "4"), (7, "7"), (11, "11"), (15, "15"), (20, "20"),
        (22, "22"), (23, "23"), (24, "24"), (30, "30"), (34, "34")
    ]

    assert [item for item in traversal.outorder_traverse(tree)] == [
        (34, "34"), (30, "30"), (24, "24"), (23, "23"), (22, "22"),
        (20, "20"), (15, "15"), (11, "11"), (7, "7"), (4, "4"), (1, "1")
    ]

    assert [item for item in traversal.outorder_traverse(tree, False)] == [
        (34, "34"), (30, "30"), (24, "24"), (23, "23"), (22, "22"),
        (20, "20"), (15, "15"), (11, "11"), (7, "7"), (4, "4"), (1, "1")
    ]


def test_red_black_tree_traversal(basic_tree):
    """Test red black tree traversal."""
    tree = red_black_tree.RBTree()

    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    # FIXME: LeafNode


def test_avl_tree_traversal(basic_tree):
    """Test AVL tree traversal."""
    tree = avl_tree.AVLTree()

    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    assert [item for item in traversal.inorder_traverse(tree, False)] == [
        (1, "1"), (4, "4"), (7, "7"), (11, "11"), (15, "15"), (20, "20"),
        (22, "22"), (23, "23"), (24, "24"), (30, "30"), (34, "34")
    ]
