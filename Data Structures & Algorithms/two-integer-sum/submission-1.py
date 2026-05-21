class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resultat = []
        for i in list(range(len(nums))):
            difference = target - nums[i]
            for j in list(range(i+1, len(nums))):
                if nums[j] == difference:
                    resultat = [i, j]
        return resultat


        