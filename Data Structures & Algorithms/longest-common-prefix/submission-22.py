class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        ans = len(ref)

        for i in range(1, len(strs)):
            target = strs[i]
            m = min(ans, len(target))

            for j in range(m):
                if ref[j] != target[j]:
                    ans = j
                    break
            else:
                ans = m

        return ref[:ans]