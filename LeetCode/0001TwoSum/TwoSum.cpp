class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int a, b, c;
        for (int i = 0; i < nums.size(); i++){
            a = i;
            b = target - nums[i];
            for (int j = 0; j < nums.size(); j++){
                if (nums[j] == b){
                    c = j;
                    break;
                }
            }
        }
        
        vector<int> ans;
        ans.push_back(a);
        ans.push_back(c);
        return ans;
    }
};
