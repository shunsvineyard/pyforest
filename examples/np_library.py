# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A National Park Library to demonstrate the usage of binary search tree.

The purpose of National Park Library is to demonstrate how to use binary
search trees to build indexes. It is not an optimal solution. Besides,
most of databases are designed to host a lot of data and the data
are persistent on disks. However, the disk IO is usually the performance
bottleneck. Therefore, most databases build second index to find data quick.
In the National Park Library, it uses an array (i.e., a Python List) to
simulate a disk. And use binary search tree to build two indexes, name and
size, so it can perform sorting operation by name and size.
"""

import enum

from dataclasses import dataclass
from typing import Any, List, Tuple

from pyforest.binary_trees import binary_search_tree
from pyforest.binary_trees import traversal


class SortType(enum.Enum):
    """Sorting criteria."""

    Name = enum.auto()
    Size = enum.auto()


@dataclass
class NPData:
    """Data structure to hold national park data."""

    name: str
    location: str
    date: str
    area: int

    def dump(self):
        """Print out the data."""
        print(f"{self.name}, {self.location}, {self.date}, {self.area}")


class NPLibrary:
    """NPLibrary is a simple in RAM database for national park data.

    The purpose of NPLibrary is to demonstrate the usage of binary search tree.
    Therefore, the implementation of NPLibrary is not an optimal solution. It
    does not support concurrency protection; it does not persist data, either.
    """

    def __init__(self):
        # In the real world, the data is stored in a persistent medium
        # such as a disk. The NPLibrary uses an array (i.e., Python List)
        # to simulate a disk-like medium.
        self._persistent_data = []  # Use list to simulate disk

        # An unique key for each national park data.
        self._key = 0

        # Usually, disk IO is the slowest. In order to sort efficient,
        # most database build second index to accelerate the sorting and
        # search operations.

        # {name, index}
        self._name_index = binary_search_tree.BinarySearchTree()

        # {size, index}
        self._area_index = binary_search_tree.BinarySearchTree()

    def insert(self, data: NPData):
        """Insert a national park data.

        Parameters
        ----------
        data: NPData
            The national park data object.
        """
        self._persistent_data.append(data)
        self._name_index.insert(key=data.name, data=self._key)
        self._area_index.insert(key=data.area, data=self._key)

        #  Increase the key
        self._key += 1

    def delete(self, name: str):
        """Delete a national park data.

        Parameters
        ----------
        name: str
            The name of the national park to delete.
        """
        item_index = self._name_index.search(key=name)
        item = self._persistent_data[item_index]
        self._persistent_data[item_index] = None
        self._name_index.delete(key=name)
        self._area_index.delete(key=item.area)

    def query(self, name: str) -> NPData:
        """Query a national park data.

        Parameters
        ----------
        name: str
            The name of the national park to query.

        Returns
        -------
        NPData
            The national park data object.
        """
        item_index = self._name_index.search(key=name)
        return self._persistent_data[item_index]

    def update(self, name: str, data: NPData):
        """Update a national park data.

        Parameters
        ----------
        name: str
            The name of the national park to update.

        data: NPData
            The new national park data.
        """
        item_index = self._name_index.search(key=name)

        old_item = self._persistent_data[item_index]
        self._persistent_data[item_index] = data

        # Update the area index
        self._area_index.delete(key=old_item.area)
        self._area_index.insert(key=data.area, data=item_index)

    def list_all(self, sort_type: SortType, ascending: bool = True):
        """List all the national park data.

        Parameters
        ----------
        sort_type: SortType
            The sorting criteria.

        ascending: bool
            Ascending if True; decending otherwise.

        Raises
        ------
        ValueError
            If the sort_type is invalid, `valueError` will be thrown.
        """
        index_list: List[Tuple[Any, Any]] = []
        if sort_type == SortType.Name:
            if ascending:  # in-order traversal.
                index_list = traversal.inorder_traverse(tree=self._name_index)
            else:  # decending means out-order traversal.
                index_list = traversal.outorder_traverse(tree=self._name_index)
        elif sort_type == SortType.Size:
            if ascending:
                index_list = traversal.inorder_traverse(
                    tree=self._area_index)
            else:
                index_list = traversal.outorder_traverse(
                    tree=self._area_index)
        else:
            raise ValueError("Invalid SortType")

        for _, item_index in index_list:
            self._persistent_data[item_index].dump()
