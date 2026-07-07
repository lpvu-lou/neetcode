class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i, v in enumerate(nums):
            x = v
            if x in dict:
                return True

            dict.update({v: i})
        
        return False