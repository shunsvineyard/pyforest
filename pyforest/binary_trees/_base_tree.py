# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

import abc

class BaseTree(abc.ABC):
    """An abstract base class for any types of binary trees. This base class
    defines the basic properties and methods that all types of binary tress
    should provide.

    Attributes
    ----------
    left: node
        The left child of the node.

    right: node
        The right child of the node.

    data: Any
        The data that the node contains.

    Methods
    -------
    search(value: Any)
        Search a binary tree for a specific value.

    insert(value: Any)
        Insert a value into a binary tree.

    delete(value: Any)
        Delete a value from a binary treeW.

    Note: One reason to use abstract base class for all types of binary trees
    is to make sure the type of binary trees is compatable. Therefore, binary
    tree traversal can be performed on any type of binary trees.
    """
    @abc.abstractmethod
    def search(self, value):
        pass

    @abc.abstractmethod
    def insert(self, value):
        pass

    @abc.abstractmethod
    def delete(self, value):
        pass

    @abc.abstractproperty
    def left(self):
        pass

    @abc.abstractproperty
    def right(self):
        pass

    @abc.abstractproperty
    def data(self):
        pass




