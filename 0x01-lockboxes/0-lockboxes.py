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
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx, box in enumerate(boxes):
            if k in box and k != idx:
                boxes_checked = True
                break
        if not boxes_checked:
            return False

    return True
