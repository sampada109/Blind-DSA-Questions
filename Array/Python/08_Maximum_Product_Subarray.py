# Maximum Product Subarray
# Question Link - https://leetcode.com/problems/maximum-product-subarray/description/
# TC - O(n)


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        
        maxi = nums[0]

        prefix = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix = 1
                continue
            prefix *= nums[i]
            maxi = max(maxi, prefix)

        sufix = 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                sufix = 1
                continue
            sufix *= nums[i]
            maxi = max(maxi, sufix)

        if maxi > 0:
            return maxi
        else:
            return 0
