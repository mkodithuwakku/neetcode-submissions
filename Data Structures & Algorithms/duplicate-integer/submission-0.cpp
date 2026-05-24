class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
       set<int> Set;

        //Iterate through vector
        for (size_t i = 0; i < nums.size(); i++){
            
            // If element is not in the array
            if(Set.find(nums[i]) == Set.end()){
                Set.insert(nums[i]);
            } else {
               return true;
            }
        }
        return false;

    }
};
