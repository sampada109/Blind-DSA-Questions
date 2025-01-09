# Two Sum
# Question Link - https://leetcode.com/problems/two-sum/description/
# Time Complexity - O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mpp = {}

        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in mpp:
                return [mpp[ans], i]
            else:
                mpp[nums[i]] = i

        return []
