# Copyright © 2020 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""The module demonstrates using AVL Tree to implement Map."""

from pyforest.binary_trees import avl_tree
from pyforest.binary_trees import traversal


class Map:
    """Map example implemented by AVL Tree."""

    def __init__(self):
        self._avlt = avl_tree.AVLTree()

    def __setitem__(self, key, value):
        self._avlt.insert(key=key, data=value)

    def __getitem__(self, key):
        return self._avlt.search(key=key).data

    def __delitem__(self, key):
        self._avlt.delete(key=key)

    def __iter__(self):
        return traversal.inorder_traverse(tree=self._avlt)

    @property
    def empty(self) -> bool:
        """Return `True` if the map is empty; `False` otherwise."""
        return self._avlt.empty


if __name__ == "__main__":

    # Initialize the Map instance.
    contacts = Map()

    # Add some items.
    contacts["Mark"] = "mark@email.com"
    contacts["John"] = "john@email.com"
    contacts["Luke"] = "luke@email.com"
    contacts["john"] = "john@email.com"

    # Iterate the items.
    for contact in contacts:
        print(contact)

    # Delete one item.
    del contacts["john"]

    # Check the deleted item.
    try:
        print(contacts["john"])
    except KeyError:
        print("john does not exist")
