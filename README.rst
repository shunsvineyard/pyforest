####################
The Forest in Python
####################

.. image:: https://travis-ci.com/shunsvineyard/pyforest.svg?branch=master
    :target: https://travis-ci.com/shunsvineyard/pyforest

.. image:: https://codecov.io/gh/shunsvineyard/pyforest/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/shunsvineyard/pyforest

The Forest is a tree data structure library for fun and also used as an example for Sphinx, and my Python working environment.

The Forest contains the following tree data structures:

- Binary Trees
    - AVL Tree
    - Binary Search Tree
    - Red Black Tree
    - Threaded Binary Tree
- B Tree

The Forest also provides the tree traversal feature to traverse binary trees and generic trees.

- Binary Tree Traversal
    - In-order
    - Out-order
    - Pre-order
    - Post-order
    - Level-order
- Generic Tree Traversal
    - Breadth First Search
    - Depth First Search

Requirements
============

The Forest uses the standard Python library as much as possible, but it does have the following dependencies:

- Python 3.7
- pytest (for unit test)
- Sphinx (for documents)

Installation
============


Roadmap
=======
Although the purpose of building ``The Forest`` is for fun and for informative, it is unlikely ``The Forest`` can be built all at once. Therefore, ``The Forest`` will be implemented by the following plan.

- **The Forest 1.0** supports Binary Trees (e.g., Binary Search Tree and Red-Black Tree), and binary tree traversal.
- **The Forest 2.0** focuses on B-Trees, including B-Tree, B+-Tree, 2-3 Tree, etc.
- **The Forest 3.0** may implement Heap.
- **The Forest 4.0** may implement more general tree data structures, and Breadth First Search and Depth First Search.

Version
-------
The version format of ``The Forest`` is x.y.z with the following convention:
- x: major change. For example, for The Forest 1.0, x is 1. And, x is 2 in The Forest 2.0.
- y: new trees or new features. When a new tree or a new feature is added into The Forest, bump up this number.
- z: minor change or bug fix.


