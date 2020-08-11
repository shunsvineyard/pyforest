from dataclasses import dataclass
from typing import Any, Generic, Optional, TypeVar

KeyType = TypeVar("KeyType")
"""Type of a tree node key. The key must be comparable."""

Pairs = Iterator[Tuple[KeyType, Any]]
"""An iterator of Key-Value pairs. Yield by traversal functions."""


@dataclass
class SingleThreadNode(Generic[KeyType]):

    key: KeyType
    data: Any
    left: Optional["SingleThreadNode"] = None
    right: Optional["SingleThreadNode"] = None
    parent: Optional["SingleThreadNode"] = None
    isThread: bool = False


class RightThreadedBinaryTree:

    def __init__(self):
        self.root: Optional[SingleThreadNode] = None

    def insert(self, key: KeyType, data: Any):
        # ...

    def search(self, key: KeyType) -> SingleThreadNode:
        # ...

    def delete(self, key: KeyType):
        # ...

    def get_leftmost(self,
                node: Optional[SingleThreadNode] = None) -> SingleThreadNode:
        # ...

    def get_rightmost(self,
                node: Optional[SingleThreadNode] = None) -> SingleThreadNode:
        # ...

    def get_successor(self,
                      node: SingleThreadNode) -> Optional[SingleThreadNode]:
        # ...

    def get_predecessor(self,
                        node: SingleThreadNode) -> Optional[SingleThreadNode]:
        # ...


    def get_height(self, node: Optional[binary_tree.Node]) -> int:
        # ...

    def inorder_traverse(self) -> Pairs:
        # ...

    def preorder_traverse(self) -> Pairs:
        # ...