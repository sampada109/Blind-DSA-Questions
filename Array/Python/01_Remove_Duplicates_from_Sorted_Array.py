# Remove Duplicates from Sorted Array
# Question Link - https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        k = 1
        
        while(j < len(nums)):
            
            if(nums[i] == nums[j]):
                j += 1
            else:
                k += 1
                i += 1
                nums[i] = nums[j]
                j += 1
                
        return k
