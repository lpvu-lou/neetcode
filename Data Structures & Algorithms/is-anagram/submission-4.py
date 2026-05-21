class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = ''.join(sorted(s))
        T = ''.join(sorted(t))
        return S == T