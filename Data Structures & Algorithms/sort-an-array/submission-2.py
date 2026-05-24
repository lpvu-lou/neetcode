# Bubble Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1): # -i: how many elements have been sorted
            # -1: because we compare j and j + 1: not out of bound
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
                