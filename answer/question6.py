from typing import List, Union


def unique_ordered(items: List[int | str]) -> List[int | str]:
    result = []
    for i in range(0, len(items)):
        if items[i] not in result:
            result.append(items[i])
    return result
