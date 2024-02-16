class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int le=0;
        int ri=0;
        int zeroo=0;
        for(ri;ri<nums.size();ri++){
            if(nums[ri]==0){zeroo++;}
            if(zeroo>k){
                if(nums[le]==0){zeroo--;}
                le++;
            }
        }
        return ri-le;

    }
};