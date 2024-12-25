# Rotate Array
# Question Link - https://leetcode.com/problems/rotate-array/description/


def reverse(i,j,nums):

    while(i < j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1
        j -= 1

    return nums

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n
        m = n-k

        reverse(m,n-1,nums)

        reverse(0, m-1, nums)

        reverse(0, n-1,nums)
        
