from typing import Any, Iterator, Tuple, TypeVar


KeyType = TypeVar("KeyType")
"""Type of a tree node key. The key must be comparable."""

Pairs = Iterator[Tuple[KeyType, Any]]
"""An iterator of Key-Value pairs. Yield by traversal functions."""


def inorder_traverse(root) -> Pairs:
    if root:
        yield from inorder_traverse(root.left)
        yield (root.key, root.data)
        yield from inorder_traverse(root.right)


def inorder_traverse_non_recursive(root) -> Pairs:
    if root is None:
        raise StopIteration

    stack = []
    if root.right:
        stack.append(root.right)
        stack.append(root)

    current = root.left

    while True:

        if current:
            if current.right:
                stack.append(current.right)
                stack.append(current)
                current = current.left
                continue
            stack.append(current)
            current = None

        else:  # current is None

            if len(stack) > 0:
                current = stack.pop()

                if current.right is None:
                    yield (current.key, current.data)
                    current = None
                    continue
                else:  # current.right is not None
                    if len(stack) > 0:
                        if current.right == stack[-1]:
                            yield (current.key, current.data)
                            current = None
                            continue
                        else:  # current.right != stack[-1]:
                            # This case means there are more nodes on the right
                            # Keep the current and go back to add them.
                            continue

            else:  # stack is empty
                break


def reverse_inorder_traverse(root) -> Pairs:
    if root:
        yield from reverse_inorder_traverse(root.right)
        yield (root.key, root.data)
        yield from reverse_inorder_traverse(root.left)


def reverse_inorder_traverse_non_recursive(root) -> Pairs:
    if root is None:
        raise StopIteration

    stack = []
    if root.left:
        stack.append(root.left)
        stack.append(root)

    current = root.right

    while True:

        if current:
            if current.left:
                stack.append(current.left)
                stack.append(current)
                current = current.right
                continue
            stack.append(current)
            current = None

        else:  # current is None

            if len(stack) > 0:
                current = stack.pop()

                if current.left is None:
                    yield (current.key, current.data)
                    current = None
                    continue
                else:  # current.right is not None
                    if len(stack) > 0:
                        if current.left == stack[-1]:
                            yield (current.key, current.data)
                            current = None
                            continue
                        else:  # current.right != stack[-1]:
                            # This case means there are more nodes on the right
                            # Keep the current and go back to add them.
                            continue

            else:  # stack is empty
                break


def preorder_traverse(root) -> Pairs:
    if root:
        yield (root.key, root.data)
        yield from preorder_traverse(root.left)
        yield from preorder_traverse(root.right)


def preorder_traverse_non_recursive(root) -> Pairs:
    if root is None:
        raise StopIteration

    stack = [root]

    while len(stack) > 0:
        temp = stack.pop()
        yield (temp.key, temp.data)

        # Because stack is FILO, insert right child before left child.
        if temp.right:
            stack.append(temp.right)

        if temp.left:
            stack.append(temp.left)


def postorder_traverse(root) -> Pairs:
    if root:
        yield from postorder_traverse(root.left)
        yield from postorder_traverse(root.right)
        yield (root.key, root.data)


def postorder_traverse_non_recursive(root) -> Pairs:
    if root is None:
        raise StopIteration

    stack = []
    if root.right:
        stack.append(root.right)

    stack.append(root)
    current = root.left

    while True:

        if current:
            if current.right:
                stack.append(current.right)
                stack.append(current)
                current = current.left
                continue
            else:  # current.right is None
                yield (current.key, current.data)
                current = None

        else:  # current is None
            if len(stack) > 0:
                current = stack.pop()

                if current.right is None:
                    yield (current.key, current.data)
                    current = None
                else:  # current.right is not None
                    if len(stack) > 0:
                        if current.right != stack[-1]:
                            yield (current.key, current.data)
                            current = None
                        else:  # current.right == stack[-1]
                            temp = stack.pop()
                            stack.append(current)
                            current = temp

                    else:  # stack is empty
                        yield (current.key, current.data)
                        break


def levelorder_traverse(root) -> Pairs:

    queue = [root]

    while len(queue) > 0:
        temp = queue.pop(0)
        if temp:
            yield (temp.key, temp.data)
            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)
