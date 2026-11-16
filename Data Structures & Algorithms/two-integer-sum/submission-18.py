class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, v in enumerate(nums):
            left = target - v
            if left in store:
                return [store[left], i]
            
            store.update({v: i})


                


        