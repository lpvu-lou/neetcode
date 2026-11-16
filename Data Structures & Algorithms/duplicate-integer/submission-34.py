class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        after = set(nums)
        return len(after) != len(nums)