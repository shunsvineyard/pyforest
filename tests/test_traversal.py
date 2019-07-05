
from pyforest.binary_trees import binary_search_tree
from pyforest.binary_trees import traversal

def test_binary_search_tree_traversal():
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


    assert traversal.levelorder_traverse(tree) == [
        (23, "23"), (4, "4"), (30, "30"), (1, "1"), (11, "11"), (24, "24"),
        (34, "34"), (7, "7"), (20, "20"), (15, "15"), (22, "22")
    ]

    assert traversal.postorder_traverse(tree) == [
        (1, "1"), (7, "7"), (15, "15"), (22, "22"), (20, "20"), (11, "11"),
        (4, "4"), (24, "24"), (34, "34"), (30, "30"), (23, "23")
    ]

    assert traversal.preorder_traverse(tree) == [
        (23, "23"), (4, "4"), (1, "1"), (11, "11"), (7, "7"), (20, "20"),
        (15, "15"), (22, "22"), (30, "30"), (24, "24"), (34, "34")
    ]

    assert traversal.inorder_traverse(tree) == [
        (1, "1"), (4, "4"), (7, "7"), (11, "11"), (15, "15"), (20, "20"),
        (22, "22"), (23, "23"), (24, "24"), (30, "30"), (34, "34")
    ]

    assert traversal.outorder_traverse(tree) == [
        (34, "34"), (30, "30"), (24, "24"), (23, "23"), (22, "22"),
        (20, "20"), (15, "15"), (11, "11"), (7, "7"), (4, "4"), (1, "1")
    ]


