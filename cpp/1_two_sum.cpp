#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, vector<int>> info;
        vector<int> rst;
        for (int i = 0; i < nums.size(); i++) {
            info[nums[i]].push_back(i);
        }
        for (int i = 0; i < nums.size(); i++) {
            int a = target - nums[i];
            if (a != nums[i]) {
                if (info.find(a) != info.end()) {
                    rst.push_back(i);
                    rst.push_back(info[a][0]);
                    return rst;
                }
            } else if (a == nums[i] && info[a].size() > 1) {
                rst.push_back(info[a][0]);
                rst.push_back(info[a][1]);
                return rst;
            }
        }
    }
};


int main() {
    int x[10] = {0, 4, 3, 0};
    vector<int> nums(x, x + 4);
    int target = 0;
    Solution so;
    so.twoSum(nums, target);
    return 0;
}