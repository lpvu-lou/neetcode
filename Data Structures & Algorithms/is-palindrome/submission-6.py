class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())

        mid = len(s) // 2

        if len(s) % 2 == 0:
            return s[:mid] == s[mid:][::-1]
        else:
            return s[:mid] == s[mid+1:][::-1]