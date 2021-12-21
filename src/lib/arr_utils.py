from typing import Callable, TypeVar

from random import randint

_T = TypeVar('_T')


def filter(arr: list[_T], func: Callable[[_T], bool]):
    
    arr_len = len(arr)

    filtered_items = []

    for i in range(arr_len):

        if func(arr[i]):
            filtered_items.append(arr[i])
    
    return filtered_items


def find_item(arr: list[_T], func: Callable[[_T], bool]):

    arr_len = len(arr)

    for i in range(arr_len):

        if func(arr[i]):
            return arr[i]
    
    return None


def find_index(arr: list[_T], func: Callable[[_T], bool]) -> int:

    arr_len = len(arr)

    for i in range(arr_len):

        if func(arr[i]):
            return i
        
    return -1


def shuffle(arr: list[_T]):

        arr = arr[:]

        max_index = len(arr) -1

        shuffled_arr: list[_T] = []

        while max_index >= 0:

            next_index = randint(0, max_index)

            item = arr.pop(next_index)

            shuffled_arr.append(item)

            max_index -= 1
        
        return shuffled_arr