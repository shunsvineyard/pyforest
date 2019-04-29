# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

import enum


# first index for sorting by name
# second index for sorting by release date


class SortType(enum.Enum):
    Name = enum.auto()
    RELEASE_DATE = enum.auto()

class MovieLibrary:
    
    def __init__(self):
        pass

    def add(self, name: str, path: str):
        pass

    def delete(self, name: str, path: str):
        pass

    def search(self, name: str = None, date: str = None):
        pass

    def view_all(self, sort: SortType):
        pass

    def get_latest(self) -> str:
        pass

    def get_oldest(self) -> str:
        pass