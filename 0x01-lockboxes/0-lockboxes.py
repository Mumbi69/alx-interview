#!/usr/bin/python3
"""lockboxes class"""


def canUnlockAll(boxes):
    """represents the lockbox class"""
    opened_boxes = {0}

    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                queue.append(key)

    return len(opened_boxes) == len(boxes)
