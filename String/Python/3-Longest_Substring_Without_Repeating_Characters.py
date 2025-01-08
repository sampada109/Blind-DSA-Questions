# Longest Substring Without Repeating Characters
# Question Link - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Time Complexity - O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        maxcount = 0

        dic = {}

        while(r < len(s)):
            if s[r] in dic:
                if dic[s[r]] >= l:
                    l = dic[s[r]] + 1
            dic[s[r]] = r
            count = r-l + 1
            maxcount = max(count, maxcount)
            r += 1

        return maxcount
