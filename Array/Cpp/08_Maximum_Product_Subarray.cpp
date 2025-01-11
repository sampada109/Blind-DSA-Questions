// Maximum Product Subarray
// Question Link - https://leetcode.com/problems/maximum-product-subarray/description/
// TC - O(n)

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if(nums.size() == 1){
            return nums[0];
        }

        int maxi = INT_MIN;

        int prefix = 1;
        for(int i=0; i<nums.size(); i++){
            if(nums[i] == 0){
                prefix = 1;
                continue;
            }
            prefix *= nums[i];
            maxi = max(maxi, prefix);
        }

        int suffix = 1;
        for(int i=nums.size()-1; i>=0; i--){
            if(nums[i] == 0){
                suffix = 1;
                continue;
            }
            suffix *= nums[i];
            maxi = max(maxi, suffix);
        }

        if(maxi > 0) return maxi;
        else return 0;
    }
};
