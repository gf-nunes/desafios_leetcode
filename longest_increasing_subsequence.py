# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence.

import bisect


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        num = []
        for n in nums:
            if not num or num[-1] < n:
                num.append(n)
            else:
                i = bisect.bisect_left(num, n)
                num[i] = n
        return len(num)