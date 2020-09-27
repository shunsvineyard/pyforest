# Copyright © 2020 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""The module demonstrates the useage of traversal functions."""

from pyforest.binary_trees import binary_search_tree
from pyforest.binary_trees import traversal

tree = binary_search_tree.BinarySearchTree()

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


print("In-Order Traversal")
for item in traversal.inorder_traverse(tree):
    print(item[0], end=" ")
# Output: 4 7 11 15 20 22 23 24 30 3
print("\n")

print("Reverse In-Order Traversal")
for item in traversal.reverse_inorder_traverse(tree):
    print(item[0], end=" ")
# Output: 34 30 24 23 22 20 15 11 7 4 1
print("\n")

print("Pre-Order Traversal")
for item in traversal.preorder_traverse(tree):
    print(item[0], end=" ")
# Output: 23 4 1 11 7 20 15 22 30 24 34
print("\n")

print("Post-Order Traversal")
for item in traversal.postorder_traverse(tree):
    print(item[0], end=" ")
# Output: 1 7 15 22 20 11 4 24 34 30 23
print("\n")

print("Level-Order Traversal")
for item in traversal.levelorder_traverse(tree):
    print(item[0], end=" ")
# Output: 23 4 30 1 11 24 34 7 20 15 22
print("\n")
