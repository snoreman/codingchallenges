#!/usr/bin/env python3

"""

return a new sorted merged list from k sorted lists. each with size N

"""

import heapq
#one solution is to flatten lists and sort O(KN log KN)
def merge_sorted_lists(lists):
    flat_list = [item for sublist in lists for item in sublist]
    print (flat_list)
    sorted_list = sorted(flat_list)
    print(sorted_list)
    return sorted_list


merge_sorted_lists([[1, 2, 3], [2, 3, 4], [3, 10, 20], [5, 11, 12]])

sorted1 = merge_sorted_lists([[10, 15, 30], [12, 15, 20], [17, 20, 32]]) # should be  [10, 12, 15, 15, 17, 20, 20, 30, 32]
#sorted1.insert(0, 1)
print (sorted1)
assert sorted1 == [10, 12, 15, 15, 17, 20, 20, 30, 32], "Error {} does not equal {}.".format(sorted1, \
        [10, 12, 15, 15, 17, 20, 20, 30, 32])
print (sorted1 == [10, 12, 15, 15, 17, 20, 20, 30, 32])
#these cases arent working need to be explicitly checked for
#merge_sorted_lists([1])
#merge_sorted_lists([])


def merge_sorted_lists_better(lists):
    merged_list = []
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    print (list(enumerate(lists)))
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],list_ind, element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list

""""
Some test cases
- lists is []
- lists only contains empty lists [[], []. []]
- lists contain empty lists and non-empty lists [[], [1]. [1, 2]]
- lists contains lists of varying size [[1], [1,3,5], [1, 10, 20, 30, 40]]

Other solutions? use divide and conguer strategy
recursively merge each half of the lists and then combine the two lists
would have same asymptotic complexities but would require more "real" memory and time
"""""

sorted1 = merge_sorted_lists_better([[10, 15, 30], [12, 15, 20], [17, 20, 32]]) # should be  [10, 12, 15, 15, 17, 20, 20, 30, 32]
#sorted1.insert(0, 1)
print (sorted1)
assert sorted1 == [10, 12, 15, 15, 17, 20, 20, 30, 32], "Error {} does not equal {}.".format(sorted1, \
        [10, 12, 15, 15, 17, 20, 20, 30, 32])
print (sorted1 == [10, 12, 15, 15, 17, 20, 20, 30, 32])
