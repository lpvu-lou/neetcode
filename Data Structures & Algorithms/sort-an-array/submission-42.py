# Shell Short : improved version of insertion sort
# instead of comparind only neighboring elements, we compare elements that are far apart
# then gradually reduce the distance
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        gap = n // 2 # big gap first

        while gap > 0:
            for i in range(gap, n):
                j = i

                while j - gap >=0 and nums[j - gap] > nums[j]:
                    nums[j], nums[j - gap] = nums[j - gap], nums[j]
                    j -= gap

            gap //= 2
        
        return nums

