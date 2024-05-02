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
    if type(boxes) is not list or len(boxes) == 0:
        return False

    if len(boxes) <= 1 or boxes == [[]]:
        return True

    def dfs(box_index, visited):
        if visited[box_index]:
            return
        visited[box_index] = True
        for key in boxes[box_index]:
            if key < len(boxes):
                dfs(key, visited)

    n = len(boxes)
    visited = [False] * n
    dfs(0, visited)
    return all(visited)
