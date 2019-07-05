import pytest

from pyforest.binary_trees import binary_search_tree
from pyforest.binary_trees import traversal

def test_simple_case():

    tree = binary_search_tree.BinarySearchTree()
    # Test an empty tree
    assert tree.size() == 0

    # Draw a tree
    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    tree.insert(key=23, data="23")
    tree.insert(key=4, data="4")
    tree.insert(key=30, data="30")
    tree.insert(key=11, data="11")
    tree.insert(key=7, data="7")
    tree.insert(key=34, data="34")
    tree.insert(key=20, data="20")
    tree.insert(key=24, data="24")
    tree.insert(key=22, data="22")
    tree.insert(key=15, data="15")
    tree.insert(key=1, data="1")

    assert tree.size() == 11
    assert tree.get_min() == 1
    assert tree.get_max() == 34
    assert tree.get_height() == 5
    assert tree.is_balance() == False
    assert tree.search(24) == "24"

    tree.delete(15)
    tree.delete(22)
    tree.delete(7)
    tree.delete(20)

    assert tree.size() == 7
    assert tree.get_height() == 3
    assert tree.is_balance() == True

    with pytest.raises(KeyError):
        tree.search(15)


def test_deletion():
    tree = binary_search_tree.BinarySearchTree()

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    tree.insert(key=23, data="23")
    tree.insert(key=4, data="4")
    tree.insert(key=30, data="30")
    tree.insert(key=11, data="11")
    tree.insert(key=7, data="7")
    tree.insert(key=34, data="34")
    tree.insert(key=20, data="20")
    tree.insert(key=24, data="24")
    tree.insert(key=22, data="22")
    tree.insert(key=15, data="15")
    tree.insert(key=1, data="1")

    # No child
    tree.delete(15)
    assert traversal.levelorder_traverse(tree) == [
        (23, "23"), (4, "4"), (30, "30"), (1, "1"), (11, "11"),
        (24, "24"), (34, "34"), (7, "7"), (20, "20"), (22, "22")
    ]

    # One right child
    tree.delete(20)
    assert traversal.levelorder_traverse(tree) == [
        (23, "23"), (4, "4"), (30, "30"), (1, "1"), (11, "11"),
        (24, "24"), (34, "34"), (7, "7"), (22, "22")
    ]

    # One left child
    tree.insert(key=17, data="17")
    tree.delete(22)
    assert traversal.levelorder_traverse(tree) == [
        (23, "23"), (4, "4"), (30, "30"), (1, "1"), (11, "11"),
        (24, "24"), (34, "34"), (7, "7"), (17, "17")
    ]

    # Two children
    tree.delete(11)
    assert traversal.levelorder_traverse(tree) == [
        (23, "23"), (4, "4"), (30, "30"), (1, "1"),
        (17, "17"), (24, "24"), (34, "34"), (7, "7")
    ]

