class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = sorted(nums)
        curr = 1
        longest = 1
        for i in range(len(n)-1):
            if n[i+1] == (n[i] + 1):
                curr+=1
                longest = max(longest, curr)
            elif n[i+1] == n[i]:
                continue
            else:
                curr = 1
        return longest 