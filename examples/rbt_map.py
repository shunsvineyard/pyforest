# Copyright © 2020 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

from pyforest.binary_trees import red_black_tree
from pyforest.binary_trees import traversal


class Map:

    def __init__(self):
        self._rbt = red_black_tree.RBTree()

    def __setitem__(self, key, value):
        self._rbt.insert(key=key, data=value)

    def __getitem__(self, key):
        return self._rbt.search(key=key).data

    def __delitem__(self, key):
        self._rbt.delete(key=key)

    def __iter__(self):
        return traversal.inorder_traverse(tree=self._rbt)

    @property
    def empty(self):
        return self._rbt.empty

    @property
    def size(self):
        return 0


if __name__ == "__main__":
    mymap = Map()
