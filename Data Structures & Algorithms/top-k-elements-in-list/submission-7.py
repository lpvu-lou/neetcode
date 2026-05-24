class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        sort_freq = sorted(freq.items(), key=lambda x: x[1])

        output = []
        for j in range(1, k+1):
            output.append(sort_freq[-j][0])
        
        return output