from dataclasses import dataclass
from typing import Any, Generic, Optional, TypeVar


KeyType = TypeVar("KeyType")
"""Type of a tree node key. The key must be comparable."""


@dataclass
class Node(Generic[KeyType]):
    """Basic binary tree node definition."""

    key: KeyType
    data: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None


class BinarySearchTree:

    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, key: KeyType, data: Any):
        new_node = Node(key=key, data=data)
        parent = None
        temp = self.root
        while temp:
            parent = temp
            if new_node.key == temp.key:
                raise KeyError(f"{key} already exists")
            elif new_node.key < temp.key:
                temp = temp.left
            else:
                temp = temp.right
        new_node.parent = parent
        # If the tree is empty
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def search(self, key: KeyType) -> Node:
        current = self.root
        while current:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:  # key > current.key:
                current = current.right
        raise KeyError(f"{key} not found")

    def delete(self, key: KeyType):
        if self.root:
            deleting_node = self.search(key=key)

            # Case 1: No child or Case 2: only one right child
            if deleting_node.left is None:
                self._transplant(deleting_node=deleting_node,
                                 replacing_node=deleting_node.right)
            # Case 2: Only one left child
            elif deleting_node.right is None:
                self._transplant(deleting_node=deleting_node,
                                 replacing_node=deleting_node.left)
            # Case 3: Two children
            else:
                min_node = self.get_min(node=deleting_node.right)
                # the min node is not the direct child of the deleting node
                if min_node:
                    if min_node.parent != deleting_node:
                        self._transplant(deleting_node=min_node,
                                         replacing_node=min_node.right)
                        min_node.right = deleting_node.right
                        min_node.right.parent = min_node
                    self._transplant(deleting_node=deleting_node,
                                     replacing_node=min_node)
                    min_node.left = deleting_node.left
                    min_node.left.parent = min_node
                else:
                    raise RuntimeError("Leftmost node must exist when \
                                        deleting node has two children")

    def get_min(self, node: Optional[Node] = None) -> Optional[Node]:
        if node:
            current_node = node
        else:
            if self.root:
                current_node = self.root
            else:
                return None
        while current_node.left:
            current_node = current_node.left
        return current_node

    def get_max(self, node: Optional[Node] = None) -> Optional[Node]:
        if node:
            current_node = node
        else:
            if self.root:
                current_node = self.root
            else:
                return None
        if current_node:
            while current_node.right:
                current_node = current_node.right
        return current_node

    def get_successor(self, node: Node) -> Optional[Node]:
        if node.right:  # Case 1: Right child is not empty
            return self.get_min(node=node.right)
        # Case 2: Right child is empty
        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    def get_predecessor(self, node: Node) -> Optional[Node]:
        if node.left:  # Case 1: Left child is not empty
            return self.get_max(node=node.left)
        # Case 2: Left child is empty
        parent = node.parent
        while parent and node == parent.left:
            node = parent
            parent = parent.parent
        return parent

    def _transplant(self, deleting_node: Node,
                    replacing_node: Optional[Node]):
        if deleting_node.parent is None:
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node
        if replacing_node:
            replacing_node.parent = deleting_node.parent


class Contact:

    def __init__(self):
        self._bst = BinarySearchTree()

    def __setitem__(self, name: str, email: str):
        self._bst.insert(key=name, data=email)

    def __getitem__(self, name: str):
        return self._bst.search(key=name).data

    def __delitem__(self, name: str):
        self._bst.delete(key=name)

    def list_all(self, ascending: bool = True):

        if ascending:
            item = self._bst.get_min()
            while item:
                yield (item.key, item.data)
                item = self._bst.get_successor(node=item)
        else:
            item = self._bst.get_max()
            print(item.key)

            while item:
                yield (item.key, item.data)
                item = self._bst.get_predecessor(node=item)


if __name__ == "__main__":

    # Initialize the Contact instance.
    contacts = Contact()

    # Add some items.
    contacts["Mark"] = "mark@email.com"
    contacts["John"] = "john@email.com"
    contacts["Luke"] = "luke@email.com"
    contacts["john"] = "john@gmail.com"

    print("List all contacts in ascending order")
    for contact in contacts.list_all():
        print(contact)

    # Delete one item.
    print("Delete john's contact info")
    del contacts["john"]

    # Check the deleted item.
    try:
        print(contacts["john"])
    except KeyError:
        print("john does not exist")

    print("List all contacts in decending order")
    for contact in contacts.list_all(ascending=False):
        print(contact)
