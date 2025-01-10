# Maximum Subarray
# Question Link - https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      
      # TC - O(n^2), SC - O(1)
      # maxi = nums[0]
      # for i in range(len(nums)):
      #     sum = 0
      #     for j in range(i, len(nums)):
      #         sum += nums[j]
      #         maxi = max(maxi, sum)

      
      # TC - O(n), SC - O(1)
        sum = 0
        maxi = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            maxi = max(maxi, sum)
            if sum < 0 :
                sum = 0

        return maxi
