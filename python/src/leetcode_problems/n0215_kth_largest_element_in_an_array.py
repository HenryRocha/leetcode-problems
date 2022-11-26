import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Given an integer array nums and an integer k, return
        the kth largest element in the array.

        Note that it is the kth largest element in the sorted
        order, not the kth distinct element.
        """
        # The heapify function rearranges the given list
        # into a min heap. Since we want a max heap, all
        # we need to do is invert all the elements in
        # the nums list.
        inverted_nums = [n * -1 for n in nums]
        heapq.heapify(inverted_nums)

        for _ in range(k - 1):
            heapq.heappop(inverted_nums)

        return heapq.heappop(inverted_nums) * -1
