# Copyright © 2020 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

from pyforest.binary_trees import binary_search_tree
from pyforest.binary_trees import traversal


class Map:

    def __init__(self):
        self._bst = binary_search_tree.BinarySearchTree()

    def __setitem__(self, key, value):
        self._bst.insert(key=key, data=value)

    def __getitem__(self, key):
        return self._bst.search(key=key).data

    def __delitem__(self, key):
        self._bst.delete(key=key)

    def __iter__(self):
        return traversal.inorder_traverse(tree=self._bst)

    @property
    def empty(self):
        return self._bst.empty

    @property
    def size(self):
        return 0


if __name__ == "__main__":
    mymap = Map()
