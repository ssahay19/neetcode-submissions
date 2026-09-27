class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ""
        for char in s:
            if char.isalnum():
                n += char.lower()

        return n == n[::-1]