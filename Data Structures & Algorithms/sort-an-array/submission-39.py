# counting sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        # step 1
        min_value = min(nums)
        max_value = max(nums)

        offset = -min_value

        # step 2
        freq = [0] * (max_value - min_value + 1)
        # count frequency for each element
        for v in nums:
            freq[v+offset] += 1

        # step 3: accumlate weights
        for i in range(1, len(freq)):
            freq[i] = freq[i] + freq[i-1]

        # Step 4: shift 1 to the right
        for i in range(len(freq) - 1, 0, -1):
            freq[i] = freq[i - 1]
        freq[0] = 0

        # step 5: output
        # initialize output array
        output = [0] * n

        # fill the output array
        for i in range(n):
            v = nums[i]
            idx = v + offset
            output[freq[idx]] = v
            freq[idx] += 1

        return output
            
            
        

        