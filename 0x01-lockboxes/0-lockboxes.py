#!/usr/bin/python3
"""Lock Boxes Algorithm"""


def canUnlockAll(boxes):
   """Implement of Lock box Algo."""
    unlocked = [0]
    for bxd, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != bxd:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
            return True
    return False
