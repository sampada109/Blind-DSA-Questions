// Longest Substring Without Repeating Characters
// Question Link - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
// Time complexity - O(n)

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int l = 0, r = 0, maxcount = 0;

        unordered_map<char, int> mpp;

    while (r < s.length()) {
        if (mpp.find(s[r]) != mpp.end() && mpp[s[r]] >= l) {
            l = mpp[s[r]] + 1;
        }
        mpp[s[r]] = r;
        int count = r - l + 1;
        maxcount = max(count, maxcount);
        r++;
    }

    return maxcount;
    }
};
