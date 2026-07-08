class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for v in nums:
            if v in freq: 
                freq[v] += 1
            else:
                freq[v] = 1
        
        # k most frequent elements within the array
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse = True)

        output = []
        for i in range(k):
            output.append(sorted_freq[i][0])
        
        return output