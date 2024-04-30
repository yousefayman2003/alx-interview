#!/usr/bin/python3
"""Module containing Lockboxes problem solution"""


def canUnlockAll(boxes):
    """
        determines if all the boxes can be opened

        Args:
            boxes (list): a list of lists

        Returns:
            True if all boxes can be opened, else return False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    visited = set()

    def dfs(i):
        """
            Perform depth first search on boxes keys

            i (int): index of box to open
        """
        if i in visited:
            return

        visited.add(i)
        for n in boxes[i]:
            dfs(n)

    # Start DFS
    dfs(0)

    return len(visited) == len(boxes)
