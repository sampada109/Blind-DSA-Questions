// Maximum Subarray
// Question Link - https://leetcode.com/problems/maximum-subarray/


class Solution {
public:
    int maxSubArray(vector<int>& nums) {

        // TC - O(n^2), SC - O(1)
        // int maxi = nums[0];
        // for(int i=0; i<nums.size(); i++){
        //     int sum = 0;
        //     for(int j=i; j<nums.size(); j++){
        //         sum += nums[j];
        //         maxi = max(maxi, sum);
        //     }
        // }
        // return maxi;

        // TC - O(n), SC - O(1)
        int sum = 0;
        int maxi = nums[0];

        for(int i=0; i<nums.size(); i++){
            sum += nums[i];
            maxi = max(maxi, sum);
            if(sum < 0){
                sum = 0;
            }
        }

        return maxi;
    }
};
