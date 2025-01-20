// Find Minimum in Rotated Sorted Array
// Question Link - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
// TC - O(logn)

class Solution {
public:
    int findMin(vector<int>& nums) {
        int mini = INT_MAX;

        int low = 0;
        int high = nums.size()-1;
        
        while(low <= high){
            int mid = (low+high)/2;
            if(nums[low] <= nums[mid]){
                mini = min(mini, nums[low]);
                low = mid + 1;
            }
            else{
                high = mid - 1;
                mini = min(mini, nums[mid]);
            }
        }

        return mini;
    }
};
