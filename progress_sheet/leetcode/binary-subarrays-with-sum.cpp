class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        unordered_map<int,int>mp;
        int sum=0,count=0;

        for (int i=0;i<nums.size();i++){
            sum+=nums[i];
          if(sum==goal){
              count++;
          }
          if(mp.find(sum-goal) != mp.end() ){
              count +=mp[sum-goal];
          }
          
             mp[sum]++; 
          
            }


        
     return count;  
        
    }
};