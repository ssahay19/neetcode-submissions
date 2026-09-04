class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t1 = "".join(sorted(s))
        t2 = "".join(sorted(t))
        if t1==t2:
            return True
        return False