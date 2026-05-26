class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = dict()

        for i in range(n):
            v = nums[i]
            if v in freq:
                freq[v] += 1
            else:
                freq[v] = 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1])

        output = []
        for i in range(1, k+1):
            output.append(sorted_freq[-i][0])
        
        return output