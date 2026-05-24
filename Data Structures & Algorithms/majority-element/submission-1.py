class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums = sorted(nums)
        if nums[0] == nums[-1]:
            return nums[0]
        else:
            hmap = {}
            for num in nums:
                if num in hmap:
                    hmap[num] += 1
                else:
                    hmap[num] = 1

                if hmap[num] > len(nums) // 2:
                    return num