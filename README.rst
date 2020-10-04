#################################
Build the Forest in Python Series
#################################

.. image:: https://travis-ci.com/shunsvineyard/pyforest.svg?branch=master
    :target: https://travis-ci.com/shunsvineyard/pyforest

.. image:: https://codecov.io/gh/shunsvineyard/pyforest/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/shunsvineyard/pyforest

The Forest Project is a tree data structure library for fun. It has the following tree data structures:

- Binary Trees
    - AVL Tree
    - Binary Search Tree
    - Red Black Tree
    - Threaded Binary Trees

The Forest also provides the tree traversal feature to traverse binary trees and generic trees.

- Binary Tree Traversal
    - In-order
    - Reversed In-order
    - Pre-order
    - Post-order
    - Level-order

The API document is available at `The Forest Documentation <https://the-forest-in-python.readthedocs.io/en/latest/>`_.

Requirements
============

The Forest Project requires Python 3.7 or newer.
The key Python 3.7 feature used in the Forest Project is `dataclass <https://docs.python.org/3/library/dataclasses.html#module-dataclasses>`_.

Installation
============

There are two ways to install the Forest Project.

1. Install and update using `pip <https://pip.pypa.io/en/stable/quickstart/>`_:

.. code-block:: text

    pip install -U python-forest

2. Install from Github

.. code-block:: text

    git clone https://github.com/shunsvineyard/pyforest.git
    cd pyforest
    pip install .

Examples
========

.. code-block:: python

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


Forest CLI
==========

The Forest Project provides a command line tool to simulate tree data structures.

.. code-block:: text

    forest-cli

It will show the interactive prompt. Use ``help`` to list all the available commands


.. code-block:: text

    Welcome to the Forest CLI. Type help or ? to list commands.

    forest> help

    Documented commands (type help <topic>):
    ========================================
    build  delete  destroy  detail  exit  help  insert  search  traverse


Build the Forest Series
=======================

`Build the Forest Series <https://shunsvineyard.info/build-the-forest-series/>`_ is
a series of articles about tree data structures in the Forest Project. It provides
the tree concept and implementation detail of each tree data structures and the
thoughts behind the scenes.