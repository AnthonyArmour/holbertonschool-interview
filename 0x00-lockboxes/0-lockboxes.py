#!/usr/bin/env python3
"""
   The Lockbox Problem
"""


def check_boxes(checked, keys, boxes):
    """
       Checks each unchecked box corresponding to each key
         in keys.

       Args:
         checked: list of indecies of checked boxes
         keys: newest set of found keys
         boxes: list of boxes to be searched

       Return:
        checked: appended checked box indecies
        new_keys: newly found keys
    """

    new_keys = []

    for key in keys:
        if key not in checked:
            new_keys = new_keys + boxes[key]
            checked.append(key)

    return checked, new_keys


def canUnlockAll(boxes):
    """
       Checks to see if all boxes can be opened with
         accessible keys.

       Args:
         boxes: List of boxes to be checked

       Return:
         True, else False
    """
    keys = boxes[0]
    checked = [0]

    if type(keys) is not list or len(keys) == 0:
        return True

    for x in range(len(boxes)):
        if x in checked:
            continue

        checked, keys = check_boxes(checked, keys, boxes)

        if len(keys) == 0:
            break

    return len(checked) == len(boxes)
