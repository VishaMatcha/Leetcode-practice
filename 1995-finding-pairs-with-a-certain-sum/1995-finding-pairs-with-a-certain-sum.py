from collections import Counter
from typing import List

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        """
        Initializes the FindSumPairs object with two lists and their counters.
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter1 = Counter(nums1)
        self.counter2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        """
        Adds val to the element at index in nums2 and updates the counter.
        """
        old_val = self.nums2[index]
        new_val = old_val + val
        self.nums2[index] = new_val
        self.counter2[old_val] -= 1
        if self.counter2[old_val] == 0:
            del self.counter2[old_val]
        self.counter2[new_val] += 1

    def count(self, tot: int) -> int:
        """
        Counts the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.
        """
        total_pairs = 0
        for num1, count1 in self.counter1.items():
            complement = tot - num1
            count2 = self.counter2.get(complement, 0)
            total_pairs += count1 * count2
        return total_pairs