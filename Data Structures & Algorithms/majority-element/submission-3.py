class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # the majority element must occupy the middle position
        nums.sort()
        return nums[len(nums) // 2]