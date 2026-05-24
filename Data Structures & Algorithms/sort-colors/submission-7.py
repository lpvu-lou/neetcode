# Dutch National Flag
# 3 pointers = low mid high -> 4 invariants
# left of low = low
# low to left of mid = mid (include low)
# mid to high (include mid and high) = unknown
# mid = first unknown, high = last unknown
# right of high = high
# when mid pass high = finish
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # initialize pointers : l red, m white, h blue
        l = m = 0
        h = n - 1

        while m <= h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l] 
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m], nums[h] = nums[h], nums[m] 
                h -= 1

            



        
        