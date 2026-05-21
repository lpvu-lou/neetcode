class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minwlen = min(len(s) for s in strs)

        for i in range(minwlen):
            if any(w[i] != strs[0][i] for w in strs):
                return strs[0][:i]
        
        return strs[0][:minwlen]