class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram : a string that contains the exact same characters as another strings, but the order of the characters can be different
        dict = {}
        for str in strs:
            sorted_strs = ''.join(sorted(str))
            if sorted_strs in dict:
                dict[sorted_strs].append(str)
            else: 
                dict[sorted_strs] = [str]

        return list(dict.values())