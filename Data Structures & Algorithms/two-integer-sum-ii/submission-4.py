class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i, v in enumerate(numbers):
            diff = target - v
            if diff in dict:
                ans = [dict[diff] + 1, i + 1]
            dict.update({v: i})
        
        return sorted(ans)