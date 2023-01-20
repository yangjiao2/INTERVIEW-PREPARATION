# https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/1349609/python-4-solutions-minheap-maxheap-quickselect-clean-concise/?orderBy=most_votes

Time: O(N) in the avarage case, O(N^2) in the worst case.
Space: O(N)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthSmallest(nums, 0, len(nums) - 1, len(nums) - k + 1 - 1)

    def findKthSmallest(self, nums, left, right, k):  # k is one-base indexing
        def partition(left, right, pivotIndex):
            pivot = nums[pivotIndex]

            # Move pivot to the right most
            nums[right], nums[pivotIndex] = nums[pivotIndex], nums[right]
            pivotIndex = left

            # Swap elements less than pivot to the left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[pivotIndex], nums[i] = nums[i], nums[pivotIndex]
                    pivotIndex += 1

            # Move pivot to the right place
            nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
            return pivotIndex

        if left == right:
            return nums[left]

        pivotIndex = random.randint(left, right)  # Rand between [left, right]
        pivotIndex = partition(left, right, pivotIndex)
        if pivotIndex == k:
            return nums[pivotIndex]
        if k < pivotIndex:
            return self.findKthSmallest(nums, left, pivotIndex - 1, k)
        return self.findKthSmallest(nums, pivotIndex + 1, right, k)
