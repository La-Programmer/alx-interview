#!/usr/bin/python3
"""LockBoxes Algorithm"""

from queue import Queue


def canUnlockAll(boxes):
    """Function to check if all boxes can be unlocked"""
    if (boxes == [] or boxes is None):
        return True
    all_keys = {x for x in range(len(boxes))}
    visited_boxes = set()
    boxes_to_visit = Queue(maxsize=len(boxes))
    boxes_to_visit.put(0)

    while (boxes_to_visit.empty() is False):
        box_key = boxes_to_visit.get()
        box_to_visit = boxes[box_key]
        for key in box_to_visit:
            if key not in visited_boxes and key < len(boxes):
                boxes_to_visit.put(key)
        visited_boxes.add(box_key)
    return (visited_boxes & all_keys) == all_keys
