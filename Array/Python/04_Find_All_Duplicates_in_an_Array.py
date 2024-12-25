# Find All Duplicates in an Array
# Question Link - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        ''' using sorting, Time - O(nlogn)
        ans = []
        arr = sorted(nums)
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                ans.append(arr[i]);
        return ans
        '''
      
        mpp = {}
        for i in nums:
            if(i in mpp):
                mpp[i] += 1
            else:
                mpp[i] = 1
        arr = []
        for key,value in mpp.items():
            if(value >= 2):
                arr.append(key)

        return arr
        
        
