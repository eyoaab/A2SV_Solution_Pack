class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        vector<int> pre( gain.size()+1);
        pre[0]=0;
        for (int i=0;i<gain.size();i++){
            pre[i+1]=gain[i]+pre[i];
        }  
        sort(pre.begin(),pre.end());
        return pre[ gain.size()];      
    }
};