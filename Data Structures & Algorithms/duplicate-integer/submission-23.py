class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i, v in enumerate(nums):
            if v in dict: # check clés
                return True
            
            dict.update({v : i})
        return False