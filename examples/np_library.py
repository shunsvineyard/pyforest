# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

from typing import Any

import enum

class SortType(enum.Enum):
    Name = enum.auto()
    Date = enum.auto() # Founded data
    Location = enum.auto()
    Size = enum.auto()

class NPLibrary:
    """The National Park Library is a simple in RAM database for storing
    National Parks information.

    No concurrency protection. No persistent. in ram only.
    """

    def __init__(self):

        # In the real world, the data is stored in a persistent medium
        # such as a disk. The example uses a dictionary to simulate
        # the persistent data.
        # (key, data)
        self._key = 0
        self._persistent_data = dict()

        # Usually, IO is the slowest. In order to sort efficient, most
        # database build second index to accelerate the sorting and
        # search operations.

        # {name, index}
        self._name_index = dict()

        # {date, index}
        self._date_index = dict()

        # {location, index}
        self._location_index = dict()

        # {size, index}
        self._size_index = dict()

    def insert(self, data: Any) -> NoReturn:
        self._persistent_data[self._key] = data
        self._key += 1

        self._name_index[name] = len(self._persistent_data) - 1

    def delete(self, name: str) -> NoReturn:
        pass

    def query(self, name: str) -> Any:
        
        index = self._name_index[name]
        return self._persistent_data[index]

    def update(self, name: str, data: Any) -> NoReturn:
        pass

    def list_all(self, sort: SortType):
        # in-order for sorting
        pass